# Build clean PDFs for all 4 digital products.
# Run with: miniconda3/python.exe build_pdfs.py
# Output: products/pdfs/  (ready to upload to Gumroad)

import os
import re
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# Brand colors
NAVY    = colors.HexColor('#1a2744')
GOLD    = colors.HexColor('#c9a84c')
LIGHT   = colors.HexColor('#f8f6f1')
GRAY    = colors.HexColor('#666666')
WHITE   = colors.white

BASE = Path(__file__).parent
OUT  = BASE / "products" / "pdfs"
OUT.mkdir(parents=True, exist_ok=True)


def build_styles():
    styles = getSampleStyleSheet()
    custom = {
        'H1': ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=24, textColor=NAVY,
                             spaceAfter=12, spaceBefore=20, alignment=TA_CENTER),
        'H2': ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=16, textColor=NAVY,
                             spaceAfter=8, spaceBefore=16, borderPad=4),
        'H3': ParagraphStyle('H3', fontName='Helvetica-Bold', fontSize=13, textColor=GOLD,
                             spaceAfter=6, spaceBefore=12),
        'Body': ParagraphStyle('Body', fontName='Helvetica', fontSize=11, textColor=colors.HexColor('#333333'),
                               leading=18, spaceAfter=8),
        'Bullet': ParagraphStyle('Bullet', fontName='Helvetica', fontSize=11,
                                 textColor=colors.HexColor('#333333'), leading=16,
                                 leftIndent=20, spaceAfter=4),
        'Sub': ParagraphStyle('Sub', fontName='Helvetica-Oblique', fontSize=10,
                              textColor=GRAY, spaceAfter=6),
        'Cover': ParagraphStyle('Cover', fontName='Helvetica-Bold', fontSize=32, textColor=WHITE,
                                alignment=TA_CENTER, spaceAfter=10),
        'CoverSub': ParagraphStyle('CoverSub', fontName='Helvetica', fontSize=14, textColor=GOLD,
                                   alignment=TA_CENTER),
        'Price': ParagraphStyle('Price', fontName='Helvetica-Bold', fontSize=18, textColor=GOLD,
                                alignment=TA_CENTER, spaceBefore=20),
        'Bold': ParagraphStyle('Bold', fontName='Helvetica-Bold', fontSize=11, textColor=NAVY,
                               spaceAfter=6),
    }
    return custom


def cover_page(elements, title, subtitle, price_label, styles):
    """Navy cover page with gold accents."""
    from reportlab.platypus import Table, TableStyle
    from reportlab.lib.units import inch

    # Spacer to push content down
    elements.append(Spacer(1, 1.5 * inch))

    # Top gold rule
    elements.append(HRFlowable(width="100%", thickness=3, color=GOLD, spaceAfter=20))

    # Brand
    brand_style = ParagraphStyle('brand', fontName='Helvetica', fontSize=11,
                                  textColor=GOLD, alignment=TA_CENTER, spaceAfter=20)
    elements.append(Paragraph("THE RESET METHOD", brand_style))

    # Title
    elements.append(Paragraph(title, styles['Cover']))
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph(subtitle, styles['CoverSub']))
    elements.append(Spacer(1, 0.5 * inch))
    elements.append(HRFlowable(width="60%", thickness=1, color=GOLD, spaceAfter=20))

    elements.append(Paragraph(price_label, styles['Price']))
    elements.append(Spacer(1, 2 * inch))

    footer_style = ParagraphStyle('footer', fontName='Helvetica', fontSize=9,
                                   textColor=GRAY, alignment=TA_CENTER)
    elements.append(Paragraph("theresetmethod.com  |  hello@theresetmethod.com", footer_style))
    elements.append(PageBreak())


def parse_and_render(md_text, elements, styles):
    """Very basic Markdown → ReportLab elements."""
    lines = md_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if not line.strip():
            elements.append(Spacer(1, 6))
            i += 1
            continue

        if line.startswith('### '):
            elements.append(Paragraph(line[4:], styles['H3']))
        elif line.startswith('## '):
            elements.append(Paragraph(line[3:], styles['H2']))
            elements.append(HRFlowable(width="100%", thickness=0.5, color=GOLD, spaceAfter=4))
        elif line.startswith('# '):
            elements.append(Paragraph(line[2:], styles['H1']))
        elif line.startswith('---'):
            elements.append(HRFlowable(width="100%", thickness=1, color=GOLD,
                                        spaceBefore=8, spaceAfter=8))
        elif line.startswith('- ') or line.startswith('* '):
            # Collect bullet block
            bullets = []
            while i < len(lines) and (lines[i].startswith('- ') or lines[i].startswith('* ')):
                bullets.append(lines[i][2:].strip())
                i += 1
            for b in bullets:
                elements.append(Paragraph(f"• {b}", styles['Bullet']))
            continue
        elif re.match(r'^\d+\.', line):
            # Numbered list
            elements.append(Paragraph(line, styles['Bullet']))
        elif line.startswith('**') and line.endswith('**') and len(line) > 4:
            elements.append(Paragraph(line.strip('*'), styles['Bold']))
        else:
            # Inline bold
            rendered = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
            rendered = re.sub(r'\*(.+?)\*', r'<i>\1</i>', rendered)
            elements.append(Paragraph(rendered, styles['Body']))

        i += 1


def build_pdf(md_path: Path, out_path: Path, title: str, subtitle: str, price_label: str):
    print(f"  Building: {out_path.name}")
    styles = build_styles()

    # Page background color via canvas
    def add_background(canvas, doc):
        canvas.saveState()
        if doc.page == 1:
            canvas.setFillColor(NAVY)
            canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
        canvas.restoreState()

    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=letter,
        rightMargin=0.85 * inch,
        leftMargin=0.85 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    elements = []
    cover_page(elements, title, subtitle, price_label, styles)

    md_text = md_path.read_text(encoding='utf-8', errors='replace')
    parse_and_render(md_text, elements, styles)

    doc.build(elements, onFirstPage=add_background, onLaterPages=add_background)
    print(f"  Done -> {out_path}")


PRODUCTS = [
    {
        "md":       BASE / "products/paycheck-reset/COMPANION-GUIDE.md",
        "out":      OUT / "The-Paycheck-Reset.pdf",
        "title":    "The Paycheck Reset",
        "subtitle": "Your Complete System for Monthly Budget Mastery",
        "price":    "Value: $27",
    },
    {
        "md":       BASE / "products/500-challenge/THE-500-CHALLENGE-FULL-CONTENT.md",
        "out":      OUT / "The-500-Challenge.pdf",
        "title":    "The $500 Challenge",
        "subtitle": "30 Days to Your First Emergency Fund",
        "price":    "Value: $17",
    },
    {
        "md":       BASE / "products/boundaries-playbook/ANXIOUS-GIRLS-BOUNDARIES-PLAYBOOK-FULL.md",
        "out":      OUT / "Anxious-Girls-Boundaries-Playbook.pdf",
        "title":    "Anxious Girl's Boundaries Playbook",
        "subtitle": "Scripts & Strategies for Guilt-Free Boundaries",
        "price":    "Value: $29",
    },
    {
        "md":       BASE / "products/calm-brain-toolkit/CALM-BRAIN-TOOLKIT-FULL.md",
        "out":      OUT / "Calm-Brain-Toolkit.pdf",
        "title":    "The Calm Brain Toolkit",
        "subtitle": "CBT-Based Templates for Anxiety & Overthinking",
        "price":    "Value: $32",
    },
]

if __name__ == "__main__":
    print(f"\nBuilding {len(PRODUCTS)} product PDFs -> {OUT}\n")
    for p in PRODUCTS:
        if not p["md"].exists():
            print(f"  SKIP (not found): {p['md']}")
            continue
        build_pdf(p["md"], p["out"], p["title"], p["subtitle"], p["price"])
    print("\nAll done! Upload the PDFs from products/pdfs/ to Gumroad.")
