import streamlit as st
import requests
from PIL import Image

st.set_page_config(
    page_title="Seek A Nest AI",
    page_icon="🏡",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

# =========================
# CSS
# =========================

st.markdown("""
<style>
.stApp {
    background: #f3efe6 !important;
    color: #1f2933 !important;
    font-family: Inter, Arial, sans-serif;
}

.block-container {
    padding-top: 0.8rem;
    max-width: 1250px;
}

html, body, p, div, span, label {
    color: #1f2933 !important;
}

h1, h2, h3, h4 {
    color: #1f4d3a !important;
}

/* =========================
SIDEBAR NAVIGATION FIX
========================= */

section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e5e7eb !important;
}

section[data-testid="stSidebar"] * {
    color: #1f2933 !important;
}

section[data-testid="stSidebar"] label {
    color: #1f2933 !important;
    font-weight: 700 !important;
}

div[role="radiogroup"] label {
    background: #f8faf5 !important;
    color: #1f2933 !important;
    border: 1px solid #d1d5db !important;
    border-radius: 14px !important;
    padding: 10px 12px !important;
    margin-bottom: 8px !important;
}

div[role="radiogroup"] label:hover {
    background: #e8f1df !important;
    border-color: #1f4d3a !important;
}

div[role="radiogroup"] label:has(input:checked) {
    background: #1f4d3a !important;
    border-color: #1f4d3a !important;
}

div[role="radiogroup"] label:has(input:checked) * {
    color: white !important;
    font-weight: 800 !important;
}

/* =========================
DROPDOWN VISIBILITY FIX
========================= */

.stSelectbox label,
.stNumberInput label,
.stSlider label,
.stTextInput label,
.stTextArea label,
.stFileUploader label {
    color: #111827 !important;
    font-weight: 800 !important;
}

div[data-baseweb="select"] {
    background: #ffffff !important;
    color: #111827 !important;
}

div[data-baseweb="select"] * {
    color: #111827 !important;
    background: transparent !important;
}

ul[role="listbox"] {
    background: #ffffff !important;
}

li[role="option"] {
    background: #ffffff !important;
    color: #111827 !important;
}

li[role="option"] * {
    color: #111827 !important;
}

input,
textarea {
    background: #ffffff !important;
    color: #111827 !important;
}

/* =========================
TOP NAVBAR
========================= */

.navbar {
    background: white;
    padding: 18px 30px;
    border-radius: 0 0 22px 22px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.07);
    margin-bottom: 22px;
}

.logo {
    font-size: 28px;
    font-weight: 900;
    color: #1f4d3a !important;
}

.nav-subtitle {
    color: #5b6470 !important;
    font-weight: 600;
}

/* =========================
HERO
========================= */

.hero {
    background: linear-gradient(rgba(20,45,34,0.76), rgba(20,45,34,0.76)),
    url("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1400");
    background-size: cover;
    background-position: center;
    padding: 95px 55px 120px 55px;
    border-radius: 30px;
    margin-bottom: 40px;
}

.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    color: white !important;
    padding: 8px 16px;
    border-radius: 999px;
    font-weight: 800;
    margin-bottom: 18px;
}

.hero h1 {
    color: #ffffff !important;
    font-size: 58px;
    line-height: 1.05;
    font-weight: 900;
    max-width: 850px;
    text-shadow: 0 3px 12px rgba(0,0,0,0.55);
}

.hero p {
    color: #f8fafc !important;
    font-size: 20px;
    max-width: 720px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.55);
}

.location-hero {
    background: linear-gradient(rgba(31,77,58,0.78), rgba(31,77,58,0.78)),
    url("https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1400");
    background-size: cover;
    background-position: center;
    padding: 65px 45px;
    border-radius: 28px;
}

.location-hero h1,
.location-hero p {
    color: white !important;
    text-shadow: 0 3px 10px rgba(0,0,0,0.65);
}

/* =========================
HOME SEARCH BOX
========================= */

.home-search-box {
    background: white !important;
    padding: 22px;
    border-radius: 22px;
    margin-top: -85px;
    position: relative;
    z-index: 5;
    box-shadow: 0 18px 45px rgba(0,0,0,0.14);
    margin-bottom: 35px;
}

.home-search-box * {
    color: #1f2933 !important;
}

.home-search-box label {
    color: #111827 !important;
    font-weight: 800 !important;
}

/* =========================
SECTIONS
========================= */

.section-title {
    text-align: center;
    font-size: 36px;
    font-weight: 900;
    color: #1f4d3a !important;
    margin-top: 40px;
}

.section-subtitle {
    text-align: center;
    color: #4b5563 !important;
    font-size: 17px;
    margin-bottom: 28px;
}

/* =========================
CARDS
========================= */

.card {
    background: white !important;
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.07);
    margin-bottom: 18px;
    color: #1f2933 !important;
}

.card * {
    color: #1f2933 !important;
}

.card h3 {
    color: #1f4d3a !important;
}

.card p {
    color: #5b6470 !important;
}

.home-stat {
    background: white !important;
    padding: 22px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.07);
}

.home-stat h2 {
    color: #1f4d3a !important;
    font-size: 32px;
    margin-bottom: 4px;
}

.home-stat p {
    color: #5b6470 !important;
}

/* =========================
PROPERTY CARDS
========================= */

.property-card {
    background: white !important;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    margin-bottom: 22px;
    transition: 0.25s ease;
}

.property-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 18px 38px rgba(0,0,0,0.12);
}

.property-card img {
    width: 100%;
    height: 190px;
    object-fit: cover;
}

.property-body {
    padding: 20px;
}

.property-body * {
    color: #1f2933 !important;
}

.property-body p {
    color: #5b6470 !important;
}

.price {
    color: #1f4d3a !important;
    font-size: 24px;
    font-weight: 900;
}

.tag {
    display: inline-block;
    background: #e8f1df !important;
    color: #1f4d3a !important;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-right: 6px;
    margin-bottom: 8px;
}

/* =========================
PANELS / RESULT
========================= */

.panel {
    background: white !important;
    padding: 30px;
    border-radius: 28px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
    margin-top: 20px;
}

.panel * {
    color: #1f2933 !important;
}

.result-box {
    background: #1f4d3a !important;
    padding: 30px;
    border-radius: 24px;
    margin-top: 28px;
}

.result-box,
.result-box p,
.result-box div,
.result-box span,
.result-box h1,
.result-box h2,
.result-box h3,
.result-box h4 {
    color: white !important;
}

/* UPDATED: AI valuation price cards visibility fix */
.result-box .metric-card {
    background: #ffffff !important;
    border: 2px solid #111827 !important;
    border-radius: 18px;
    padding: 22px 16px;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.22);
}

.result-box .metric-card,
.result-box .metric-card *,
.result-box .metric-card div,
.result-box .metric-card span,
.result-box .metric-number,
.result-box .metric-label {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    opacity: 1 !important;
    text-shadow: none !important;
}

.result-box .metric-number {
    font-size: 30px;
    font-weight: 950;
    line-height: 1.25;
}

.result-box .metric-label {
    font-weight: 900;
    margin-top: 8px;
}

.metric-card {
    background: #ffffff !important;
    border: 2px solid #111827 !important;
    border-radius: 18px;
    padding: 22px 16px;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.12);
}

.metric-card,
.metric-card *,
.metric-number,
.metric-label {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    opacity: 1 !important;
    text-shadow: none !important;
}

.metric-number {
    font-size: 30px;
    font-weight: 950;
    line-height: 1.25;
}

.metric-label {
    color: #000000 !important;
    font-weight: 900;
    margin-top: 8px;
}

.facility-chip {
    background: #f8faf5 !important;
    border: 1px solid #e0ead8;
    padding: 12px;
    border-radius: 16px;
    margin-bottom: 10px;
    color: #1f2933 !important;
}

.facility-chip b {
    color: #1f4d3a !important;
}

/* =========================
BUTTONS
========================= */

.stButton > button {
    width: 100%;
    height: 46px;
    border-radius: 999px;
    border: none;
    background: #d97706;
    color: white !important;
    font-weight: 900;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: #b45309;
    color: white !important;
    transform: translateY(-2px);
}

/* =========================
FOOTER
========================= */

.footer {
    background: #1f4d3a;
    color: white;
    margin-top: 55px;
    padding: 35px;
    border-radius: 28px 28px 0 0;
    text-align: center;
}

.footer h2,
.footer p,
.footer * {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# API HELPERS
# =========================

def api_get_properties(location="All", purpose="All", user_type="All"):
    try:
        response = requests.get(
            f"{API_URL}/properties",
            params={
                "location": location,
                "purpose": purpose,
                "user_type": user_type
            },
            timeout=15
        )

        if response.status_code == 200:
            return response.json().get("properties", [])

    except Exception:
        pass

    return []


def api_recommend(location, budget, bedrooms, purpose, user_type, priority):
    try:
        response = requests.post(
            f"{API_URL}/recommend",
            data={
                "location": location,
                "budget": str(budget),
                "bedrooms": str(bedrooms),
                "purpose": purpose,
                "user_type": user_type,
                "priority": priority
            },
            timeout=20
        )

        if response.status_code == 200:
            return response.json()

    except Exception:
        pass

    return {
        "best_recommendation": None,
        "recommendations": []
    }


# =========================
# FALLBACK DATA
# =========================

@st.cache_data
def fallback_properties():
    return [
        {
            "id": "fallback-1",
            "title": "3 BHK Premium Apartment in Malviya Nagar",
            "location": "Malviya Nagar",
            "purpose": "Buy",
            "price": 8200000,
            "price_text": "₹82,00,000",
            "bhk": 3,
            "sqft": 1800,
            "type": "Apartment",
            "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=700",
            "safety_score": 84,
            "locality_score": 91,
            "appreciation": "8-11%",
            "value_for_money": 86,
            "best_for": "families and working professionals",
            "facilities": {
                "airport": "3 km",
                "railway": "9 km",
                "hospitals": 10,
                "gyms": 18,
                "schools": 14
            },
            "details": "1800 sq.ft • 3 BHK • premium family option"
        },
        {
            "id": "fallback-2",
            "title": "Student PG Room in Jagatpura",
            "location": "Jagatpura",
            "purpose": "Rent",
            "price": 8500,
            "price_text": "₹8,500/month",
            "bhk": 1,
            "sqft": 250,
            "type": "PG",
            "image": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=700",
            "safety_score": 78,
            "locality_score": 88,
            "appreciation": "12-16%",
            "value_for_money": 95,
            "best_for": "students and bachelors",
            "facilities": {
                "airport": "7 km",
                "railway": "13 km",
                "hospitals": 6,
                "gyms": 12,
                "schools": 8
            },
            "details": "250 sq.ft • student PG • near colleges"
        }
    ]


def get_all_properties():
    data = api_get_properties()
    if data:
        return data
    return fallback_properties()


# =========================
# LOCALITY DISPLAY DATA
# =========================

area_data = {
    "Jagatpura": {
        "best_for": "Students, new flats, investment buyers",
        "avg_price": "₹3,800 - ₹5,800/sq.ft.",
        "rent_range": "₹8,000 - ₹25,000/month",
        "growth": "High",
        "summary": "Jagatpura is one of Jaipur’s strongest student rental and affordable investment areas."
    },
    "Malviya Nagar": {
        "best_for": "Families, working professionals, resale buyers",
        "avg_price": "₹5,500 - ₹8,500/sq.ft.",
        "rent_range": "₹18,000 - ₹45,000/month",
        "growth": "Stable",
        "summary": "Malviya Nagar is a mature residential area with strong demand and lifestyle access."
    },
    "Mansarovar": {
        "best_for": "Families and budget buyers",
        "avg_price": "₹4,000 - ₹6,500/sq.ft.",
        "rent_range": "₹12,000 - ₹30,000/month",
        "growth": "Medium",
        "summary": "Mansarovar is balanced for affordability, family living and connectivity."
    },
    "Vaishali Nagar": {
        "best_for": "Families, PGs, working professionals",
        "avg_price": "₹5,000 - ₹7,500/sq.ft.",
        "rent_range": "₹8,000 - ₹35,000/month",
        "growth": "Stable",
        "summary": "Vaishali Nagar is popular for rentals, families and established societies."
    },
    "C-Scheme": {
        "best_for": "Luxury buyers and premium investors",
        "avg_price": "₹8,500 - ₹14,000/sq.ft.",
        "rent_range": "₹35,000 - ₹90,000/month",
        "growth": "Premium",
        "summary": "C-Scheme is one of Jaipur’s premium real estate locations."
    },
    "Ajmer Road": {
        "best_for": "Plots and long-term investment",
        "avg_price": "₹2,500 - ₹5,000/sq.ft.",
        "rent_range": "₹10,000 - ₹25,000/month",
        "growth": "High",
        "summary": "Ajmer Road is a growth corridor with plot and investment demand."
    }
}

# =========================
# HELPERS
# =========================

def go_to(page, **kwargs):
    st.session_state["page"] = page
    for key, value in kwargs.items():
        st.session_state[key] = value
    st.rerun()


def info_card(title, value):
    st.markdown(f"""
    <div class="card">
        <h3>{title}</h3>
        <p>{value}</p>
    </div>
    """, unsafe_allow_html=True)


def facility_chip(icon, title, value):
    st.markdown(f"""
    <div class="facility-chip">
        <b>{icon} {title}</b><br>
        {value}
    </div>
    """, unsafe_allow_html=True)


def format_price(price):
    try:
        return f"₹{int(price):,}"
    except Exception:
        return str(price)


def get_facility(prop, key):
    facilities = prop.get("facilities", {})
    return facilities.get(key, "N/A")


def property_grid(items, context):
    if not items:
        st.warning("No properties found.")
        return

    cols = st.columns(3)

    for index, prop in enumerate(items):
        unique_key = f"{context}_{prop.get('id', index)}_{index}"

        with cols[index % 3]:
            st.markdown(f"""
            <div class="property-card">
                <img src="{prop.get('image', '')}">
                <div class="property-body">
                    <span class="tag">{prop.get('purpose', 'Property')}</span>
                    <span class="tag">{prop.get('type', 'Listing')}</span>
                    <h3>{prop.get('title', 'Property')}</h3>
                    <p>{prop.get('location', 'Jaipur')}, Jaipur</p>
                    <div class="price">{prop.get('price_text', format_price(prop.get('price', 0)))}</div>
                    <p>{prop.get('details', '')}</p>
                    <p>🏥 Hospitals: {get_facility(prop, 'hospitals')}</p>
                    <p>✈️ Airport: {get_facility(prop, 'airport')}</p>
                    <p>🏋️ Gyms: {get_facility(prop, 'gyms')}</p>
                    <p><b>Value Score:</b> {prop.get('value_for_money', 'N/A')}/100</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("View Full Property Details", key=f"view_{unique_key}"):
                go_to("Property Details", selected_property=prop)

            if st.button(f"Explore {prop.get('location', 'Jaipur')}", key=f"area_{unique_key}"):
                go_to("Location Page", selected_location=prop.get("location", "Jagatpura"))


# =========================
# TOP NAV
# =========================

st.markdown("""
<div class="navbar">
    <div class="logo">🏡 Seek A Nest</div>
    <div class="nav-subtitle">Jaipur Homes • Student Rentals • AI Valuation • Owner Listings • Admin Review</div>
</div>
""", unsafe_allow_html=True)

pages = [
    "Home",
    "Buy Properties",
    "Rent / PG",
    "Best Fit Calculator",
    "Compare Properties",
    "Sell / Rent Your Property",
    "Owner Chat Submission",
    "Admin Panel",
    "AI Valuation"
]

if "page" not in st.session_state:
    st.session_state["page"] = "Home"

current_sidebar_index = pages.index(st.session_state["page"]) if st.session_state["page"] in pages else 0

selected_sidebar_page = st.sidebar.radio("Navigate", pages, index=current_sidebar_index)

if selected_sidebar_page != st.session_state["page"] and st.session_state["page"] in pages:
    st.session_state["page"] = selected_sidebar_page

active_page = st.session_state["page"]

all_properties = get_all_properties()

# =========================
# HOME
# =========================

if active_page == "Home":
    st.markdown("""
    <div class="hero">
        <div class="hero-badge">AI-Powered Jaipur Real Estate Platform</div>
        <h1>Find your perfect property with intelligence, not guesswork.</h1>
        <p>
            Buy, rent, compare and value Jaipur properties using AI-powered locality insights,
            safety score, nearby facilities and future appreciation prediction.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="home-search-box">', unsafe_allow_html=True)

    s1, s2, s3, s4, s5 = st.columns([1.2, 1, 1, 1, 1])

    with s1:
        home_location = st.selectbox(
            "Location",
            [
                "Any",
                "Jagatpura",
                "Malviya Nagar",
                "Mansarovar",
                "Vaishali Nagar",
                "C-Scheme",
                "Ajmer Road"
            ],
            key="home_location"
        )

    with s2:
        home_need = st.selectbox(
            "Need",
            ["Buy", "Rent"],
            key="home_need"
        )

    with s3:
        home_property_type = st.selectbox(
            "Property Type",
            [
                "Any",
                "Flat",
                "Apartment",
                "House/Villa",
                "Plot",
                "PG",
                "Student Rental"
            ],
            key="home_property_type"
        )

    with s4:
        home_user = st.selectbox(
            "You are",
            ["Student", "Family", "Investor", "Working Professional"],
            key="home_user"
        )

    with s5:
        st.write("")
        st.write("")
        if st.button("Search", key="home_search_button"):
            if home_location != "Any":
                go_to("Location Page", selected_location=home_location)
            elif home_need == "Buy":
                go_to("Buy Properties")
            else:
                go_to("Rent / PG")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Explore by Jaipur Area</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Open area-wise property options, rentals, facilities and growth insights.</div>', unsafe_allow_html=True)

    a1, a2, a3 = st.columns(3)
    a4, a5, a6 = st.columns(3)

    with a1:
        info_card("📍 Jagatpura", "Students, colleges, rental demand, affordable flats.")
        if st.button("Open Jagatpura", key="area_jagatpura"):
            go_to("Location Page", selected_location="Jagatpura")

    with a2:
        info_card("📍 Malviya Nagar", "Premium family homes, malls, professionals.")
        if st.button("Open Malviya Nagar", key="area_malviya"):
            go_to("Location Page", selected_location="Malviya Nagar")

    with a3:
        info_card("📍 Mansarovar", "Family-friendly, budget homes, connectivity.")
        if st.button("Open Mansarovar", key="area_mansarovar"):
            go_to("Location Page", selected_location="Mansarovar")

    with a4:
        info_card("📍 Vaishali Nagar", "Rentals, families, working professionals.")
        if st.button("Open Vaishali Nagar", key="area_vaishali"):
            go_to("Location Page", selected_location="Vaishali Nagar")

    with a5:
        info_card("📍 C-Scheme", "Luxury homes, premium buyers, high lifestyle.")
        if st.button("Open C-Scheme", key="area_cscheme"):
            go_to("Location Page", selected_location="C-Scheme")

    with a6:
        info_card("📍 Ajmer Road", "Plots, long-term investment, future growth.")
        if st.button("Open Ajmer Road", key="area_ajmer"):
            go_to("Location Page", selected_location="Ajmer Road")

    st.markdown('<div class="section-title">Start Your Property Journey</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Buy, rent, compare, value, list or review properties.</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        info_card("🏠 Buy Properties", "Explore 5+ purchase options per area.")
        if st.button("Open Buy Page", key="home_buy"):
            go_to("Buy Properties")

    with c2:
        info_card("🎓 Rent / PG", "Explore 4+ rent options per area.")
        if st.button("Open Rent Page", key="home_rent"):
            go_to("Rent / PG")

    with c3:
        info_card("🎯 Best Fit Finder", "Compare by student, family, investor and budget.")
        if st.button("Open Best Fit", key="home_fit"):
            go_to("Best Fit Calculator")

    with c4:
        info_card("📤 List Property", "Owner can submit property for selling or renting.")
        if st.button("List Property", key="home_sell"):
            go_to("Sell / Rent Your Property")

    st.markdown('<div class="section-title">Featured Listings</div>', unsafe_allow_html=True)

    property_grid(all_properties[:6], context="home_featured")

# =========================
# BUY
# =========================

elif active_page == "Buy Properties":
    st.markdown('<div class="section-title">Buy Properties in Jaipur</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">At least 5 purchase options per area from backend/dataset.</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        location_filter = st.selectbox(
            "Location",
            ["All", "Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"],
            key="buy_location"
        )

    with col2:
        user_type = st.selectbox(
            "User Type",
            ["All", "Student", "Family", "Investor", "Working Professional"],
            key="buy_user"
        )

    with col3:
        budget_filter = st.selectbox(
            "Budget",
            ["All", "Below ₹50L", "₹50L - ₹1Cr", "₹1Cr - ₹2Cr", "Above ₹2Cr"],
            key="buy_budget"
        )

    with col4:
        search = st.text_input("Search", key="buy_search")

    filtered = api_get_properties(location=location_filter, purpose="Buy", user_type=user_type)

    if not filtered:
        filtered = [p for p in all_properties if p.get("purpose") == "Buy"]

    if search:
        filtered = [
            p for p in filtered
            if search.lower() in p.get("title", "").lower()
            or search.lower() in p.get("location", "").lower()
            or search.lower() in p.get("type", "").lower()
        ]

    if budget_filter == "Below ₹50L":
        filtered = [p for p in filtered if p.get("price", 0) < 5000000]
    elif budget_filter == "₹50L - ₹1Cr":
        filtered = [p for p in filtered if 5000000 <= p.get("price", 0) <= 10000000]
    elif budget_filter == "₹1Cr - ₹2Cr":
        filtered = [p for p in filtered if 10000000 < p.get("price", 0) <= 20000000]
    elif budget_filter == "Above ₹2Cr":
        filtered = [p for p in filtered if p.get("price", 0) > 20000000]

    property_grid(filtered, context="buy")

# =========================
# RENT
# =========================

elif active_page == "Rent / PG":
    st.markdown('<div class="section-title">Rentals & PGs in Jaipur</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">At least 4 rental options per area from backend/dataset.</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        location_filter = st.selectbox(
            "Location",
            ["All", "Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"],
            key="rent_location"
        )

    with col2:
        user_type = st.selectbox(
            "User Type",
            ["All", "Student", "Family", "Investor", "Working Professional"],
            key="rent_user"
        )

    with col3:
        max_rent = st.slider("Max Monthly Rent", 5000, 100000, 25000, key="rent_budget")

    filtered = api_get_properties(location=location_filter, purpose="Rent", user_type=user_type)

    if not filtered:
        filtered = [p for p in all_properties if p.get("purpose") == "Rent"]

    filtered = [p for p in filtered if p.get("price", 0) <= max_rent]

    property_grid(filtered, context="rent")

# =========================
# LOCATION PAGE
# =========================

elif active_page == "Location Page":
    location = st.session_state.get("selected_location", "Jagatpura")
    info = area_data.get(location, area_data["Jagatpura"])

    st.markdown(f"""
    <div class="location-hero">
        <h1>{location} Property Guide</h1>
        <p>{info['summary']}</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        info_card("Best For", info["best_for"])
    with c2:
        info_card("Avg Price", info["avg_price"])
    with c3:
        info_card("Rent Range", info["rent_range"])
    with c4:
        info_card("Growth", info["growth"])

    st.markdown('<div class="section-title">Buy Options</div>', unsafe_allow_html=True)
    buy_options = api_get_properties(location=location, purpose="Buy")
    property_grid(buy_options[:8], context=f"location_buy_{location}")

    st.markdown('<div class="section-title">Rent Options</div>', unsafe_allow_html=True)
    rent_options = api_get_properties(location=location, purpose="Rent")
    property_grid(rent_options[:6], context=f"location_rent_{location}")

# =========================
# PROPERTY DETAILS
# =========================

elif active_page == "Property Details":
    prop = st.session_state.get("selected_property", all_properties[0])

    left, right = st.columns([1.3, 1])

    with left:
        st.image(prop.get("image", ""), use_container_width=True)

    with right:
        st.markdown(f"## {prop.get('title', 'Property')}")
        st.write(f"### {prop.get('location', 'Jaipur')}, Jaipur")
        st.markdown(f'<div class="price">{prop.get("price_text", format_price(prop.get("price", 0)))}</div>', unsafe_allow_html=True)
        st.write(prop.get("details", ""))
        st.write(f"**Property Type:** {prop.get('type', 'N/A')}")
        st.write(f"**Size:** {prop.get('sqft', 'N/A')} sq.ft")
        st.write(f"**Best For:** {prop.get('best_for', 'N/A')}")

    st.markdown('<div class="section-title">Property Intelligence</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        info_card("Safety Score", f"{prop.get('safety_score', 'N/A')}/100")
    with c2:
        info_card("Future Appreciation", prop.get("appreciation", "N/A"))
    with c3:
        info_card("Value For Money", f"{prop.get('value_for_money', 'N/A')}/100")
    with c4:
        info_card("Locality Score", f"{prop.get('locality_score', 'N/A')}/100")

    st.markdown('<div class="section-title">Nearby Facilities</div>', unsafe_allow_html=True)

    f1, f2, f3, f4, f5 = st.columns(5)

    with f1:
        facility_chip("✈️", "Airport", get_facility(prop, "airport"))
    with f2:
        facility_chip("🚆", "Railway", get_facility(prop, "railway"))
    with f3:
        facility_chip("🏥", "Hospitals", get_facility(prop, "hospitals"))
    with f4:
        facility_chip("🏋️", "Gyms", get_facility(prop, "gyms"))
    with f5:
        facility_chip("🏫", "Schools", get_facility(prop, "schools"))

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.subheader("AI Recommendation According To Your Requirement")

    user_type = st.selectbox(
        "Who are you?",
        ["Student", "Family", "Investor", "Working Professional"],
        key="detail_user_type"
    )

    user_budget = st.number_input(
        "Your Budget",
        min_value=5000,
        value=25000 if prop.get("purpose") == "Rent" else 5000000,
        step=5000,
        key="detail_budget"
    )

    priority = st.selectbox(
        "Your Priority",
        ["Value", "Safety", "Future Growth", "Facilities", "Lifestyle"],
        key="detail_priority"
    )

    if st.button("Check If This Property Is Good For Me", key="detail_recommend"):
        score = 50

        if user_type.lower() in prop.get("best_for", "").lower():
            score += 20

        if prop.get("price", 0) <= user_budget:
            score += 20

        if priority == "Safety":
            score += int(prop.get("safety_score", 70) / 10)
        elif priority == "Future Growth":
            score += 8
        elif priority == "Facilities":
            score += 8
        else:
            score += int(prop.get("value_for_money", 70) / 10)

        score = min(score, 100)

        st.success(f"Compatibility Score: {score}/100")

        if score >= 85:
            st.write("✅ Strongly recommended for your requirement.")
        elif score >= 70:
            st.write("⚠️ Good option, but compare with alternatives.")
        else:
            st.write("❌ Not the best fit for your requirement.")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# BEST FIT
# =========================

elif active_page == "Best Fit Calculator":
    st.markdown('<div class="section-title">Best Property For You</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">We compare properties according to student, family, investor, budget and priority.</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        user_type = st.selectbox(
            "Who are you?",
            ["Student", "Family", "Investor", "Working Professional"],
            index=["Student", "Family", "Investor", "Working Professional"].index(st.session_state.get("fit_user_pref", "Student")),
            key="fit_user"
        )

        purpose = st.selectbox(
            "What do you need?",
            ["Buy", "Rent"],
            index=["Buy", "Rent"].index(st.session_state.get("fit_purpose_pref", "Buy")),
            key="fit_purpose"
        )

        location = st.selectbox(
            "Preferred Location",
            ["Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"],
            index=["Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"].index(
                st.session_state.get("fit_location_pref", "Jagatpura")
            ),
            key="fit_location"
        )

    with col2:
        if purpose == "Buy":
            budget = st.number_input("Buying Budget", min_value=500000, value=5000000, step=100000, key="fit_buy_budget")
        else:
            budget = st.number_input("Monthly Rent Budget", min_value=5000, value=15000, step=1000, key="fit_rent_budget")

        bedrooms = st.slider("Bedrooms", 0, 5, 2, key="fit_bedrooms")

        priority = st.selectbox(
            "Main Priority",
            ["Value", "Safety", "Facilities", "Future Growth", "Lifestyle"],
            index=["Value", "Safety", "Facilities", "Future Growth", "Lifestyle"].index(
                st.session_state.get("fit_priority_pref", "Value")
            ),
            key="fit_priority"
        )

    if st.button("Compare And Recommend", key="fit_button"):
        data = api_recommend(
            location=location,
            budget=budget,
            bedrooms=bedrooms,
            purpose=purpose,
            user_type=user_type,
            priority=priority
        )

        recommendations = data.get("recommendations", [])
        best = data.get("best_recommendation")

        if not recommendations:
            st.warning("No recommendations found.")
        else:
            st.markdown("## Compared Options")

            property_grid(recommendations, context="fit_recommendations")

            if best:
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.markdown("## Final AI Recommendation")
                st.write(f"Best match for you is **{best['title']}** in **{best['location']}**.")
                st.write(f"Match Score: **{best.get('match_score', 'N/A')}/100**")
                st.write(f"Best for: **{best.get('best_for', 'N/A')}**")
                st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# COMPARE
# =========================

elif active_page == "Compare Properties":
    st.markdown('<div class="section-title">Compare Properties</div>', unsafe_allow_html=True)

    names = [p.get("title", "Property") for p in all_properties]

    if len(names) < 2:
        st.warning("Not enough properties to compare.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            p1_name = st.selectbox("Property 1", names, key="compare_1")

        with col2:
            p2_name = st.selectbox("Property 2", names, index=1, key="compare_2")

        p1 = next(p for p in all_properties if p.get("title") == p1_name)
        p2 = next(p for p in all_properties if p.get("title") == p2_name)

        for col, prop in zip(st.columns(2), [p1, p2]):
            with col:
                st.image(prop.get("image", ""), use_container_width=True)
                st.markdown(f"## {prop.get('title', 'Property')}")
                st.write(f"**Location:** {prop.get('location', 'N/A')}")
                st.write(f"**Price:** {prop.get('price_text', format_price(prop.get('price', 0)))}")
                st.write(f"**Safety:** {prop.get('safety_score', 'N/A')}/100")
                st.write(f"**Appreciation:** {prop.get('appreciation', 'N/A')}")
                st.write(f"**Value For Money:** {prop.get('value_for_money', 'N/A')}/100")
                st.write(f"**Best For:** {prop.get('best_for', 'N/A')}")
                st.write(f"**Hospitals:** {get_facility(prop, 'hospitals')}")
                st.write(f"**Airport:** {get_facility(prop, 'airport')}")
                st.write(f"**Gyms:** {get_facility(prop, 'gyms')}")

# =========================
# SELL / RENT PROPERTY
# =========================

elif active_page == "Sell / Rent Your Property":
    st.markdown('<div class="section-title">Sell or Rent Your Property</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Owner view: submit property for admin review.</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    owner_name = st.text_input("Owner Name", key="owner_name")
    phone = st.text_input("Phone Number", key="owner_phone")

    listing_type = st.selectbox("Listing Type", ["Owner", "Broker", "Builder"], key="listing_type")
    purpose = st.selectbox("Purpose", ["Sell", "Rent"], key="submit_purpose")
    location = st.selectbox("Location", ["Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"], key="submit_location")

    expected_price = st.number_input("Expected Price / Rent", min_value=1000, value=5000000, key="submit_price")
    bedrooms = st.slider("Bedrooms", 0, 6, 2, key="submit_bedrooms")
    sqft = st.number_input("Square Feet", min_value=100, value=1200, key="submit_sqft")

    furnishing = st.selectbox("Furnishing", ["Unfurnished", "Semi-Furnished", "Fully Furnished"], key="submit_furnishing")
    description = st.text_area("Property Description", key="submit_description")

    st.write("### Highlight Nearby Features")
    near_hospital = st.checkbox("Near hospital")
    near_airport = st.checkbox("Near airport")
    near_railway = st.checkbox("Near railway station")
    near_gym = st.checkbox("Near gym")
    near_school = st.checkbox("Near school/college")
    near_market = st.checkbox("Near market")

    image = st.file_uploader("Upload Property Image", type=["jpg", "jpeg", "png"], key="submit_image")

    if image:
        st.image(Image.open(image), use_container_width=True)

    if st.button("Submit Property For Admin Review", key="submit_property_button"):
        try:
            files = {}

            if image:
                files["image"] = (image.name, image.getvalue(), image.type)

            response = requests.post(
                f"{API_URL}/submit-property",
                data={
                    "owner_name": owner_name,
                    "phone": phone,
                    "listing_type": listing_type,
                    "purpose": purpose,
                    "location": location,
                    "expected_price": str(expected_price),
                    "bedrooms": str(bedrooms),
                    "sqft": str(sqft),
                    "furnishing": furnishing,
                    "description": description,
                    "near_hospital": str(near_hospital),
                    "near_airport": str(near_airport),
                    "near_railway": str(near_railway),
                    "near_gym": str(near_gym),
                    "near_school": str(near_school),
                    "near_market": str(near_market),
                },
                files=files,
                timeout=20
            )

            if response.status_code == 200:
                result = response.json()
                st.success("Property submitted successfully.")
                st.write(f"Submission ID: {result.get('submission_id')}")
                st.write(f"Status: {result.get('status')}")
            else:
                st.error("Submission failed.")
                st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# CHAT SUBMISSION
# =========================

elif active_page == "Owner Chat Submission":
    st.markdown('<div class="section-title">Chat-Style Property Submission</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Owner can describe property like a message. Backend extracts purpose and location.</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    owner_name = st.text_input("Owner Name", key="chat_owner_name")
    phone = st.text_input("Phone Number", key="chat_phone")

    message = st.text_area(
        "Describe your property",
        placeholder="Example: I want to rent my 2 BHK flat in Jagatpura near college. It is semi-furnished and has parking.",
        key="chat_message"
    )

    image = st.file_uploader("Upload Property Image", type=["jpg", "jpeg", "png"], key="chat_image")

    if image:
        st.image(Image.open(image), use_container_width=True)

    if st.button("Submit Through Chat", key="chat_submit"):
        try:
            files = {}

            if image:
                files["image"] = (image.name, image.getvalue(), image.type)

            response = requests.post(
                f"{API_URL}/property-chat-submit",
                data={
                    "owner_name": owner_name,
                    "phone": phone,
                    "message": message
                },
                files=files,
                timeout=20
            )

            if response.status_code == 200:
                result = response.json()
                st.success("Chat submission received.")
                st.write(f"Submission ID: {result.get('submission_id')}")
                st.write(f"Detected Purpose: {result.get('detected_purpose')}")
                st.write(f"Detected Location: {result.get('detected_location')}")
                st.write(f"Status: {result.get('status')}")
            else:
                st.error("Chat submission failed.")
                st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# ADMIN PANEL
# =========================

elif active_page == "Admin Panel":
    st.markdown('<div class="section-title">Admin Panel</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Admin view: see owner-submitted properties waiting for review.</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    admin_key = st.text_input("Admin Key", type="password", key="admin_key")

    if st.button("Load Submissions", key="admin_load"):
        try:
            response = requests.get(
                f"{API_URL}/admin/submissions",
                params={"admin_key": admin_key},
                timeout=20
            )

            result = response.json()

            if "error" in result:
                st.error(result["error"])
            else:
                st.success(f"{result.get('count', 0)} submissions found.")

                for item in result.get("submissions", []):
                    st.markdown(f"""
                    <div class="card">
                        <h3>Submission ID: {item.get('id')}</h3>
                        <p><b>Owner:</b> {item.get('owner_name')}</p>
                        <p><b>Phone:</b> {item.get('phone')}</p>
                        <p><b>Location:</b> {item.get('location', item.get('detected_location', 'N/A'))}</p>
                        <p><b>Purpose:</b> {item.get('purpose', item.get('detected_purpose', 'N/A'))}</p>
                        <p><b>Status:</b> {item.get('status')}</p>
                    </div>
                    """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# AI VALUATION
# =========================

elif active_page == "AI Valuation":
    st.markdown('<div class="section-title">AI Property Valuation</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Price prediction + image + recommendations + AI advisor.</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    left, right = st.columns(2)

    with left:
        purpose_label = st.selectbox("Why do you need valuation?", ["Buying", "Selling", "Investment", "Rent Estimation"], key="ai_purpose")
        backend_purpose = "Rent" if purpose_label == "Rent Estimation" else "Buy"

        user_type = st.selectbox("User Type", ["Student", "Family", "Investor", "Working Professional"], key="ai_user_type")
        priority = st.selectbox("Priority", ["Value", "Safety", "Facilities", "Future Growth", "Lifestyle"], key="ai_priority")

        location = st.selectbox("Location", ["Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"], key="ai_location")

        sqft = st.number_input("Square Feet", min_value=500, max_value=10000, value=1500, key="ai_sqft")
        bedrooms = st.slider("Bedrooms", 0, 10, 3, key="ai_bedrooms")
        bathrooms = st.slider("Bathrooms", 1, 10, 2, key="ai_bathrooms")
        balcony = st.slider("Balcony", 0, 5, 1, key="ai_balcony")

    with right:
        age_of_property = st.slider("Age of Property", 0, 30, 5, key="ai_age")
        furnishing = st.selectbox("Furnishing", ["Unfurnished", "Semi-Furnished", "Fully Furnished"], key="ai_furnishing")
        parking = st.slider("Parking Slots", 0, 5, 1, key="ai_parking")
        nearby_facilities = st.slider("Nearby Facilities Score", 1, 10, 7, key="ai_facilities")

        img_file = st.file_uploader("Upload Property Image", type=["jpg", "jpeg", "png"], key="ai_image")

        if img_file:
            image = Image.open(img_file)
            st.image(image, use_container_width=True)

    submit = st.button("Generate AI Valuation Report", key="ai_submit")

    st.markdown('</div>', unsafe_allow_html=True)

    if submit:
        if img_file is None:
            st.warning("Please upload a property image.")
        else:
            data = {
                "location": location,
                "sqft": str(sqft),
                "bedrooms": str(bedrooms),
                "bathrooms": str(bathrooms),
                "balcony": str(balcony),
                "age_of_property": str(age_of_property),
                "furnishing": furnishing,
                "parking": str(parking),
                "nearby_facilities": str(nearby_facilities),
                "purpose": backend_purpose,
                "user_type": user_type,
                "priority": priority
            }

            files = {"file": (img_file.name, img_file.getvalue(), img_file.type)}

            try:
                response = requests.post(f"{API_URL}/predict", data=data, files=files, timeout=25)

                if response.status_code != 200:
                    st.error("Backend error")
                    st.write(response.text)
                else:
                    result = response.json()
                    estimated_price = int(result["estimated_price"])
                    low_price = int(estimated_price * 0.93)
                    high_price = int(estimated_price * 1.08)

                    st.markdown('<div class="result-box">', unsafe_allow_html=True)
                    st.markdown("## Jaipur AI Valuation Report")

                    r1, r2, r3 = st.columns(3)

                    with r1:
                        st.markdown(f'<div class="metric-card"><div class="metric-number">₹{low_price:,}</div><div class="metric-label">Good Deal Price</div></div>', unsafe_allow_html=True)
                    with r2:
                        st.markdown(f'<div class="metric-card"><div class="metric-number">₹{estimated_price:,}</div><div class="metric-label">Fair Market Price</div></div>', unsafe_allow_html=True)
                    with r3:
                        st.markdown(f'<div class="metric-card"><div class="metric-number">₹{high_price:,}</div><div class="metric-label">Premium Asking Price</div></div>', unsafe_allow_html=True)

                    st.markdown('</div>', unsafe_allow_html=True)

                    st.write("## Property Image Recommendation")
                    st.image(result.get("property_image", ""), use_container_width=True)

                    st.write("## Locality Intelligence")

                    l1, l2, l3 = st.columns(3)

                    with l1:
                        st.metric("Locality Score", f"{result['locality_score']}/100")
                    with l2:
                        st.metric("Safety Score", f"{result['crime_score']}/100")
                    with l3:
                        st.metric("Estimated Rent", f"₹{int(result['estimated_monthly_rent']):,}/month")

                    st.write("## Future Appreciation")
                    st.success(result["future_growth_prediction"])

                    st.write("## AI Recommendation")
                    st.write(result["ai_recommendation"])

                    st.write("## Nearby Facilities")

                    facilities = result["nearby_facilities_data"]

                    f1, f2, f3, f4, f5 = st.columns(5)

                    with f1:
                        st.metric("Airport", facilities["airport_distance"])
                    with f2:
                        st.metric("Railway", facilities["railway_distance"])
                    with f3:
                        st.metric("Hospitals", facilities["hospitals"])
                    with f4:
                        st.metric("Gyms", facilities["gyms"])
                    with f5:
                        st.metric("Schools", facilities["schools"])

                    st.write("## Similar Property Recommendations")

                    similar = result.get("similar_properties", [])

                    property_grid(similar, context="valuation_similar")

                    st.write("## AI Property Advisor")

                    advisor_question = st.text_input("Ask AI about this property", key="advisor_question")

                    if advisor_question:
                        advisor_response = requests.post(
                            f"{API_URL}/advisor",
                            data={
                                "question": advisor_question,
                                "location": location,
                                "estimated_price": str(result["estimated_price"])
                            },
                            timeout=20
                        )

                        if advisor_response.status_code == 200:
                            st.success(advisor_response.json()["reply"])
                        else:
                            st.error("Advisor API error")

            except requests.exceptions.ConnectionError:
                st.error("Backend is not running. Start backend using: uvicorn main:app --reload")
            except requests.exceptions.Timeout:
                st.error("Backend took too long to respond.")
            except Exception as e:
                st.error(f"Frontend error: {e}")

# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">
    <h2>Seek A Nest AI</h2>
    <p>Jaipur homes • Student rentals • AI valuation • Owner listings • Admin review • Smart recommendations</p>
</div>
""", unsafe_allow_html=True)
