from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/creator_cyber_insurance_data.csv")
REQUIRED_COLUMNS = [
    "year",
    "tiktok_users_au_millions",
    "estimated_creators_au_millions",
    "creator_market_value_aud_millions",
    "cybercrime_reports",
    "avg_individual_loss_aud",
    "avg_business_loss_aud",
    "risk_type",
    "estimated_creator_loss_aud",
    "affected_group",
]


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {', '.join(missing)}")
    if df.empty:
        raise ValueError("Dataset is empty.")
    if df[REQUIRED_COLUMNS].isna().any().any():
        raise ValueError("Dataset contains missing values.")
    if (df["estimated_creator_loss_aud"] < 0).any():
        raise ValueError("Estimated creator loss must be non-negative.")
    print(f"Data check passed: {len(df):,} rows, {df['year'].nunique()} years.")


if __name__ == "__main__":
    main()
