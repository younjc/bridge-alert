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
    
    /* Button Styles */
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
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
        transition: all 0.3s cubic-bezier(.25,.8,.25,1);
    }
    .big-button:hover {
        box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
        opacity: 0.9;
    }

    /* Color Classes */
    .btn-penndot { background-color: #1e3a8a; }
    .btn-fra { background-color: #1e40af; }
    .btn-media { background-color: #047857; }
    .btn-sms { background-color: #2563eb; } /* Blue for SMS */
    .btn-wa { background-color: #25D366; }  /* Brand Green for WhatsApp */
    
    /* Share Box Styling */
    .share-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
    }
    .suggested-msg {
        background-color: white;
        border-left: 4px solid #cbd5e1;
        padding: 10px;
        margin: 10px 0;
        text-align: left;
        font-style: italic;
        color: #475569;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---
def create_html_button(link, text, style_class):
    return f'<a href="{link}" target="_blank" class="big-button {style_class}">{text}</a>'

# --- CONTENT CONSTANTS ---
# NOTE: Update this URL after you deploy (e.g. https://bridge-alert.streamlit.app)
SITE_URL = "https://fixpghbridge.streamlit.app" 

SHARE_TEXT = f"Hey, this train bridge in our area looks really unsafe and trains are still using it. We’re trying to push the authorities to inspect and fix it. Can you take a look? {SITE_URL}"

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
        "to": "",
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

# 3. Action Center
st.header("📢 Take Action Now")
st.write("Click these buttons to open your email app with a pre-written message.")

# Email Button Generators
def get_mailto(key, label, css_class):
    t = TEMPLATES[key]
    safe_subject = urllib.parse.quote(t["subject"])
    safe_body = urllib.parse.quote(t["body"])
    link = f"mailto:{t['to']}?subject={safe_subject}&body={safe_body}"
    return create_html_button(link, label, css_class)

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown(get_mailto("penndot", "Email PennDOT", "btn-penndot"), unsafe_allow_html=True)
with col_b:
    st.markdown(get_mailto("fra", "Email FRA", "btn-fra"), unsafe_allow_html=True)
with col_c:
    st.markdown(get_mailto("media", "Email Media", "btn-media"), unsafe_allow_html=True)

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
            # Here you would typically connect to Google Sheets
            st.success(f"Thank you, {name}! Your support has been recorded.")
            st.balloons()
        else:
            st.error("Please fill in your name and email.")

# --- NEW SHARE SECTION ---
st.markdown("<br>", unsafe_allow_html=True) # Spacer

st.markdown('<div class="share-box">', unsafe_allow_html=True)
st.markdown("### 🤝 Share this with friends")
st.markdown("""
<p style='color: #475569; margin-bottom: 15px;'>
People are more likely to take action when someone they know asks them. 
If this matters to you, please share this with <strong>1–3 friends, neighbors, or family members</strong>.
</p>
""", unsafe_allow_html=True)

# Suggested Message Box
st.markdown("<div style='text-align: left; font-weight: bold; font-size: 0.8rem; color: #94a3b8; text-transform: uppercase;'>Suggested message:</div>", unsafe_allow_html=True)
st.markdown(f'<div class="suggested-msg">{SHARE_TEXT}</div>', unsafe_allow_html=True)

# Generate Deep Links
encoded_share_text = urllib.parse.quote(SHARE_TEXT)
sms_link = f"sms:?&body={encoded_share_text}"
wa_link = f"https://wa.me/?text={encoded_share_text}"

col_s1, col_s2 = st.columns(2)

with col_s1:
    # SMS Button
    st.markdown(create_html_button(sms_link, "💬 Invite via Text", "btn-sms"), unsafe_allow_html=True)

with col_s2:
    # WhatsApp Button
    st.markdown(create_html_button(wa_link, "🟢 Invite via WhatsApp", "btn-wa"), unsafe_allow_html=True)

# Copy Link Section (Streamlit Native)
st.markdown("---")
st.write("**Or copy the link manually:**")
st.code(SITE_URL, language="text")
st.markdown('</div>', unsafe_allow_html=True) # End share-box
# -------------------------

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
