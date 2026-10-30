# IAG Creator Cyber Insurance Pitch Dashboard

This Streamlit dashboard is a hackathon pitch exploring why IAG should consider a cyber insurance product for Australian content creators, influencers, TikTok creators, streamers, esports players, and public figures.

## Pitch Question

Why should IAG invest in cyber insurance for content creators and public figures in Australia?

The dashboard argues that digital platforms are growing, more Australians are earning income online, and creator income increasingly depends on digital accounts, reputation, sponsorships, and audience trust. Cyber incidents such as account hacking, scams, data breaches, doxxing, impersonation, deepfakes, and platform downtime can create financial, reputational, emotional, and personal safety harm.

## Data Disclaimer

`data/creator_cyber_insurance_data.csv` is demo / synthetic data for hackathon visualisation. It uses public-source inspired values and directional assumptions, but the row-level values are not official statistics and should not be used for investment, underwriting, pricing, or product launch decisions.

## Public Source Notes

- DataReportal Digital 2025: Australia: Australian internet, social media, YouTube, Instagram, and TikTok reach data.
  https://datareportal.com/reports/digital-2025-australia
- eSafety Guide: Australian online platform safety context.
  https://www.esafety.gov.au/key-topics/esafety-guide
- ATO business income guidance: Australian income declaration context for digital income earners and businesses.
  https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/business-income-and-deductions/income-you-must-declare
- ASD / ACSC Annual Cyber Threat Report 2024-25: cybercrime reports, average reported losses, identity fraud, scams, credential theft, and data breach themes.
  https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2024-2025?ref=search
- IAG 1H26 Presentation Slides: IAG scale, insurance growth, financial strength, and strategic fit.
  https://www.iag.com.au/content/dam/corporate-iag/iag-aus/au/en/documents/report-and-results/fy26/iag-1h26-presentation-slides.pdf
- Market sizing in the CSV remains synthetic and should be replaced with verified official data before any real product or investment decision.
- The dashboard includes filters for year range and creator group.

## Dashboard Structure

- `app.py` sets page configuration, dashboard styling, year / creator group filters, and tab routing.
- `utils.py` contains shared helpers: `load_data()`, `filter_data()`, `kpi_card()`, `add_source_note()`, and `format_currency()`.
- `data_check.py` validates the CSV schema and basic data quality.
- `tabs/market_opportunity.py` shows platform and creator market growth.
- `tabs/cyber_risk.py` shows the Australian cyber risk landscape.
- `tabs/creator_impact.py` maps cyber events to financial and non-financial creator harms.
- `presentation/pitch_deck_plan.md` provides a 3 minute pitch structure, speaker script, and Q&A prep aligned to the IAG Realise, Explore, and Decide journey stages.
- `presentation/creatortrust_pitch_script.md` provides the refined CreatorTrust Shield pitch script.
- `presentation/creatortrust_pitch_slides.html` provides a standalone slide deck that can be opened in a browser or printed to PDF.
- `docs/history/presentation/creatortrust_pitch_classic.pptx` provides an editable PowerPoint deck generated from the refined pitch.
- `docs/history/presentation/generate_pitch_classic.py` regenerates the PowerPoint deck.
- `docs/history/presentation/creatortrust_pitch_designer.pptx` provides a more polished designer-style PowerPoint deck.
- `docs/history/presentation/generate_pitch_designer.py` regenerates the designer-style deck.
- `presentation/creatortrust_pitch_deck.pptx` is the recommended senior-design pitch deck.
- `presentation/generate_pitch_deck.py` regenerates the senior-design deck.
- `presentation/google_slides_prompts.md` provides page-by-page prompts for recreating the deck in Google Slides or AI slide tools.

## How To Run

Create and activate a local virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies inside the active virtual environment:

```bash
pip install -r requirements.txt
```

Validate the dataset:

```bash
python data_check.py
```

Start the dashboard:

```bash
streamlit run app.py
```

If you open a new terminal later, activate the virtual environment again before running the app:

```bash
source .venv/bin/activate
streamlit run app.py
```

## Recommended Pitch Conclusion

IAG should invest in a pilot cyber insurance product for Australian creators and public figures. The pilot should combine cyber incident response with insurance coverage for digital income disruption, account recovery, data breach support, doxxing response, reputation support, legal support, and scam or impersonation response.
