import pandas as pd
import plotly.express as px
import streamlit as st

from utils import add_source_note, apply_dark_chart_theme, format_currency, kpi_card, latest_year_frame


def render_card_grid(cards):
    card_html = ['<div class="card-grid">']
    for card in cards:
        proof = card.get("proof", "")
        proof_html = f'<div class="pitch-card-proof">{proof}</div>' if proof else ""
        card_html.append(
            f"""
            <div class="pitch-card">
                <div class="pitch-card-label">{card["label"]}</div>
                <div class="pitch-card-title">{card["title"]}</div>
                <div class="pitch-card-body">{card["body"]}</div>
                {proof_html}
            </div>
            """
        )
    card_html.append("</div>")
    st.markdown("".join(card_html), unsafe_allow_html=True)


def render(df):
    st.header("Why IAG?")
    st.markdown(
        '<div class="insight">IAG can use its insurance expertise and trusted Australian presence '
        "to create a cyber insurance product for digital income earners.</div>",
        unsafe_allow_html=True,
    )

    avg_selected_loss = 0
    max_selected_loss = 0
    if not df.empty:
        latest = latest_year_frame(df)
        avg_selected_loss = float(latest["estimated_creator_loss_aud"].mean())
        max_selected_loss = float(latest["estimated_creator_loss_aud"].max())

    c1, c2, c3 = st.columns(3)
    with c1:
        kpi_card("Pilot segment", "Content creators")
    with c2:
        kpi_card("Core proposition", "Cyber + income")
    with c3:
        kpi_card("Selected risk signal", format_currency(avg_selected_loss), "Average latest-year demo loss for selected creator groups.")

    st.subheader("IAG Strategic Fit Dashboard")
    fit_scores = pd.DataFrame(
        [
            {"Capability": "Insurance scale", "Fit score": 5, "Why it supports the pilot": "Ability to test, price, govern, and scale a new protection product"},
            {"Capability": "Claims capability", "Fit score": 5, "Why it supports the pilot": "Cyber incidents need fast triage, recovery partners, and clear claims handling"},
            {"Capability": "Trusted brands", "Fit score": 4, "Why it supports the pilot": "Brands such as NRMA, CGU, WFI, AMI, State, and NZI can support customer trust"},
            {"Capability": "Digital ambition", "Fit score": 4, "Why it supports the pilot": "Creator risks are digital-first and can be served through app, hotline, and partner workflows"},
            {"Capability": "New growth segment", "Fit score": 4, "Why it supports the pilot": "Creators are a growing customer group with personal and business risk overlap"},
        ]
    )

    chart_col, table_col = st.columns([1, 1.25])
    with chart_col:
        fig = px.bar(
            fit_scores,
            x="Fit score",
            y="Capability",
            orientation="h",
            title="Capability Fit for Creator Cyber Insurance",
            labels={"Fit score": "Fit score (1-5)", "Capability": ""},
            color="Fit score",
            color_continuous_scale=["#0e7490", "#67e8f9"],
        )
        fig.update_layout(height=360, margin=dict(l=10, r=10, t=55, b=10), coloraxis_showscale=False)
        fig.update_xaxes(range=[0, 5])
        apply_dark_chart_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    with table_col:
        capability_cards = [
            {
                "label": "Capability",
                "title": row["Capability"],
                "body": row["Why it supports the pilot"],
                "proof": f"Fit score: {row['Fit score']} / 5",
            }
            for _, row in fit_scores.iterrows()
        ]
        render_card_grid(capability_cards[:4])

    recommendation_cols = st.columns([1, 1])
    with recommendation_cols[0]:
        st.markdown(
            """
            <div class="insight">
            <strong>Pitch recommendation:</strong> run a small pilot for Australian content creators
            that bundles cyber cover with practical incident response.
            </div>
            """,
            unsafe_allow_html=True,
        )
    with recommendation_cols[1]:
        st.markdown(
            """
            <div class="insight">
            <strong>Why IAG:</strong> the opportunity needs underwriting discipline,
            claims operations, trusted brands, and partner-led recovery support.
            </div>
            """,
            unsafe_allow_html=True,
        )

    add_source_note(
        'Evidence: <a href="https://www.iag.com.au/content/dam/corporate-iag/iag-aus/au/en/documents/report-and-results/fy26/iag-1h26-presentation-slides.pdf" target="_blank">IAG 1H26 Presentation Slides</a> '
        '| <a href="https://www.iag.com.au/about-us" target="_blank">IAG company profile</a> '
        '| <a href="https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2024-2025?ref=search" target="_blank">ASD / ACSC Annual Cyber Threat Report 2024-25</a>'
    )
