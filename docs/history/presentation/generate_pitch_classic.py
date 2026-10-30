from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt


OUT_PATH = Path(__file__).with_name("creatortrust_pitch_classic.pptx")

NAVY = RGBColor(7, 17, 31)
PANEL = RGBColor(13, 27, 45)
INK = RGBColor(238, 246, 255)
MUTED = RGBColor(174, 188, 207)
CYAN = RGBColor(57, 198, 244)
TEAL = RGBColor(56, 224, 194)
PURPLE = RGBColor(167, 139, 250)
ORANGE = RGBColor(251, 146, 60)
LINE = RGBColor(31, 52, 77)


def set_background(slide, color=NAVY):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_textbox(slide, text, x, y, w, h, font_size=24, color=INK, bold=False, align=None):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    if align:
        p.alignment = align
    run = p.runs[0]
    run.font.name = "Aptos"
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = color
    return box


def add_multiline(slide, lines, x, y, w, h, font_size=20, color=MUTED, bullet=False):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    for idx, line in enumerate(lines):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = line
        p.level = 0
        if bullet:
            p.text = line
            p._p.get_or_add_pPr().insert(0, p._p.get_or_add_pPr()._new_buChar())
        for run in p.runs:
            run.font.name = "Aptos"
            run.font.size = Pt(font_size)
            run.font.color.rgb = color
    return box


def add_title(slide, eyebrow, title, subtitle=None):
    add_textbox(slide, eyebrow.upper(), 0.62, 0.45, 6.5, 0.35, 12, TEAL, True)
    add_textbox(slide, title, 0.62, 0.9, 11.8, 1.2, 34, INK, True)
    if subtitle:
        add_textbox(slide, subtitle, 0.66, 2.05, 10.9, 0.75, 18, MUTED)


def add_card(slide, title, body, x, y, w, h, accent=CYAN):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = PANEL
    shape.line.color.rgb = LINE
    shape.line.width = Pt(1)
    add_textbox(slide, title, x + 0.22, y + 0.18, w - 0.44, 0.36, 16, accent, True)
    if isinstance(body, list):
        add_multiline(slide, body, x + 0.28, y + 0.68, w - 0.55, h - 0.85, 14, INK)
    else:
        add_textbox(slide, body, x + 0.22, y + 0.68, w - 0.44, h - 0.86, 15, MUTED)


def add_footer(slide, text="CreatorTrust Shield | IAG Hackathon"):
    add_textbox(slide, text, 0.62, 7.05, 7.5, 0.25, 9, RGBColor(126, 143, 166))


def add_notes_slide(prs, title, body):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    add_title(slide, "Speaker notes", title)
    add_textbox(slide, body, 0.8, 2.0, 11.7, 4.6, 17, MUTED)
    add_footer(slide)


def build_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # 1
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    add_textbox(slide, "IAG HACKATHON PITCH", 0.65, 0.62, 6.0, 0.35, 13, TEAL, True)
    add_textbox(slide, "CreatorTrust Shield", 0.62, 1.24, 11.7, 0.9, 40, INK, True)
    add_textbox(
        slide,
        "AI deepfake protection and cyber liability support for content creators.",
        0.68,
        2.18,
        10.5,
        0.55,
        20,
        MUTED,
    )
    add_card(slide, "Realise", "My account, face, voice, sponsors, and content are assets.", 0.75, 3.25, 3.65, 1.35, CYAN)
    add_card(slide, "Explore", "I need a clear way to check what is authentic or suspicious.", 4.85, 3.25, 3.65, 1.35, TEAL)
    add_card(slide, "Decide", "I need confidence that support exists if something goes wrong.", 8.95, 3.25, 3.65, 1.35, PURPLE)
    add_footer(slide)

    # 2
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    add_title(slide, "Start with the problem", "What if your face sold a scam you never approved?")
    add_textbox(
        slide,
        "A fake sponsorship video can damage income, reputation, sponsor trust, privacy, and audience safety.",
        0.68,
        2.1,
        11.4,
        0.75,
        22,
        INK,
        True,
    )
    add_card(slide, "Creator pain", "A deepfaked creator may not know what is provable, how to explain it, or who can help.", 0.75, 3.25, 5.8, 1.75, CYAN)
    add_card(slide, "Business pain", "Sponsorships, revenue, audience trust, legal cost, takedown cost, and stress can hit together.", 6.85, 3.25, 5.8, 1.75, ORANGE)
    add_footer(slide)

    # 3
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    add_title(slide, "Customer journey fit", "Designed around IAG's Realise, Explore, and Decide stages")
    add_card(slide, "Realise", "\"My online identity is worth protecting.\"", 0.75, 2.15, 3.8, 2.0, CYAN)
    add_card(slide, "Explore", "\"What is authentic, suspicious, or impersonation?\"", 4.75, 2.15, 3.8, 2.0, TEAL)
    add_card(slide, "Decide", "\"Who helps me if an identity incident happens?\"", 8.75, 2.15, 3.8, 2.0, PURPLE)
    add_textbox(
        slide,
        "Addresses IAG journey pains: unclear choices, hard-to-understand products, and inconsistent support.",
        0.85,
        5.0,
        11.4,
        0.65,
        20,
        MUTED,
    )
    add_footer(slide)

    # 4
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    add_title(slide, "The solution", "A trusted registry plus evidence-backed incident response")
    steps = [
        ("1", "Verified creator registry"),
        ("2", "Original content fingerprints"),
        ("3", "Simulated monitoring scan"),
        ("4", "Registry + AI analysis"),
        ("5", "Incident response actions"),
    ]
    x = 0.55
    for num, label in steps:
        add_card(slide, num, label, x, 2.35, 2.35, 1.55, CYAN if num in ["1", "4"] else TEAL)
        x += 2.55
    add_textbox(
        slide,
        "Responsible claim: we do not promise perfect deepfake detection. We combine AI evidence with a trusted source of truth.",
        0.75,
        4.75,
        11.8,
        0.8,
        20,
        INK,
        True,
    )
    add_footer(slide)

    # 5
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    add_title(slide, "Show the demo", "One complete vertical slice")
    add_card(
        slide,
        "Demo path",
        [
            "Dashboard",
            "Trusted registry",
            "Register original content",
            "Run monitoring scan",
            "Analyse fake sponsorship",
            "Open incident response",
        ],
        0.75,
        2.05,
        5.8,
        3.6,
        CYAN,
    )
    add_card(
        slide,
        "What the prototype proves",
        [
            "Clear source of truth",
            "Deterministic suspicious findings",
            "Registry evidence separated from simulated AI evidence",
            "Actionable response workflow",
        ],
        6.85,
        2.05,
        5.8,
        3.6,
        TEAL,
    )
    add_footer(slide)

    # 6
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    add_title(slide, "Customer impact", "From panic to a clear response path")
    add_card(slide, "Before", "\"I do not know if this video is provable, how to explain it, or what action to take.\"", 0.75, 2.25, 5.8, 2.0, ORANGE)
    add_card(slide, "After", "\"I have a source of truth, evidence-backed classification, and guided actions.\"", 6.85, 2.25, 5.8, 2.0, TEAL)
    add_textbox(
        slide,
        "Value created: faster recovery, stronger sponsor trust, safer digital participation.",
        0.85,
        5.1,
        11.5,
        0.65,
        24,
        INK,
        True,
        PP_ALIGN.CENTER,
    )
    add_footer(slide)

    # 7
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    add_title(slide, "Recommendation", "Pilot CreatorTrust Shield with digital income earners")
    add_card(slide, "Target", "Creators, streamers, esports players, influencers, and public figures.", 0.75, 2.25, 3.7, 2.2, CYAN)
    add_card(slide, "Test", "Registry adoption, monitoring value, response completion, and future claim assessment quality.", 4.82, 2.25, 3.7, 2.2, TEAL)
    add_card(slide, "Why IAG", "Cyber risk, customer trust, incident support, and insurance assessment belong together.", 8.9, 2.25, 3.7, 2.2, PURPLE)
    add_textbox(slide, "Pilot, learn, then scale responsibly.", 0.75, 5.25, 11.8, 0.55, 24, INK, True, PP_ALIGN.CENTER)
    add_footer(slide)

    # 8
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    add_title(slide, "Iteration", "What we improved")
    add_card(slide, "From broad to focused", "Narrowed from generic creator cyber insurance to identity protection and deepfake response.", 0.75, 2.1, 5.8, 1.6, CYAN)
    add_card(slide, "From overclaim to responsible", "Kept AI analysis simulated and deterministic; framed it as evidence support, not perfect detection.", 6.85, 2.1, 5.8, 1.6, TEAL)
    add_card(slide, "From concept to demo", "Built one reliable journey: registry, scan, analysis, incident actions, and reset.", 0.75, 4.0, 5.8, 1.6, PURPLE)
    add_card(slide, "From product to journey", "Aligned value to IAG's Realise, Explore, and Decide stages.", 6.85, 4.0, 5.8, 1.6, ORANGE)
    add_footer(slide)

    # Optional notes slide
    add_notes_slide(
        prs,
        "3 minute delivery reminder",
        "Open with the fake sponsorship scenario. Keep the demo under 45 seconds. Emphasise responsible tech: simulated AI, deterministic findings, no perfect detection claim. Close with the pilot ask and IAG journey fit.",
    )

    prs.save(OUT_PATH)


if __name__ == "__main__":
    build_deck()
    print(f"Saved {OUT_PATH}")
