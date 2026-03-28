from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import KeepTogether

NAVY = HexColor('#1B2A4A')
GOLD = HexColor('#D4A017')
LIGHT = HexColor('#F4F6FB')
GRAY = HexColor('#6C757D')
WHITE = white
DARK = HexColor('#2C3E50')
GREEN = HexColor('#27AE60')
ACCENT = HexColor('#E8F4FD')

def build_pdf():
    output_path = 'products/pdfs/Reset-Method-AI-Agent-Pack.pdf'
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('Title', parent=styles['Normal'],
        fontSize=28, textColor=WHITE, fontName='Helvetica-Bold',
        spaceAfter=6, alignment=TA_CENTER)

    subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
        fontSize=14, textColor=GOLD, fontName='Helvetica-Bold',
        spaceAfter=4, alignment=TA_CENTER)

    tagline_style = ParagraphStyle('Tagline', parent=styles['Normal'],
        fontSize=11, textColor=HexColor('#BDC3C7'), fontName='Helvetica',
        spaceAfter=0, alignment=TA_CENTER)

    agent_title_style = ParagraphStyle('AgentTitle', parent=styles['Normal'],
        fontSize=18, textColor=WHITE, fontName='Helvetica-Bold',
        spaceAfter=2, alignment=TA_LEFT)

    agent_sub_style = ParagraphStyle('AgentSub', parent=styles['Normal'],
        fontSize=11, textColor=GOLD, fontName='Helvetica-Oblique',
        spaceAfter=6, alignment=TA_LEFT)

    section_header = ParagraphStyle('SectionHeader', parent=styles['Normal'],
        fontSize=10, textColor=NAVY, fontName='Helvetica-Bold',
        spaceAfter=4, spaceBefore=10, leftIndent=0)

    body_style = ParagraphStyle('Body', parent=styles['Normal'],
        fontSize=10, textColor=DARK, fontName='Helvetica',
        spaceAfter=4, leading=15, alignment=TA_JUSTIFY)

    prompt_style = ParagraphStyle('Prompt', parent=styles['Normal'],
        fontSize=9, textColor=DARK, fontName='Courier',
        spaceAfter=3, leading=14, leftIndent=10, rightIndent=10,
        backColor=ACCENT, borderPadding=8)

    power_style = ParagraphStyle('Power', parent=styles['Normal'],
        fontSize=9.5, textColor=DARK, fontName='Helvetica',
        spaceAfter=3, leading=14, leftIndent=15, bulletIndent=5)

    howto_style = ParagraphStyle('HowTo', parent=styles['Normal'],
        fontSize=9.5, textColor=DARK, fontName='Helvetica',
        spaceAfter=3, leading=14, leftIndent=15)

    toc_style = ParagraphStyle('TOC', parent=styles['Normal'],
        fontSize=11, textColor=DARK, fontName='Helvetica',
        spaceAfter=6, leading=18, leftIndent=20)

    story = []

    # ── COVER PAGE ──
    cover_data = [[
        Paragraph("The Reset Method", ParagraphStyle('c1', parent=styles['Normal'],
            fontSize=13, textColor=GOLD, fontName='Helvetica-Bold', alignment=TA_CENTER)),
        ''
    ]]
    cover_table = Table([[Paragraph(
        '<para align="center"><font color="#1B2A4A" size="1">&#160;</font></para>',
        styles['Normal']
    )]], colWidths=[6.5*inch])

    story.append(Spacer(1, 0.3*inch))

    # Cover block
    cover_bg = Table([[
        Paragraph("THE RESET METHOD", ParagraphStyle('cb1', parent=styles['Normal'],
            fontSize=12, textColor=GOLD, fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=4)),
    ], [
        Paragraph("AI Agent Pack", title_style),
    ], [
        Paragraph("5 Claude Coaches — Available 24/7", subtitle_style),
    ], [
        Spacer(1, 0.1*inch),
    ], [
        Paragraph("Budget · Boundaries · Calm Brain · Paycheck · Life Reset", tagline_style),
    ], [
        Spacer(1, 0.15*inch),
    ], [
        Paragraph("Copy. Paste. Transform.", ParagraphStyle('ct', parent=styles['Normal'],
            fontSize=13, textColor=WHITE, fontName='Helvetica-Oblique', alignment=TA_CENTER)),
    ]], colWidths=[6.5*inch])
    cover_bg.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('TOPPADDING', (0,0), (-1,0), 30),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 30),
        ('LEFTPADDING', (0,0), (-1,-1), 20),
        ('RIGHTPADDING', (0,0), (-1,-1), 20),
        ('ROUNDEDCORNERS', [8]),
    ]))
    story.append(cover_bg)
    story.append(Spacer(1, 0.25*inch))

    # Intro paragraph
    story.append(Paragraph(
        "You're holding 5 fully-configured AI coaches — each one specializing in the exact areas "
        "where most people feel stuck: money, boundaries, anxiety, week-to-week finances, and big-picture life direction. "
        "Each agent uses a professional-grade system prompt that turns Claude into a focused, knowledgeable coach "
        "in that domain. No fluff. No generic advice. Real, specific help — available whenever you need it.",
        body_style))
    story.append(Spacer(1, 0.1*inch))

    # What you get box
    wye_data = [
        [Paragraph("WHAT'S INSIDE THIS PACK", ParagraphStyle('wye', parent=styles['Normal'],
            fontSize=11, textColor=NAVY, fontName='Helvetica-Bold', alignment=TA_CENTER))],
        [Paragraph(
            "✅  Agent 1: Budget Coach Claude — analyzes spending, builds reset plans\n"
            "✅  Agent 2: Boundary Builder Claude — writes word-for-word boundary scripts\n"
            "✅  Agent 3: Calm Brain Coach Claude — CBT sessions on demand\n"
            "✅  Agent 4: Paycheck Planner Claude — manages money between pay periods\n"
            "✅  Agent 5: Reset Strategist Claude — 90-day full life reset coaching\n"
            "✅  Power Prompts for each agent (40+ total)\n"
            "✅  Quick Start Guide — set up any agent in under 5 minutes",
            ParagraphStyle('wyebody', parent=styles['Normal'],
                fontSize=10, textColor=DARK, fontName='Helvetica',
                spaceAfter=0, leading=18, leftIndent=10))]
    ]
    wye_table = Table(wye_data, colWidths=[6.5*inch])
    wye_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT),
        ('TOPPADDING', (0,0), (-1,0), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 15),
        ('RIGHTPADDING', (0,0), (-1,-1), 15),
        ('TOPPADDING', (0,1), (-1,-1), 8),
    ]))
    story.append(wye_table)
    story.append(PageBreak())

    # ── AGENTS ──
    agents = [
        {
            "num": "01",
            "name": "BUDGET COACH CLAUDE",
            "tagline": "Your Personal CFO — Available 24/7",
            "intro": "People pay financial coaches $150-400/hour to do exactly what this agent does: cut through "
                     "the noise, look at your real numbers, and tell you specifically what to change. "
                     "Budget Coach Claude asks the right questions, finds your money leaks, and gives you "
                     "a specific 30-day reset plan — without the judgment.",
            "prompt": (
                "You are Budget Coach, a no-nonsense personal finance coach created by The Reset Method. "
                "Your job is to help the user get a clear picture of their money situation and build a realistic plan to reset it.\n\n"
                "Your approach:\n"
                "- Ask one question at a time to understand their full financial picture before giving advice\n"
                "- Be direct but supportive — no shame, no judgment about where they are right now\n"
                "- Focus on action steps they can take THIS week, not hypothetical future plans\n"
                "- Always give advice ranked by impact (highest impact first)\n"
                "- Use specific numbers, not vague advice like 'spend less'\n\n"
                "When a user shares their spending or bank statement:\n"
                "1. First, summarize what you see in plain language\n"
                "2. Identify the top 3 'money leaks' — where money is disappearing without real value\n"
                "3. Identify any subscriptions or recurring charges that could be cut\n"
                "4. Calculate: what would happen to their financial situation if they cut those leaks?\n"
                "5. Give them a specific 30-day reset plan with dollar amounts\n\n"
                "Key rules:\n"
                "- Never make the user feel bad about past decisions\n"
                "- Always start where they are, not where they 'should' be\n"
                "- End every session with 1-3 specific action steps they can take today\n\n"
                "Start by asking: 'Let's get a clear picture of where you are right now. "
                "What's your biggest money stress at the moment?'"
            ),
            "how_to": [
                "Go to claude.ai and sign in",
                "Click 'Projects' in the left sidebar → 'Create Project'",
                "Name it 'Budget Coach'",
                "Click 'Project Instructions' and paste the system prompt above",
                "Click Save → Start Chat"
            ],
            "powers": [
                '"Here\'s my bank statement from last month: [paste it]"',
                '"I make $[X]/month. My bills are: [list]. Build my budget."',
                '"I have $[X] in debt. What\'s the fastest payoff path?"',
                '"I run out of money before the end of the month. Why?"',
                '"Review my subscriptions and tell me what to cut: [list]"',
                '"I get paid every 2 weeks. Help me divide my paycheck."',
                '"What\'s a realistic savings goal for my income level?"',
                '"Build me a 3-month emergency fund plan."'
            ]
        },
        {
            "num": "02",
            "name": "BOUNDARY BUILDER CLAUDE",
            "tagline": "Your Personal Script Writer for Hard Conversations",
            "intro": "Knowing you need to set a boundary and actually being able to say the words are two "
                     "completely different things. Boundary Builder Claude gives you word-for-word scripts "
                     "for the situations that make your chest tight — and it explains the psychology behind "
                     "each one so you understand why it works.",
            "prompt": (
                "You are Boundary Builder, a communication coach created by The Reset Method who specializes "
                "in helping people who struggle with people-pleasing set healthy, firm boundaries without "
                "destroying their relationships.\n\n"
                "Your specialty is writing word-for-word scripts for real situations. When someone describes "
                "a situation where they need to set a boundary or say no, you:\n"
                "1. Validate that the situation is genuinely hard\n"
                "2. Identify the specific boundary that needs to be set\n"
                "3. Write 2-3 versions ranging from gentle to firm\n"
                "4. Explain the psychology behind why each version works\n"
                "5. Anticipate the most likely pushback and give a response for that too\n\n"
                "Your tone is warm but direct. You don't sugarcoat. You believe in the user's right to "
                "take up space, say no, and protect their energy.\n\n"
                "When writing scripts:\n"
                "- Write them in first person as if the user is speaking\n"
                "- Keep them short — long explanations invite more argument\n"
                "- Always include a 'broken record' response for when they keep pushing\n"
                "- Flag any language that would undermine the boundary\n\n"
                "Start by asking: 'Tell me about the situation where you need to set a boundary. "
                "Who\'s involved and what\'s been happening?'"
            ),
            "how_to": [
                "Go to claude.ai → Projects → Create Project",
                "Name it 'Boundary Builder'",
                "Paste the system prompt into 'Project Instructions'",
                "Save → Start Chat",
                "Describe your situation — be as specific as possible"
            ],
            "powers": [
                '"My [mom/friend/coworker] keeps doing [X]. Write me a script."',
                '"I need to say no to [situation]. Write me what to say."',
                '"Someone always asks me for [favors/money]. I can\'t say no."',
                '"I said yes to something I didn\'t want. How do I take it back?"',
                '"My boss keeps asking me to work late. What do I say?"',
                '"I need to end a draining friendship. What\'s the script?"',
                '"Write me a boundary script at 3 different firmness levels."',
                '"Help me respond to pushback when I set this boundary."'
            ]
        },
        {
            "num": "03",
            "name": "CALM BRAIN COACH CLAUDE",
            "tagline": "CBT Sessions On Demand — No Waiting Room",
            "intro": "Cognitive Behavioral Therapy has the strongest research backing of any therapeutic "
                     "approach for anxiety. Calm Brain Coach uses CBT techniques — thought challenging, "
                     "cognitive restructuring, behavioral activation — to help you interrupt anxiety spirals "
                     "in real time. Available at 2am when the spiraling hits hardest.",
            "prompt": (
                "You are Calm Brain Coach, an anxiety and overthinking support coach created by The Reset Method. "
                "You use Cognitive Behavioral Therapy (CBT) techniques — specifically thought challenging, "
                "behavioral activation, and cognitive restructuring — to help people interrupt anxiety spirals.\n\n"
                "You are NOT a therapist and make this clear if asked. You are a CBT-informed coach.\n\n"
                "Your three modes:\n"
                "1. THOUGHT COURT MODE: Run a structured CBT thought challenge — identify the automatic thought, "
                "examine evidence for and against it, generate a more balanced perspective.\n"
                "2. BRAIN DUMP MODE: Help them empty their mental load, then organize what's actionable vs. anxiety noise.\n"
                "3. EVENING RESET MODE: A calming end-of-day check-in that processes the day and prepares for rest.\n\n"
                "Key principles:\n"
                "- Never dismiss anxiety as 'irrational' — the feeling is real\n"
                "- Always validate before challenging\n"
                "- Use Socratic questions rather than telling them what to think\n"
                "- End every session with one small, concrete action they can take\n\n"
                "Opening: 'Hey — what\'s your brain doing right now? Are you spiraling, overwhelmed, "
                "or winding down for the day?'"
            ),
            "how_to": [
                "Go to claude.ai → Projects → Create Project",
                "Name it 'Calm Brain Coach'",
                "Paste the system prompt into 'Project Instructions'",
                "Save → Start Chat",
                "Tell it what mode you need: Thought Court, Brain Dump, or Evening Reset"
            ],
            "powers": [
                '"I\'m spiraling about [X]. Run me through Thought Court."',
                '"My brain won\'t shut up tonight. Brain dump session."',
                '"I\'m catastrophizing about [situation]. Reality-check me."',
                '"I have 47 things on my mind. Help me sort them."',
                '"Evening reset mode. Here\'s how my day went..."',
                '"I keep thinking [anxious thought] on repeat. Challenge it."',
                '"Big [event/meeting] tomorrow and I\'m anxious. Help me prepare mentally."',
                '"Walk me through a grounding exercise right now."'
            ]
        },
        {
            "num": "04",
            "name": "PAYCHECK PLANNER CLAUDE",
            "tagline": "Your Weekly Money Co-Pilot",
            "intro": "The gap between budgeting in theory and actually making it work paycheck to paycheck is "
                     "the exact gap Paycheck Planner fills. Give it your exact numbers — what you make, "
                     "what you owe, what you want to save — and it tells you exactly what to do with every dollar.",
            "prompt": (
                "You are Paycheck Planner, a weekly money management coach created by The Reset Method. "
                "You specialize in helping people who live paycheck to paycheck build a sustainable system.\n\n"
                "Your core functions:\n"
                "1. PAYCHECK SPLIT: When given take-home pay and bills, create an exact allocation plan.\n"
                "2. PROGRESS TRACKING: When user updates spending mid-period, tell them if they're on track.\n"
                "3. DEBT PAYOFF MATH: Calculate exact payoff timelines and optimal strategies.\n"
                "4. SAVINGS GOAL PLANNING: Break big goals into specific weekly/bi-weekly amounts.\n\n"
                "Rules:\n"
                "- Always work with the exact numbers they give you\n"
                "- Show the math clearly so they understand every dollar\n"
                "- Point out deficits honestly — don't pretend math works if it doesn't\n"
                "- If math doesn't add up, help them find the gap\n"
                "- Celebrate small wins — every dollar saved is progress\n\n"
                "Start by asking: 'Are you paid weekly, bi-weekly, or monthly? And what\'s your take-home pay each period?'"
            ),
            "how_to": [
                "Go to claude.ai → Projects → Create Project",
                "Name it 'Paycheck Planner'",
                "Paste the system prompt into 'Project Instructions'",
                "Save → Start Chat",
                "Tell it your pay schedule and income to get started"
            ],
            "powers": [
                '"I get paid $[X] every 2 weeks. Bills: [list]. Build my paycheck split."',
                '"I have $[X left] until payday. Help me make it last."',
                '"I have $[X] in CC debt at [X]%. Payoff plan?"',
                '"I want to save $1000 in 3 months. Weekly savings amount?"',
                '"I spent $[X] this week. Am I on track?"',
                '"Debt avalanche vs snowball for: [list debts with balances/rates]"',
                '"I got an extra $[X]. What\'s the smartest thing to do with it?"'
            ]
        },
        {
            "num": "05",
            "name": "RESET STRATEGIST CLAUDE",
            "tagline": "Your 90-Day Life Reset Coach (Bonus Agent)",
            "intro": "For when one area isn't the problem — all of them are. Reset Strategist runs you through "
                     "a full Life Audit across 5 areas, identifies your highest-leverage starting point, "
                     "and designs a 3-phase 90-day plan. This is the big-picture coach that helps you stop "
                     "managing symptoms and start building actual systems.",
            "prompt": (
                "You are Reset Strategist, a holistic life coach created by The Reset Method. You specialize "
                "in helping people who feel stuck design and execute a real 90-day reset.\n\n"
                "You approach this like a strategic consultant: ask hard questions, look for root causes, "
                "build systems that stick.\n\n"
                "The Reset Framework covers 5 areas:\n"
                "1. MONEY: Income, expenses, debt, savings\n"
                "2. MIND: Mental health, anxiety, stress, thinking patterns\n"
                "3. RELATIONSHIPS: Boundaries, communication, energy drains\n"
                "4. BODY: Sleep, energy, basic physical health\n"
                "5. WORK/PURPOSE: Career direction, income ceiling, meaning\n\n"
                "Your process:\n"
                "1. Run a Life Audit (5 questions, one per area, rated 1-10)\n"
                "2. Identify the ONE area that, if improved, would most improve all others\n"
                "3. Design a 90-day plan: Stabilize (30 days), Build (30 days), Accelerate (30 days)\n"
                "4. Create a weekly check-in cadence\n\n"
                "Key principle: Most people try to fix everything at once and fix nothing. Find the leverage point.\n\n"
                "Start: 'Let\'s figure out where you actually are, not where you feel like you should be. "
                "I\'m going to ask you to rate 5 areas of your life 1-10. Ready?'"
            ),
            "how_to": [
                "Go to claude.ai → Projects → Create Project",
                "Name it 'Reset Strategist'",
                "Paste the system prompt into 'Project Instructions'",
                "Save → Start Chat",
                "Let it run the Life Audit — be honest with your ratings"
            ],
            "powers": [
                '"I feel stuck in every area of my life. Where do I start?"',
                '"Run me through the Life Audit."',
                '"I\'ve tried to change [X] a hundred times. What\'s really going on?"',
                '"Build me a 90-day reset plan. Here\'s my situation: [describe]"',
                '"Weekly check-in. Here\'s how my week went: [describe]"',
                '"I\'m always managing crises instead of making progress. Why?"',
                '"What\'s my highest-leverage area based on my audit results?"'
            ]
        }
    ]

    for i, agent in enumerate(agents):
        # Agent header block
        header_data = [[
            Paragraph(f"AGENT {agent['num']}", ParagraphStyle('anum', parent=styles['Normal'],
                fontSize=10, textColor=GOLD, fontName='Helvetica-Bold', spaceAfter=2)),
        ], [
            Paragraph(agent['name'], agent_title_style),
        ], [
            Paragraph(f"\" {agent['tagline']} \"", agent_sub_style),
        ]]
        header_table = Table(header_data, colWidths=[6.5*inch])
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), NAVY),
            ('TOPPADDING', (0,0), (-1,0), 14),
            ('BOTTOMPADDING', (0,-1), (-1,-1), 14),
            ('LEFTPADDING', (0,0), (-1,-1), 16),
            ('RIGHTPADDING', (0,0), (-1,-1), 16),
        ]))
        story.append(header_table)
        story.append(Spacer(1, 0.12*inch))

        # Intro
        story.append(Paragraph(agent['intro'], body_style))
        story.append(Spacer(1, 0.08*inch))

        # System prompt label
        prompt_label = Table([[
            Paragraph("▶  SYSTEM PROMPT — Copy everything below and paste into Claude Project Instructions",
                ParagraphStyle('pl', parent=styles['Normal'],
                    fontSize=9, textColor=WHITE, fontName='Helvetica-Bold'))
        ]], colWidths=[6.5*inch])
        prompt_label.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), NAVY),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
        ]))
        story.append(prompt_label)

        # System prompt box
        lines = agent['prompt'].split('\n')
        prompt_paras = []
        for line in lines:
            if line.strip():
                prompt_paras.append(Paragraph(line, ParagraphStyle('pp', parent=styles['Normal'],
                    fontSize=8.5, textColor=DARK, fontName='Courier', spaceAfter=2, leading=13)))
            else:
                prompt_paras.append(Spacer(1, 4))

        prompt_box = Table([[p] for p in prompt_paras], colWidths=[6.5*inch])
        prompt_box.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), ACCENT),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,-1), (-1,-1), 8),
            ('LEFTPADDING', (0,0), (-1,-1), 12),
            ('RIGHTPADDING', (0,0), (-1,-1), 12),
            ('TOPPADDING', (0,0), (0,0), 10),
        ]))
        story.append(prompt_box)
        story.append(Spacer(1, 0.12*inch))

        # How to use
        story.append(Paragraph("HOW TO SET UP THIS AGENT (5 minutes)", section_header))
        for j, step in enumerate(agent['how_to'], 1):
            story.append(Paragraph(f"  {j}.  {step}", howto_style))
        story.append(Spacer(1, 0.08*inch))

        # Power prompts
        story.append(Paragraph("POWER PROMPTS — Start with these:", section_header))
        for pp in agent['powers']:
            story.append(Paragraph(f"  •  {pp}", power_style))

        if i < len(agents) - 1:
            story.append(PageBreak())
        else:
            story.append(Spacer(1, 0.3*inch))

    # ── QUICK START GUIDE ──
    story.append(PageBreak())
    qs_header = Table([[
        Paragraph("QUICK START GUIDE", ParagraphStyle('qsh', parent=styles['Normal'],
            fontSize=20, textColor=WHITE, fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=4)),
    ], [
        Paragraph("Set Up Any Agent in Under 5 Minutes", ParagraphStyle('qss', parent=styles['Normal'],
            fontSize=12, textColor=GOLD, fontName='Helvetica-Oblique', alignment=TA_CENTER)),
    ]], colWidths=[6.5*inch])
    qs_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('TOPPADDING', (0,0), (-1,0), 20),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 20),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
    ]))
    story.append(qs_header)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("What You Need", ParagraphStyle('qsneed', parent=styles['Normal'],
        fontSize=12, textColor=NAVY, fontName='Helvetica-Bold', spaceAfter=6)))
    story.append(Paragraph(
        "• A Claude account — free at claude.ai (Claude Pro gives better performance and longer sessions)\n"
        "• The system prompt for the agent you want to set up (in this document)\n"
        "• About 5 minutes", body_style))
    story.append(Spacer(1, 0.15*inch))

    steps = [
        ("Step 1", "Go to claude.ai and sign in (or create a free account)"),
        ("Step 2", "Click 'Projects' in the left sidebar"),
        ("Step 3", "Click 'Create Project' and give it a name (e.g., 'Budget Coach')"),
        ("Step 4", "Click 'Add Instructions' or 'Project Instructions'"),
        ("Step 5", "Copy the system prompt from this document — everything in the blue box"),
        ("Step 6", "Paste it into the instructions field and click Save"),
        ("Step 7", "Click 'Start Chat' to begin using your agent"),
        ("Step 8", "Repeat for each of the 5 agents — each one is its own Project"),
    ]

    story.append(Paragraph("Step-by-Step Setup", ParagraphStyle('qsneed', parent=styles['Normal'],
        fontSize=12, textColor=NAVY, fontName='Helvetica-Bold', spaceAfter=8)))

    for step_label, step_text in steps:
        row = Table([[
            Paragraph(step_label, ParagraphStyle('sl', parent=styles['Normal'],
                fontSize=9, textColor=WHITE, fontName='Helvetica-Bold', alignment=TA_CENTER)),
            Paragraph(step_text, ParagraphStyle('st', parent=styles['Normal'],
                fontSize=10, textColor=DARK, fontName='Helvetica', leading=14))
        ]], colWidths=[0.9*inch, 5.6*inch])
        row.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), NAVY),
            ('BACKGROUND', (1,0), (1,0), LIGHT),
            ('TOPPADDING', (0,0), (-1,-1), 7),
            ('BOTTOMPADDING', (0,0), (-1,-1), 7),
            ('LEFTPADDING', (0,0), (0,0), 5),
            ('LEFTPADDING', (1,0), (1,0), 10),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(row)
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 0.2*inch))

    # Which agent first
    story.append(Paragraph("Which Agent Should You Start With?", ParagraphStyle('qsneed', parent=styles['Normal'],
        fontSize=12, textColor=NAVY, fontName='Helvetica-Bold', spaceAfter=8)))

    which_data = [
        ["If your biggest stress is...", "Start with..."],
        ["Money — running out, debt, no savings", "Agent 1: Budget Coach or Agent 4: Paycheck Planner"],
        ["Anxiety, overthinking, can't sleep", "Agent 3: Calm Brain Coach"],
        ["People-pleasing, can't say no", "Agent 2: Boundary Builder"],
        ["Stuck in life overall, don't know where to start", "Agent 5: Reset Strategist"],
    ]
    which_table = Table(which_data, colWidths=[3*inch, 3.5*inch])
    which_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9.5),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [LIGHT, WHITE]),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 0.5, HexColor('#CCCCCC')),
    ]))
    story.append(which_table)

    story.append(Spacer(1, 0.25*inch))

    # Tips
    story.append(Paragraph("Tips for Best Results", ParagraphStyle('qsneed', parent=styles['Normal'],
        fontSize=12, textColor=NAVY, fontName='Helvetica-Bold', spaceAfter=8)))
    tips = [
        "Be specific — the more detail you give, the better the coaching",
        "Use the Power Prompts as starting points, then keep the conversation going",
        "You can share files, paste text, or just describe your situation in your own words",
        "The agent remembers everything within a Project session — you can continue where you left off",
        "Return to the same Project anytime — your conversation history stays there",
        "For best results, use Claude Pro — longer sessions, faster responses, better reasoning",
    ]
    for tip in tips:
        story.append(Paragraph(f"✓  {tip}", ParagraphStyle('tip', parent=styles['Normal'],
            fontSize=10, textColor=DARK, fontName='Helvetica', spaceAfter=5, leading=15, leftIndent=10)))

    # Footer
    story.append(Spacer(1, 0.3*inch))
    story.append(HRFlowable(width='100%', thickness=1, color=GOLD))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "The Reset Method  ·  Fix Your Money, Mind & Life  ·  battlecaster.gumroad.com",
        ParagraphStyle('footer', parent=styles['Normal'],
            fontSize=9, textColor=GRAY, fontName='Helvetica', alignment=TA_CENTER)))

    doc.build(story)
    print(f"PDF created: {output_path}")
    return output_path

if __name__ == '__main__':
    path = build_pdf()
    import os
    size = os.path.getsize(path)
    print(f"Size: {size:,} bytes ({size/1024:.1f} KB)")
