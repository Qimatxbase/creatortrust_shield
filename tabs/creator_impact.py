import pandas as pd
import plotly.express as px
import streamlit as st

from utils import add_source_note, apply_dark_chart_theme, format_currency


IMPACT_MATRIX = {
    "Account hacking": ["income loss", "sponsorship loss", "reputation damage", "emotional stress"],
    "Scam or phishing": ["income loss", "privacy breach", "emotional stress"],
    "Data breach": ["privacy breach", "family safety risk", "reputation damage"],
    "Doxxing": ["privacy breach", "family safety risk", "emotional stress"],
    "Deepfake scam": ["sponsorship loss", "reputation damage", "emotional stress"],
    "Impersonation": ["sponsorship loss", "reputation damage", "income loss"],
    "Platform downtime": ["income loss", "sponsorship loss"],
}


def render(df):
    st.header("Creator Impact")
    st.markdown(
        '<div class="insight">Account hacking, doxxing, and data leaks can expose private '
        "information. For public figures and pro players, this can lead to harassment or threats "
        "against themselves and their families, especially after controversial events or losing "
        "competitions.</div>",
        unsafe_allow_html=True,
    )

    if df.empty:
        st.warning("No data available.")
        return

    losses = (
        df.groupby("risk_type", as_index=False)
        .agg(estimated_creator_loss_aud=("estimated_creator_loss_aud", "median"))
        .sort_values("estimated_creator_loss_aud", ascending=False)
    )

    fig = px.bar(
        losses,
        x="risk_type",
        y="estimated_creator_loss_aud",
        title="Median Estimated Financial Loss by Risk Type",
        labels={
            "risk_type": "Risk type",
            "estimated_creator_loss_aud": "Median estimated loss (AUD)",
        },
        color="risk_type",
        color_discrete_sequence=["#38bdf8", "#2dd4bf", "#a78bfa", "#f472b6", "#fbbf24", "#fb7185", "#34d399"],
    )
    fig.update_layout(height=430, margin=dict(l=10, r=10, t=55, b=80), showlegend=False)
    fig.update_yaxes(tickprefix="$", separatethousands=True)
    apply_dark_chart_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

    selected_risks = sorted(df["risk_type"].unique())
    matrix_rows = []
    for risk in selected_risks:
        impacts = IMPACT_MATRIX.get(risk, [])
        matrix_rows.append(
            {
                "Risk type": risk,
                "Impact categories": ", ".join(impacts),
                "Typical loss signal": format_currency(
                    losses.loc[losses["risk_type"] == risk, "estimated_creator_loss_aud"].iloc[0],
                    compact=True,
                ),
            }
        )
    st.dataframe(pd.DataFrame(matrix_rows), width="stretch", hide_index=True)

    add_source_note(
        'Evidence: <a href="https://www.esafety.gov.au/key-topics/adult-cyber-abuse" target="_blank">eSafety adult cyber abuse guidance</a> '
        '| <a href="https://www.esafety.gov.au/key-topics/image-based-abuse" target="_blank">eSafety image-based abuse guidance</a> '
        '| <a href="https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2024-2025?ref=search" target="_blank">ASD / ACSC Annual Cyber Threat Report 2024-25</a>'
    )
