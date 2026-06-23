from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt


OUT_PATH = Path(__file__).with_name("creatortrust_shield_pitch_deck_v2_designer.pptx")

BG = RGBColor(4, 10, 20)
BG_2 = RGBColor(7, 17, 31)
PANEL = RGBColor(12, 24, 40)
PANEL_2 = RGBColor(15, 32, 53)
INK = RGBColor(242, 248, 255)
MUTED = RGBColor(164, 179, 199)
DIM = RGBColor(106, 124, 148)
CYAN = RGBColor(48, 199, 245)
TEAL = RGBColor(45, 212, 191)
PURPLE = RGBColor(167, 139, 250)
ROSE = RGBColor(251, 113, 133)
AMBER = RGBColor(251, 191, 36)
LINE = RGBColor(31, 52, 77)
WHITE = RGBColor(255, 255, 255)


def rgb(hex_value):
    value = hex_value.lstrip("#")
    return RGBColor(int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16))


def set_bg(slide, color=BG):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def box(slide, x, y, w, h, fill=PANEL, line=LINE, radius=True):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(shape_type, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = line
    shp.line.width = Pt(1)
    return shp


def text(slide, value, x, y, w, h, size=24, color=INK, bold=False, align=None):
    shp = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shp.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.text = value
    if align:
        p.alignment = align
    for run in p.runs:
        run.font.name = "Aptos Display"
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
    return shp


def para(slide, lines, x, y, w, h, size=18, color=MUTED, gap=0.1):
    shp = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shp.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.space_after = Pt(gap * 10)
        for run in p.runs:
            run.font.name = "Aptos"
            run.font.size = Pt(size)
            run.font.color.rgb = color
    return shp


def label(slide, value, x=0.7, y=0.45):
    text(slide, value.upper(), x, y, 4.4, 0.28, 10.5, TEAL, True)


def title(slide, value, sub=None):
    text(slide, value, 0.7, 0.82, 11.8, 1.15, 34, INK, True)
    if sub:
        text(slide, sub, 0.72, 1.93, 9.5, 0.55, 16, MUTED)


def footer(slide, number):
    text(slide, "CreatorTrust Shield", 0.7, 7.04, 3.2, 0.2, 8.5, DIM, True)
    text(slide, f"{number:02d}", 12.25, 7.02, 0.4, 0.2, 8.5, DIM, True, PP_ALIGN.RIGHT)


def accent_bar(slide, color=CYAN):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.09), Inches(7.5))
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.color.rgb = color


def dot_grid(slide):
    for x in [9.7, 10.1, 10.5, 10.9, 11.3, 11.7, 12.1]:
        for y in [0.55, 0.95, 1.35, 1.75, 2.15]:
            c = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(0.045), Inches(0.045))
            c.fill.solid()
            c.fill.fore_color.rgb = RGBColor(22, 58, 88)
            c.line.color.rgb = RGBColor(22, 58, 88)


def pill(slide, value, x, y, w, color=CYAN, text_color=BG):
    shp = box(slide, x, y, w, 0.34, fill=color, line=color)
    text(slide, value, x, y + 0.07, w, 0.18, 8.5, text_color, True, PP_ALIGN.CENTER)
    return shp


def card(slide, heading, body, x, y, w, h, accent=CYAN):
    box(slide, x, y, w, h, fill=PANEL, line=LINE)
    text(slide, heading, x + 0.24, y + 0.22, w - 0.45, 0.35, 15, accent, True)
    text(slide, body, x + 0.24, y + 0.72, w - 0.5, h - 0.88, 13.5, MUTED)


def stat(slide, value, label_text, x, y, w, accent=CYAN):
    text(slide, value, x, y, w, 0.48, 28, accent, True)
    text(slide, label_text, x, y + 0.52, w, 0.52, 11.5, MUTED)


def connector(slide, x1, y1, x2, y2, color=LINE):
    line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    line.line.color.rgb = color
    line.line.width = Pt(1.5)


def add_speaker_notes(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    accent_bar(slide, PURPLE)
    label(slide, "Presenter mode")
    title(slide, "3 minute delivery guide", "Use this as the final rehearsal slide, not as part of the live pitch.")
    card(slide, "Opening", "Lead with the fake sponsorship scenario. Make it human before showing the product.", 0.75, 2.35, 3.8, 1.45, CYAN)
    card(slide, "Demo", "Keep the live walkthrough under 45 seconds. Dashboard -> Registry -> Scan -> Analyse -> Incident response.", 4.78, 2.35, 3.8, 1.45, TEAL)
    card(slide, "Responsible tech", "Say clearly that AI evidence is simulated and deterministic. The prototype proves workflow, not model accuracy.", 8.8, 2.35, 3.8, 1.45, PURPLE)
    card(slide, "Close", "Ask IAG to pilot the protection layer for digital identity, then measure trust, response usage, and claim readiness.", 2.75, 4.45, 7.85, 1.4, AMBER)
    footer(slide, 9)


def build():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # 1 Hero
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    accent_bar(slide, TEAL)
    dot_grid(slide)
    label(slide, "IAG Hackathon")
    text(slide, "CreatorTrust\nShield", 0.72, 1.2, 7.2, 1.7, 46, INK, True)
    text(slide, "AI deepfake protection and cyber liability support for content creators.", 0.78, 3.05, 7.6, 0.55, 19, MUTED)
    pill(slide, "Realise", 0.78, 4.02, 1.2, CYAN)
    pill(slide, "Explore", 2.12, 4.02, 1.2, TEAL)
    pill(slide, "Decide", 3.46, 4.02, 1.2, PURPLE, WHITE)
    box(slide, 8.25, 2.25, 3.75, 2.35, fill=RGBColor(8, 24, 39), line=RGBColor(20, 83, 111))
    text(slide, "Protect the creator's", 8.58, 2.62, 3.0, 0.32, 14, MUTED)
    text(slide, "face, voice,\ncontent and trust", 8.55, 3.02, 3.1, 0.95, 25, INK, True)
    footer(slide, 1)

    # 2 Problem
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    accent_bar(slide, ROSE)
    label(slide, "Problem")
    title(slide, "What if your face sold a scam you never approved?")
    text(slide, "A fake sponsorship video can damage income, sponsor trust, privacy and audience safety overnight.", 0.75, 2.1, 10.4, 0.6, 20, INK, True)
    stat(slide, "1", "deepfake or impersonation incident can trigger multiple harms", 0.85, 3.25, 3.2, ROSE)
    stat(slide, "$", "lost sponsorships, takedown costs, legal costs and reputation recovery", 4.45, 3.25, 3.6, AMBER)
    stat(slide, "?", "creators often do not know what is provable or who can help", 8.55, 3.25, 3.5, CYAN)
    text(slide, "Customer pain: panic, uncertainty, reputational damage and no clear response path.", 0.85, 5.3, 11.5, 0.5, 21, INK, True, PP_ALIGN.CENTER)
    footer(slide, 2)

    # 3 Journey
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    accent_bar(slide, CYAN)
    label(slide, "IAG journey fit")
    title(slide, "The product is designed around the moments customers struggle")
    stages = [
        ("Realise", "My online identity is worth protecting.", CYAN),
        ("Explore", "What is authentic, suspicious or impersonation?", TEAL),
        ("Decide", "Who helps me when an identity incident happens?", PURPLE),
    ]
    xs = [0.9, 4.75, 8.6]
    for i, (stage, copy, color) in enumerate(stages):
        card(slide, stage, copy, xs[i], 2.55, 3.25, 1.55, color)
        if i < 2:
            connector(slide, xs[i] + 3.25, 3.32, xs[i + 1], 3.32, color)
    text(slide, "Fixes journey pain points: unclear options, hard-to-understand products, inconsistent support and low confidence.", 1.05, 5.25, 11.1, 0.6, 20, INK, True, PP_ALIGN.CENTER)
    footer(slide, 3)

    # 4 Solution model
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    accent_bar(slide, TEAL)
    label(slide, "Solution")
    title(slide, "A trusted registry turns identity chaos into evidence")
    center = box(slide, 4.75, 2.55, 3.8, 1.2, fill=RGBColor(8, 39, 52), line=CYAN)
    text(slide, "CreatorTrust Registry", 5.08, 2.92, 3.1, 0.32, 20, INK, True, PP_ALIGN.CENTER)
    nodes = [
        ("Official accounts", 0.85, 2.25, CYAN),
        ("Sponsors", 0.85, 3.72, TEAL),
        ("Original content", 9.15, 2.25, PURPLE),
        ("Face + voice refs", 9.15, 3.72, AMBER),
    ]
    for heading, x, y, color in nodes:
        card(slide, heading, "Registered source of truth", x, y, 3.0, 0.95, color)
        connector(slide, x + (3.0 if x < 4 else 0), y + 0.48, 4.75 if x < 4 else 8.55, 3.15, color)
    text(slide, "Not a generic deepfake detector. A registry + AI evidence workflow that is explainable for creators and insurers.", 0.95, 5.45, 11.2, 0.56, 20, INK, True, PP_ALIGN.CENTER)
    footer(slide, 4)

    # 5 Demo storyboard
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    accent_bar(slide, PURPLE)
    label(slide, "Prototype demo")
    title(slide, "One reliable end-to-end identity protection journey")
    steps = [
        ("01", "Dashboard", "Verified creator profile"),
        ("02", "Registry", "Accounts, sponsors, content"),
        ("03", "Scan", "Deterministic findings"),
        ("04", "Analyse", "Registry + simulated AI evidence"),
        ("05", "Respond", "Evidence package and actions"),
    ]
    for i, (num, heading, body) in enumerate(steps):
        x = 0.65 + i * 2.52
        box(slide, x, 2.55, 2.12, 2.25, fill=PANEL_2, line=LINE)
        text(slide, num, x + 0.22, 2.82, 0.6, 0.3, 12, TEAL, True)
        text(slide, heading, x + 0.22, 3.2, 1.68, 0.3, 17, INK, True)
        text(slide, body, x + 0.22, 3.72, 1.72, 0.55, 11.5, MUTED)
    text(slide, "Demo rule: show the workflow, not every detail. Keep it under 45 seconds.", 0.9, 5.55, 11.3, 0.5, 20, INK, True, PP_ALIGN.CENTER)
    footer(slide, 5)

    # 6 Responsible tech
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    accent_bar(slide, AMBER)
    label(slide, "Responsible technology")
    title(slide, "We prove the workflow without overclaiming AI")
    card(slide, "What is real in the prototype", "Trusted creator profile, registry workflow, content metadata, deterministic findings, incident actions and reset.", 0.75, 2.35, 5.75, 2.2, TEAL)
    card(slide, "What is simulated", "SHA-256 values, fingerprints, monitoring, AI deepfake evidence, platform actions and insurance assessment.", 6.85, 2.35, 5.75, 2.2, AMBER)
    text(slide, "This is decision support and incident workflow design, not a production AI claim.", 0.95, 5.4, 11.0, 0.58, 22, INK, True, PP_ALIGN.CENTER)
    footer(slide, 6)

    # 7 Impact
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    accent_bar(slide, TEAL)
    label(slide, "Customer impact")
    title(slide, "From panic to a clear response path")
    card(slide, "Before", "I do not know if this is provable. I do not know how to tell my sponsor. I do not know what action to take.", 0.75, 2.35, 5.75, 2.25, ROSE)
    card(slide, "After", "I have a source of truth, evidence-backed classification and guided response actions.", 6.85, 2.35, 5.75, 2.25, TEAL)
    text(slide, "Outcome: faster recovery, stronger sponsor trust and safer digital participation.", 0.9, 5.45, 11.4, 0.6, 22, INK, True, PP_ALIGN.CENTER)
    footer(slide, 7)

    # 8 Judging/ask
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    accent_bar(slide, CYAN)
    label(slide, "Recommendation")
    title(slide, "Pilot the digital identity protection layer")
    card(slide, "Customer value", "Protects income, trust, reputation and safety when AI identity attacks happen.", 0.75, 2.0, 3.75, 1.65, CYAN)
    card(slide, "Responsible tech", "Uses a trusted registry plus simulated AI evidence, with no perfect-detection claim.", 4.8, 2.0, 3.75, 1.65, TEAL)
    card(slide, "Pitch clarity", "Problem -> journey -> solution -> demo -> impact -> pilot ask.", 8.85, 2.0, 3.75, 1.65, PURPLE)
    card(slide, "Iteration", "Narrowed from broad cyber insurance to a concrete identity-protection workflow.", 2.8, 4.15, 3.75, 1.45, AMBER)
    card(slide, "Pilot ask", "Test adoption, response usage, sponsor confidence and future claim assessment quality.", 6.85, 4.15, 3.75, 1.45, CYAN)
    footer(slide, 8)

    add_speaker_notes(prs)

    prs.save(OUT_PATH)


if __name__ == "__main__":
    build()
    print(f"Saved {OUT_PATH}")
