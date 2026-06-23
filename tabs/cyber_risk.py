import plotly.express as px
import streamlit as st

from utils import add_source_note, apply_dark_chart_theme, format_currency, kpi_card, latest_year_frame


def render(df):
    st.header("Cyber Risk Landscape")
    st.markdown(
        '<div class="insight">Cybercrime is no longer only a business IT issue. For creators, '
        "their account is their storefront, brand, workplace, and income source.</div>",
        unsafe_allow_html=True,
    )

    if df.empty:
        st.warning("No data available.")
        return

    latest = latest_year_frame(df).iloc[0]
    c1, c2, c3 = st.columns(3)
    with c1:
        kpi_card("ACSC cybercrime reports", f'{latest["cybercrime_reports"]:,.0f}')
    with c2:
        kpi_card("Avg individual loss", format_currency(latest["avg_individual_loss_aud"]))
    with c3:
        kpi_card("Avg business loss", format_currency(latest["avg_business_loss_aud"]))

    risk_summary = (
        df.groupby("risk_type", as_index=False)
        .agg(estimated_creator_loss_aud=("estimated_creator_loss_aud", "mean"))
        .sort_values("estimated_creator_loss_aud", ascending=True)
    )

    fig = px.bar(
        risk_summary,
        x="estimated_creator_loss_aud",
        y="risk_type",
        orientation="h",
        title="Estimated Creator Loss by Cyber Risk",
        labels={
            "estimated_creator_loss_aud": "Average estimated loss (AUD)",
            "risk_type": "Risk type",
        },
        color="estimated_creator_loss_aud",
        color_continuous_scale=["#0e7490", "#67e8f9"],
    )
    fig.update_layout(height=470, margin=dict(l=10, r=10, t=55, b=10), coloraxis_showscale=False)
    apply_dark_chart_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

    add_source_note(
        'Evidence: <a href="https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2024-2025?ref=search" target="_blank">ASD / ACSC Annual Cyber Threat Report 2024-25</a> '
        '| <a href="https://www.scamwatch.gov.au/research-and-resources/targeting-scams" target="_blank">ACCC / Scamwatch Targeting Scams reports</a>'
    )
