import plotly.express as px
import streamlit as st

from utils import add_source_note, apply_dark_chart_theme, kpi_card, latest_year_frame, unique_year_metrics


def render(df):
    st.header("Market Opportunity")
    st.markdown(
        '<div class="insight">More Australians are building income streams through TikTok, '
        "streaming, sponsorships, and digital content. This creates a growing group whose "
        "income depends on digital assets.</div>",
        unsafe_allow_html=True,
    )

    if df.empty:
        st.warning("No data available.")
        return

    yearly = unique_year_metrics(df)
    latest = latest_year_frame(df).iloc[0]

    c1, c2, c3 = st.columns(3)
    with c1:
        kpi_card("Current TikTok users", f'{latest["tiktok_users_au_millions"]:.1f}m')
    with c2:
        kpi_card("Estimated creators", f'{latest["estimated_creators_au_millions"]:.2f}m')
    with c3:
        kpi_card("Creator market value", f'${latest["creator_market_value_aud_millions"]:,.0f}m')

    chart_col_1, chart_col_2 = st.columns(2)
    with chart_col_1:
        fig = px.line(
            yearly,
            x="year",
            y="tiktok_users_au_millions",
            markers=True,
            title="TikTok Users in Australia",
            labels={"year": "Year", "tiktok_users_au_millions": "Users (millions)"},
        )
        fig.update_traces(line_color="#2dd4bf", marker_size=8)
        fig.update_layout(height=390, margin=dict(l=10, r=10, t=55, b=10))
        apply_dark_chart_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    with chart_col_2:
        fig = px.bar(
            yearly,
            x="year",
            y="estimated_creators_au_millions",
            title="Estimated Australian Creators",
            labels={"year": "Year", "estimated_creators_au_millions": "Creators (millions)"},
            color_discrete_sequence=["#38bdf8"],
        )
        fig.update_layout(height=390, margin=dict(l=10, r=10, t=55, b=10))
        apply_dark_chart_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    add_source_note(
        'Evidence: <a href="https://datareportal.com/reports/digital-2025-australia" target="_blank">DataReportal Digital 2025: Australia</a> '
        '| <a href="https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/business-income-and-deductions/income-you-must-declare" target="_blank">ATO business income guidance</a> '
        '| <a href="https://www.esafety.gov.au/key-topics/esafety-guide" target="_blank">eSafety guide to online platforms</a>'
    )
