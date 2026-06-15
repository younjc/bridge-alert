# ⚠️ Bridge Safety Alert

A Streamlit civic advocacy app for raising public awareness about the deteriorating Wheeling & Lake Erie railroad bridge in Pittsburgh, PA. The app makes it easy for community members to contact regulators, sign a petition, and share the issue with others.

## What It Does

The app is a single-page action hub with four sections:

**Evidence** — Displays photos and an expandable explanation of the structural hazard: crumbling concrete, exposed rebar, and daily freight traffic carrying hazardous materials.

**Take Action** — One-click buttons that open pre-written emails addressed to PennDOT (district11@pa.gov), the Federal Railroad Administration (frawebsite@dot.gov), and local media, using `mailto:` deep links.

**Petition** — A sign-up form collecting name, email, ZIP code, and an optional comment. There is currently a placeholder for Google Sheets integration where signatures would be stored.

**Share** — SMS and WhatsApp deep links pre-populated with a suggested message, plus a copyable URL, to make peer-to-peer sharing as frictionless as possible.

## Getting Started

### Prerequisites

- Python 3.8+
- No API keys required

### Installation

```bash
git clone https://github.com/younjc/bridge-alert.git
cd bridge-alert
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`.

## Customization

If you want to adapt this template for a different bridge, location, or infrastructure issue, the key things to change are all at the top of `app.py`:

- **`SITE_URL`** — Update to your deployed URL (e.g. your Streamlit Cloud URL) so share links point to the right place.
- **`SHARE_TEXT`** — The pre-written message used for SMS and WhatsApp sharing.
- **`TEMPLATES`** — The `to`, `subject`, and `body` for each email button (PennDOT, FRA, media).
- The **evidence photos** — Replace the placeholder `st.info()` blocks with `st.image()` calls pointing to your actual photos.
- The **timeline** — Update the `timeline_data` list in the Timeline section.

### Connecting the Petition to Google Sheets

The petition form currently shows a success message but does not persist data anywhere. To wire it up, replace the `st.success(...)` block after `if submitted:` with a write to Google Sheets using the `gspread` library and a service account. The `streamlit-gsheets-connection` package is another option for Streamlit Cloud deployments.

## Deploying

This app deploys cleanly to [Streamlit Community Cloud](https://streamlit.io/cloud) with no configuration beyond the `requirements.txt`. After deploying, update `SITE_URL` in `app.py` to your live URL so the share buttons work correctly.

## Tech Stack

- [Streamlit](https://streamlit.io/) — UI framework
- [pandas](https://pandas.pydata.org/) — Timeline data display
- Python stdlib (`urllib.parse`) — URL encoding for `mailto:`, SMS, and WhatsApp deep links
