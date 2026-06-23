from pathlib import Path
from typing import Optional, Union

import pandas as pd
import streamlit as st


DATA_PATH = Path("data/creator_cyber_insurance_data.csv")


@st.cache_data
def load_data(path: Union[str, Path] = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df.sort_values(["year", "risk_type", "affected_group"]).reset_index(drop=True)


def filter_data(
    df: pd.DataFrame,
    year_range: tuple[int, int],
    affected_groups: list[str],
    risk_types: list[str],
) -> pd.DataFrame:
    filtered = df[df["year"].between(year_range[0], year_range[1])]
    if affected_groups:
        filtered = filtered[filtered["affected_group"].isin(affected_groups)]
    if risk_types:
        filtered = filtered[filtered["risk_type"].isin(risk_types)]
    return filtered


def kpi_card(label: str, value: str, help_text: Optional[str] = None) -> None:
    help_attr = f' title="{help_text}"' if help_text else ""
    st.markdown(
        f"""
        <div class="kpi-card"{help_attr}>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def add_source_note(note: str) -> None:
    st.markdown(f'<div class="source-note">{note}</div>', unsafe_allow_html=True)


def format_currency(value: float, compact: bool = False) -> str:
    if compact:
        if abs(value) >= 1_000_000:
            return f"${value / 1_000_000:.1f}m"
        if abs(value) >= 1_000:
            return f"${value / 1_000:.1f}k"
    return f"${value:,.0f}"


def apply_dark_chart_theme(fig):
    fig.update_layout(
        paper_bgcolor="#070b14",
        plot_bgcolor="#0f172a",
        font_color="#dbeafe",
        title_font_color="#e5edf7",
        legend_font_color="#dbeafe",
        xaxis=dict(
            gridcolor="#243247",
            linecolor="#334155",
            tickfont=dict(color="#cbd5e1"),
            title_font=dict(color="#cbd5e1"),
        ),
        yaxis=dict(
            gridcolor="#243247",
            linecolor="#334155",
            tickfont=dict(color="#cbd5e1"),
            title_font=dict(color="#cbd5e1"),
        ),
    )
    return fig


def latest_year_frame(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    return df[df["year"] == int(df["year"].max())]


def unique_year_metrics(df: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "year",
        "tiktok_users_au_millions",
        "estimated_creators_au_millions",
        "creator_market_value_aud_millions",
        "cybercrime_reports",
        "avg_individual_loss_aud",
        "avg_business_loss_aud",
    ]
    return df[cols].drop_duplicates("year").sort_values("year")
