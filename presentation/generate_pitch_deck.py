from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


OUT_PATH = Path(__file__).with_name("creatortrust_pitch_deck.pptx")

BG = RGBColor(3, 8, 18)
INK = RGBColor(246, 250, 255)
MUTED = RGBColor(160, 176, 197)
DIM = RGBColor(91, 111, 136)
PANEL = RGBColor(10, 22, 38)
PANEL_2 = RGBColor(14, 32, 55)
LINE = RGBColor(31, 54, 82)
CYAN = RGBColor(44, 201, 255)
TEAL = RGBColor(45, 212, 191)
VIOLET = RGBColor(139, 116, 246)
ROSE = RGBColor(251, 100, 131)
AMBER = RGBColor(245, 166, 35)
GREEN = RGBColor(132, 204, 22)


def set_bg(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BG


def txt(slide, value, x, y, w, h, size=18, color=INK, bold=False, align=None, font="Aptos"):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = shape.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = 0
    frame.margin_right = 0
    frame.margin_top = 0
    frame.margin_bottom = 0
    frame.vertical_anchor = MSO_ANCHOR.TOP
    p = frame.paragraphs[0]
    p.text = value
    if align:
        p.alignment = align
    for run in p.runs:
        run.font.name = font
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
    return shape


def panel(slide, x, y, w, h, fill=PANEL, line=LINE, radius=True):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
        Inches(x),
        Inches(y),
        Inches(w),
        Inches(h),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = line
    shape.line.width = Pt(1)
    return shape


def circle(slide, x, y, d, fill=PANEL_2, line=LINE):
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(d), Inches(d))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = line
    shape.line.width = Pt(1)
    return shape


def line(slide, x1, y1, x2, y2, color=LINE, width=1.25):
    shape = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    shape.line.color.rgb = color
    shape.line.width = Pt(width)
    return shape


def theme(slide, section, page, accent=CYAN):
    set_bg(slide)
    rail = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.08), Inches(7.5))
    rail.fill.solid()
    rail.fill.fore_color.rgb = accent
    rail.line.color.rgb = accent
    txt(slide, section.upper(), 0.62, 0.35, 4.0, 0.24, 9.5, accent, True)
    txt(slide, "CreatorTrust Shield", 0.62, 7.02, 3.4, 0.18, 8.5, DIM, True)
    txt(slide, f"{page:02d}", 12.35, 7.02, 0.35, 0.18, 8.5, DIM, True, PP_ALIGN.RIGHT)
    for i in range(6):
        c = circle(slide, 11.25 + i * 0.24, 0.42, 0.035, fill=RGBColor(20, 49, 76), line=RGBColor(20, 49, 76))
    return slide


def title(slide, title_text, sub=None, y=0.82, size=35):
    txt(slide, title_text, 0.62, y, 11.8, 0.95, size, INK, True, font="Aptos Display")
    if sub:
        txt(slide, sub, 0.66, y + 1.02, 9.6, 0.55, 15.5, MUTED)


def card(slide, label, heading, body, x, y, w, h, accent=CYAN):
    panel(slide, x, y, w, h)
    txt(slide, label.upper(), x + 0.22, y + 0.2, w - 0.42, 0.2, 8.5, accent, True)
    txt(slide, heading, x + 0.22, y + 0.48, w - 0.42, 0.35, 16, INK, True)
    txt(slide, body, x + 0.22, y + 0.94, w - 0.45, h - 1.08, 12.5, MUTED)


def metric(slide, value, label, x, y, w, color=CYAN):
    txt(slide, value, x, y, w, 0.48, 30, color, True, font="Aptos Display")
    txt(slide, label, x, y + 0.52, w, 0.55, 11, MUTED)


def build():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # 1. Hero
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    theme(slide, "IAG Hackathon", 1, TEAL)
    title(slide, "CreatorTrust\nShield", "A protection layer for creators when identity becomes the attack surface.", y=1.05, size=48)
    txt(slide, "Trusted registry + simulated monitoring + evidence-backed incident response", 0.72, 4.0, 7.6, 0.38, 16.5, INK, True)
    panel(slide, 8.7, 2.05, 3.25, 2.75, fill=RGBColor(5, 29, 43), line=RGBColor(24, 93, 122))
    txt(slide, "PROTECT", 9.02, 2.42, 2.65, 0.22, 9.5, TEAL, True, PP_ALIGN.CENTER)
    txt(slide, "face\nvoice\ncontent\ntrust", 9.0, 2.88, 2.7, 1.28, 24, INK, True, PP_ALIGN.CENTER)
    txt(slide, "Realise  /  Explore  /  Decide", 0.72, 5.3, 6.0, 0.28, 13, MUTED, True)

    # 2. Human problem
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    theme(slide, "Customer problem", 2, ROSE)
    title(slide, "A fake video can become a real-world crisis.", "The product starts with a creator's lived panic, not with technology.")
    txt(slide, "Scenario", 0.75, 2.35, 2.0, 0.24, 10, ROSE, True)
    txt(slide, "A creator wakes up to a deepfake crypto sponsorship using their face and voice.", 0.75, 2.72, 7.2, 0.55, 22, INK, True)
    line(slide, 0.86, 3.68, 11.85, 3.68, ROSE, 1.6)
    card(slide, "Harm", "Income stops", "Sponsors pause campaigns and followers question what is real.", 0.75, 4.18, 3.45, 1.4, ROSE)
    card(slide, "Harm", "Trust breaks", "The creator has to prove they did not say or endorse the scam.", 4.55, 4.18, 3.45, 1.4, AMBER)
    card(slide, "Harm", "No clear path", "They need evidence, takedown support, sponsor communication and recovery.", 8.35, 4.18, 3.45, 1.4, CYAN)

    # 3. Market/risk proof
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    theme(slide, "Why now", 3, CYAN)
    title(slide, "Creators are small businesses with exposed digital identities.")
    metric(slide, "84,700+", "cybercrime reports received by ACSC in 2024-25", 0.85, 2.35, 3.4, CYAN)
    metric(slide, "$33k", "average reported individual cybercrime loss", 4.55, 2.35, 3.1, TEAL)
    metric(slide, "#1", "identity fraud remained the top reported cybercrime", 8.05, 2.35, 3.8, AMBER)
    panel(slide, 0.85, 4.3, 10.95, 1.35, fill=RGBColor(8, 24, 39), line=LINE)
    txt(slide, "Creator risk is different:", 1.14, 4.63, 2.55, 0.28, 14, TEAL, True)
    txt(slide, "the assets are account access, face, voice, sponsorships, audience trust and reputation.", 3.48, 4.63, 7.9, 0.42, 18, INK, True)

    # 4. Journey fit
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    theme(slide, "Journey fit", 4, VIOLET)
    title(slide, "CreatorTrust maps directly to Realise, Explore and Decide.")
    stages = [
        ("Realise", "I need to protect what I care about.", "My online identity is an asset.", CYAN),
        ("Explore", "What are my options?", "What is authentic, suspicious or impersonation?", TEAL),
        ("Decide", "I need the right cover for me.", "Who helps when an incident happens?", VIOLET),
    ]
    x_positions = [0.75, 4.65, 8.55]
    for idx, (stage, journey, creator, color) in enumerate(stages):
        panel(slide, x_positions[idx], 2.2, 3.25, 2.72, fill=PANEL_2, line=color)
        txt(slide, stage, x_positions[idx] + 0.25, 2.48, 2.7, 0.35, 21, color, True)
        txt(slide, journey, x_positions[idx] + 0.25, 3.05, 2.72, 0.45, 13, MUTED)
        txt(slide, creator, x_positions[idx] + 0.25, 3.88, 2.72, 0.55, 16, INK, True)
    txt(slide, "Design target: make risk visible, options understandable and support believable.", 1.0, 5.55, 11.2, 0.36, 19, INK, True, PP_ALIGN.CENTER)

    # 5. Product architecture
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    theme(slide, "Solution model", 5, TEAL)
    title(slide, "The registry is the source of truth.")
    panel(slide, 4.78, 2.32, 3.75, 1.2, fill=RGBColor(4, 38, 50), line=TEAL)
    txt(slide, "CreatorTrust Registry", 5.1, 2.72, 3.1, 0.28, 19, INK, True, PP_ALIGN.CENTER)
    items = [
        ("Official accounts", 0.85, 2.05, CYAN),
        ("Sponsors", 0.85, 3.55, AMBER),
        ("Original content", 9.15, 2.05, VIOLET),
        ("Face + voice refs", 9.15, 3.55, TEAL),
    ]
    for name, x, y, color in items:
        panel(slide, x, y, 3.0, 0.9, fill=PANEL, line=color)
        txt(slide, name, x + 0.22, y + 0.28, 2.55, 0.2, 14, INK, True, PP_ALIGN.CENTER)
        line(slide, x + (3.0 if x < 4 else 0), y + 0.45, 4.78 if x < 4 else 8.53, 2.92, color, 1.4)
    txt(slide, "Suspicious content is judged against a trusted baseline, not in isolation.", 1.0, 5.35, 11.0, 0.4, 20, INK, True, PP_ALIGN.CENTER)

    # 6. Demo path
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    theme(slide, "Demo", 6, CYAN)
    title(slide, "One end-to-end incident journey in under 45 seconds.")
    steps = [
        ("01", "Registry", "source of truth"),
        ("02", "Upload", "metadata + fingerprints"),
        ("03", "Scan", "four findings"),
        ("04", "Analyse", "likely deepfake"),
        ("05", "Respond", "evidence + actions"),
    ]
    for i, (num, name, detail) in enumerate(steps):
        x = 0.78 + i * 2.45
        circle(slide, x, 2.72, 0.72, fill=RGBColor(5, 40, 57), line=CYAN if i != 3 else ROSE)
        txt(slide, num, x, 2.94, 0.72, 0.18, 10, CYAN if i != 3 else ROSE, True, PP_ALIGN.CENTER)
        txt(slide, name, x - 0.35, 3.68, 1.45, 0.26, 15, INK, True, PP_ALIGN.CENTER)
        txt(slide, detail, x - 0.52, 4.04, 1.82, 0.32, 10.5, MUTED, align=PP_ALIGN.CENTER)
        if i < 4:
            line(slide, x + 0.72, 3.08, x + 2.45, 3.08, LINE, 1.25)
    panel(slide, 1.78, 5.35, 9.7, 0.76, fill=RGBColor(8, 24, 39), line=LINE)
    txt(slide, "Presenter note: show workflow, not every screen. The demo proves response readiness.", 2.05, 5.58, 9.15, 0.22, 14, INK, True, PP_ALIGN.CENTER)

    # 7. Responsible tech
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    theme(slide, "Responsible technology", 7, AMBER)
    title(slide, "We do not overclaim AI.")
    panel(slide, 0.85, 2.25, 5.25, 2.65, fill=PANEL_2, line=TEAL)
    txt(slide, "Demonstrated", 1.15, 2.58, 2.2, 0.28, 17, TEAL, True)
    txt(slide, "Creator registry\nContent metadata\nDeterministic scan\nIncident workflow", 1.15, 3.12, 4.45, 1.15, 18, INK, True)
    panel(slide, 7.25, 2.25, 5.25, 2.65, fill=PANEL_2, line=AMBER)
    txt(slide, "Simulated", 7.55, 2.58, 2.2, 0.28, 17, AMBER, True)
    txt(slide, "AI analysis\nFingerprints\nMonitoring\nTakedown actions", 7.55, 3.12, 4.45, 1.15, 18, INK, True)
    txt(slide, "This is a reliable workflow prototype, not a production detection claim.", 0.95, 5.6, 11.3, 0.42, 20, INK, True, PP_ALIGN.CENTER)

    # 8. Impact and ask
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    theme(slide, "Pilot ask", 8, GREEN)
    title(slide, "Pilot the digital identity protection layer.")
    card(slide, "Target", "Creators and public figures", "Streamers, esports players, influencers, creators and public figures.", 0.85, 2.05, 3.55, 1.85, CYAN)
    card(slide, "Measure", "Trust and response value", "Registration rate, incident actions, sponsor confidence and claim-readiness.", 4.9, 2.05, 3.55, 1.85, TEAL)
    card(slide, "Scale", "Insurance pathway", "Use pilot evidence to test cyber liability support for digital income earners.", 8.95, 2.05, 3.55, 1.85, GREEN)
    txt(slide, "CreatorTrust Shield moves creators from panic to proof, and from proof to action.", 0.9, 5.15, 11.3, 0.6, 23, INK, True, PP_ALIGN.CENTER)

    # 9. Rehearsal slide
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    theme(slide, "Presenter notes", 9, VIOLET)
    title(slide, "3-minute run of show")
    card(slide, "0:00-0:30", "Hook + pain", "Start with the fake sponsorship scenario. Make the harm concrete.", 0.8, 2.05, 3.55, 1.45, ROSE)
    card(slide, "0:30-1:20", "Journey + solution", "Connect Realise, Explore and Decide to the trusted registry concept.", 4.88, 2.05, 3.55, 1.45, CYAN)
    card(slide, "1:20-2:15", "Demo", "Registry -> upload -> scan -> analyse -> incident response.", 8.95, 2.05, 3.55, 1.45, TEAL)
    card(slide, "2:15-3:00", "Impact + ask", "Responsible technology, customer confidence, pilot recommendation.", 2.85, 4.15, 7.7, 1.35, AMBER)

    prs.save(OUT_PATH)


if __name__ == "__main__":
    build()
    print(f"Saved {OUT_PATH}")
