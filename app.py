import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Bridge Safety Alert | Pittsburgh",
    page_icon="⚠️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM STYLING ---
# Minimal CSS to hide Streamlit branding and make it look like a website
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { margin-top: -50px; }
    .hazard-banner {
        background-color: #ff4b4b;
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .big-button {
        display: inline-block;
        width: 100%;
        padding: 0.75rem;
        color: white !important;
        text-align: center;
        border-radius: 0.5rem;
        text-decoration: none;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .btn-penndot { background-color: #1e3a8a; } /* Blue */
    .btn-fra { background-color: #1e40af; } /* Lighter Blue */
    .btn-media { background-color: #047857; } /* Green */
    </style>
""", unsafe_allow_html=True)

# --- EMAIL TEMPLATE LOGIC ---
def create_mailto_link(to_email, subject, body, button_text, button_class):
    # Safe URL encoding for mailto links
    safe_subject = urllib.parse.quote(subject)
    safe_body = urllib.parse.quote(body)
    link = f"mailto:{to_email}?subject={safe_subject}&body={safe_body}"
    
    # Return an HTML button that looks like a native button
    return f'<a href="{link}" target="_blank" class="big-button {button_class}">{button_text}</a>'

# --- CONTENT CONSTANTS ---
SITE_URL = "https://fixpghbridge.streamlit.app" # You will get this URL after deploying

TEMPLATES = {
    "penndot": {
        "to": "district11@pa.gov",
        "subject": "URGENT: Wheeling & Lake Erie Bridge Structural Failure",
        "body": f"I am writing to request an immediate structural inspection of the W&LE railroad bridge in Pittsburgh. Large sections of the pier are crumbling. Photos here: {SITE_URL}"
    },
    "fra": {
        "to": "frawebsite@dot.gov",
        "subject": "Safety Concern: Wheeling & Lake Erie Bridge",
        "body": f"I am reporting a dangerous structural failure on the W&LE bridge in Pittsburgh. Hazardous cargo crosses daily. Please inspect immediately. Evidence: {SITE_URL}"
    },
    "media": {
        "to": "", # User enters this manually usually, or leave blank to open draft
        "subject": "TIP: Deteriorating Train Bridge in Pittsburgh",
        "body": f"Hello, the W&LE bridge is falling apart while hazmat trains cross it. Please investigate. See photos: {SITE_URL}"
    }
}

# --- MAIN APP UI ---

# 1. Hero Section
st.markdown('<div class="hazard-banner">⚠️ URGENT SAFETY ALERT: WHEELING & LAKE ERIE BRIDGE</div>', unsafe_allow_html=True)
st.title("A Preventable Disaster Waiting to Happen")
st.write("**Location:** Pittsburgh, PA | **Hazard:** Structural Failure & Hazardous Cargo")

st.markdown("""
The Wheeling & Lake Erie railroad bridge shows **severe structural deterioration**. 
Large sections of the concrete pier have collapsed, exposing rebar. 
**Freight trains carrying hazardous materials continue to cross this bridge daily.**
""")

st.divider()

# 2. Evidence Section
st.header("📸 The Evidence")
c1, c2 = st.columns(2)
with c1:
    # Placeholder for actual image
    st.info("🖼️ [Place Photo Here]") 
    st.caption("Dec 2024: Missing concrete on main pier")
with c2:
    st.info("🖼️ [Place Photo Here]") 
    st.caption("Jan 2025: Exposed rebar structure")

with st.expander("Why this is critical (Click to expand)", expanded=True):
    st.markdown("""
    * **Visible Failure:** The load-bearing pier is actively crumbling.
    * **Hazmat Risk:** Trains carry natural gas and flammables.
    * **Public Safety:** A collapse would endanger homes and businesses below.
    """)

st.divider()

# 3. Action Center (The "Email" Buttons)
st.header("📢 Take Action Now")
st.write("Click these buttons to open your email app with a pre-written message.")

# We use HTML/Markdown for mailto links because Streamlit native buttons can't open email clients easily
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown(create_mailto_link(
        TEMPLATES["penndot"]["to"], 
        TEMPLATES["penndot"]["subject"], 
        TEMPLATES["penndot"]["body"], 
        "Email PennDOT", 
        "btn-penndot"
    ), unsafe_allow_html=True)

with col_b:
    st.markdown(create_mailto_link(
        TEMPLATES["fra"]["to"], 
        TEMPLATES["fra"]["subject"], 
        TEMPLATES["fra"]["body"], 
        "Email FRA", 
        "btn-fra"
    ), unsafe_allow_html=True)

with col_c:
    st.markdown(create_mailto_link(
        TEMPLATES["media"]["to"], 
        TEMPLATES["media"]["subject"], 
        TEMPLATES["media"]["body"], 
        "Email Media", 
        "btn-media"
    ), unsafe_allow_html=True)

st.divider()

# 4. Petition Form
st.header("✍️ Sign the Petition")
st.write("We demand an independent inspection and public report.")

with st.form("petition_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    zip_code = st.text_input("ZIP Code")
    comment = st.text_area("Comment (Optional)")
    volunteer = st.checkbox("I want to help organize")
    
    submitted = st.form_submit_button("Sign Petition")
    
    if submitted:
        if name and email:
            # --- DATA SAVING LOGIC ---
            # In a real deployed Streamlit app, local files (CSV) get deleted when the app reboots.
            # To actually save this, you would usually send this data to Google Sheets or a database.
            # For this MVP, we will just show a success message.
            
            new_data = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "name": name, 
                "zip": zip_code, 
                "volunteer": "Yes" if volunteer else "No"
            }
            st.success(f"Thank you, {name}! Your support has been recorded.")
            st.balloons()
        else:
            st.error("Please fill in your name and email.")

st.divider()

# 5. Timeline
st.subheader("📅 Timeline of Neglect")
timeline_data = [
    {"Date": "2021-2024", "Event": "Residents report deterioration; no repairs visible."},
    {"Date": "Dec 2024", "Event": "Viral photos show exposed rebar."},
    {"Date": "Jan 2025", "Event": "Community launches safety alert site."},
]
df = pd.DataFrame(timeline_data)
st.table(df)
