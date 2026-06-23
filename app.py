import streamlit as st

from tabs import cyber_risk, creator_impact, market_opportunity
from utils import filter_data, load_data


st.set_page_config(
    page_title="IAG Creator Cyber Insurance Pitch",
    page_icon="🛡️",
    layout="wide",
)

st.markdown(
    """
    <style>
        :root {
            --ink: #e5edf7;
            --muted: #94a3b8;
            --line: #243247;
            --panel: #111827;
            --panel-2: #0f172a;
            --accent: #38bdf8;
            --accent-soft: #0b2a42;
            --accent-2: #2dd4bf;
            --wash: #070b14;
        }
        .stApp {
            background: var(--wash);
            color: var(--ink);
        }
        .block-container {
            padding-top: 1.1rem;
            padding-bottom: 2.5rem;
            max-width: 1180px;
        }
        h1, h2, h3 {
            letter-spacing: 0;
            color: var(--ink);
        }
        h1 {
            font-size: clamp(2rem, 4vw, 3.2rem);
            line-height: 1.05;
            margin-bottom: 0.6rem;
        }
        h2 {
            font-size: clamp(1.55rem, 2.6vw, 2.25rem);
            line-height: 1.15;
        }
        .subtitle {
            color: #a8b3c7;
            font-size: 1rem;
            line-height: 1.55;
            max-width: 980px;
            margin-bottom: 1rem;
        }
        .filter-title {
            color: #e2e8f0;
            font-size: 0.82rem;
            font-weight: 750;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            margin-bottom: 0.2rem;
        }
        section[data-testid="stSidebar"] {
            background: #0b1220;
            border-right: 1px solid var(--line);
        }
        section[data-testid="stSidebar"] > div {
            background: #0b1220;
        }
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p {
            color: var(--ink);
        }
        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            color: #cbd5e1;
            line-height: 1.45;
        }
        section[data-testid="stSidebar"] [data-baseweb="select"] > div,
        section[data-testid="stSidebar"] [data-baseweb="tag"] {
            background: #111827;
            border-color: #334155;
            color: #e5edf7;
        }
        section[data-testid="stSidebar"] [data-baseweb="tag"] span {
            color: #e5edf7;
        }
        section[data-testid="stSidebar"] [data-testid="stSlider"] div {
            color: #e5edf7;
        }
        .kpi-card {
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 1rem 1rem 0.9rem;
            min-height: 112px;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.18);
        }
        .kpi-label {
            color: var(--muted);
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            line-height: 1.3;
        }
        .kpi-value {
            color: var(--ink);
            font-size: clamp(1.45rem, 2.5vw, 2.1rem);
            font-weight: 750;
            margin-top: 0.35rem;
            line-height: 1.08;
        }
        .insight {
            background: var(--accent-soft);
            border: 1px solid #164e63;
            border-radius: 8px;
            color: #dff6ff;
            padding: 1rem 1.1rem;
            margin: 0.8rem 0 1rem;
            line-height: 1.5;
        }
        .card-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.9rem;
            margin: 0.4rem 0 1.5rem;
        }
        .pitch-card {
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 1rem;
            min-height: 150px;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.16);
        }
        .pitch-card-label {
            color: var(--accent-2);
            font-size: 0.78rem;
            font-weight: 750;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            margin-bottom: 0.45rem;
        }
        .pitch-card-title {
            color: var(--ink);
            font-size: 1.05rem;
            font-weight: 750;
            line-height: 1.25;
            margin-bottom: 0.55rem;
        }
        .pitch-card-body {
            color: #cbd5e1;
            font-size: 0.93rem;
            line-height: 1.45;
        }
        .pitch-card-proof {
            color: #bae6fd;
            border-top: 1px solid var(--line);
            font-size: 0.88rem;
            font-weight: 650;
            line-height: 1.4;
            margin-top: 0.85rem;
            padding-top: 0.75rem;
        }
        @media (max-width: 900px) {
            .card-grid {
                grid-template-columns: 1fr;
            }
        }
        .source-note {
            border-top: 1px solid var(--line);
            color: var(--muted);
            font-size: 0.85rem;
            line-height: 1.45;
            margin-top: 1.2rem;
            padding-top: 0.8rem;
        }
        .source-note a {
            color: var(--accent);
            font-weight: 650;
            text-decoration: none;
        }
        .source-note a:hover {
            text-decoration: underline;
        }
        div[data-testid="stMetricValue"] {
            font-size: 1.6rem;
            color: var(--ink);
        }
        div[data-testid="stMetricLabel"] {
            color: var(--muted);
        }
        div[data-testid="stDataFrame"] {
            border: 1px solid var(--line);
            border-radius: 8px;
            overflow: hidden;
        }
        div[data-testid="stTabs"] button[data-baseweb="tab"] {
            color: #a8b3c7;
            font-weight: 650;
            padding-left: 0.85rem;
            padding-right: 0.85rem;
        }
        div[data-testid="stTabs"] button[data-baseweb="tab"] p {
            color: #a8b3c7;
            font-size: 1rem;
        }
        div[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] p {
            color: var(--accent);
            font-weight: 750;
        }
        div[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
            background-color: var(--accent);
            height: 3px;
        }
        div[data-testid="stTabs"] [role="tablist"] {
            border-bottom: 1px solid var(--line);
            gap: 0.2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


df = load_data()
group_labels = {
    "TikTok creators": "TikTok creators",
    "Influencers": "Influencers",
    "Public figures": "Public figures",
    "Streamers": "Streamers",
    "Esports players": "Pro gamers / esports players",
    "Small creators": "Small creators",
}

st.title("Why IAG Should Invest in Creator Cyber Insurance")
st.markdown(
    """
    <div class="subtitle">
    A hackathon pitch dashboard for cyber insurance focused on Australian content creators,
    influencers, TikTok creators, streamers, esports players, and public figures.
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown('<div class="filter-title">Filters</div>', unsafe_allow_html=True)
    min_year = int(df["year"].min())
    max_year = int(df["year"].max())
    year_range = st.slider("Year range", min_year, max_year, (min_year, max_year))
    affected_groups = st.multiselect(
        "Creator group",
        sorted(df["affected_group"].unique()),
        default=sorted(df["affected_group"].unique()),
        format_func=lambda value: group_labels.get(value, value),
    )

filtered_df = filter_data(
    df,
    year_range,
    affected_groups,
    sorted(df["risk_type"].unique()),
)

tabs = st.tabs(
    [
        "Market Opportunity",
        "Cyber Risk Landscape",
        "Creator Impact",
    ]
)

with tabs[0]:
    market_opportunity.render(filtered_df)

with tabs[1]:
    cyber_risk.render(filtered_df)

with tabs[2]:
    creator_impact.render(filtered_df)
