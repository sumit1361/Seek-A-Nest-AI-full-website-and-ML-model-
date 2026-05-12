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
    background: #f3efe6;
    color: #1f2933;
    font-family: Inter, Arial, sans-serif;
}

.block-container {
    padding-top: 0.8rem;
    max-width: 1250px;
}

html, body, p, div, span, label {
    color: #1f2933;
}

h1, h2, h3, h4 {
    color: #1f4d3a;
}

section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e5e7eb;
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
    border-radius: 14px !important;
    padding: 10px 12px !important;
    margin-bottom: 8px !important;
    border: 1px solid #e5e7eb !important;
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
    color: #1f4d3a;
}

.nav-subtitle {
    color: #5b6470 !important;
    font-weight: 600;
}

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

.home-search-box {
    background: white;
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
    color: #1f2933 !important;
    font-weight: 800 !important;
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

.section-title {
    text-align: center;
    font-size: 36px;
    font-weight: 900;
    color: #1f4d3a;
    margin-top: 40px;
}

.section-subtitle {
    text-align: center;
    color: #5b6470;
    font-size: 17px;
    margin-bottom: 28px;
}

.card {
    background: white;
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.07);
    margin-bottom: 18px;
    color: #1f2933;
}

.card h3 {
    color: #1f4d3a !important;
}

.card p {
    color: #5b6470 !important;
}

.home-stat {
    background: white;
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

.property-card {
    background: white;
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

.property-body p {
    color: #5b6470 !important;
}

.price {
    color: #1f4d3a;
    font-size: 24px;
    font-weight: 900;
}

.tag {
    display: inline-block;
    background: #e8f1df;
    color: #1f4d3a !important;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-right: 6px;
    margin-bottom: 8px;
}

.panel {
    background: white;
    padding: 30px;
    border-radius: 28px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
    margin-top: 20px;
}

.result-box {
    background: #1f4d3a;
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

.metric-card {
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
}

.metric-number {
    font-size: 24px;
    font-weight: 900;
    color: white !important;
}

.metric-label {
    color: #f3f4f6 !important;
}

.facility-chip {
    background: #f8faf5;
    border: 1px solid #e0ead8;
    padding: 12px;
    border-radius: 16px;
    margin-bottom: 10px;
    color: #1f2933 !important;
}

.facility-chip b {
    color: #1f4d3a !important;
}

.stButton > button {
    width: 100%;
    height: 46px;
    border-radius: 999px;
    border: none;
    background: #d97706;
    color: white;
    font-weight: 900;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: #b45309;
    color: white;
    transform: translateY(-2px);
}

.footer {
    background: #1f4d3a;
    color: white;
    margin-top: 55px;
    padding: 35px;
    border-radius: 28px 28px 0 0;
    text-align: center;
}

.footer h2,
.footer p {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# DATA
# =========================

@st.cache_data
def load_properties():
    return [
        {
            "id": 1,
            "title": "3 BHK Premium Apartment",
            "location": "Malviya Nagar",
            "price": 8200000,
            "price_text": "₹82,00,000",
            "type": "Apartment",
            "bhk": "3 BHK",
            "purpose": "Buy",
            "sqft": 1800,
            "rent": 28000,
            "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=700",
            "details": "1800 sq.ft • Semi-Furnished • Parking • Near mall",
            "score": 88,
            "safety_score": 84,
            "appreciation": "8-11%",
            "value_for_money": 86,
            "best_for": "Families, working professionals, premium renters",
            "recommendation": "Good option for families who want lifestyle, safety and an established locality.",
            "facilities": {
                "hospital": "1.8 km",
                "airport": "3 km",
                "railway": "9 km",
                "gym": "500 m",
                "school": "900 m",
                "college": "3.5 km",
                "market": "300 m"
            }
        },
        {
            "id": 2,
            "title": "Modern Student Flat",
            "location": "Jagatpura",
            "price": 12000,
            "price_text": "₹12,000/month",
            "type": "Student Rental",
            "bhk": "1 BHK",
            "purpose": "Rent",
            "sqft": 550,
            "rent": 12000,
            "image": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=700",
            "details": "WiFi • Food Option • Near JECRC/SKIT • Furnished",
            "score": 91,
            "safety_score": 78,
            "appreciation": "12-16%",
            "value_for_money": 92,
            "best_for": "Students, bachelors, rental investors",
            "recommendation": "Best option if you want affordable rent near colleges with strong student demand.",
            "facilities": {
                "hospital": "2.4 km",
                "airport": "7 km",
                "railway": "13 km",
                "gym": "800 m",
                "school": "1.2 km",
                "college": "1.5 km",
                "market": "600 m"
            }
        },
        {
            "id": 3,
            "title": "Luxury Villa",
            "location": "C-Scheme",
            "price": 18500000,
            "price_text": "₹1.85 Cr",
            "type": "Villa",
            "bhk": "4+ BHK",
            "purpose": "Buy",
            "sqft": 3000,
            "rent": 85000,
            "image": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=700",
            "details": "3000 sq.ft • Fully Furnished • Premium Area",
            "score": 94,
            "safety_score": 86,
            "appreciation": "6-9%",
            "value_for_money": 80,
            "best_for": "Luxury buyers, business owners, premium investors",
            "recommendation": "Premium choice for lifestyle and prestige, but value-for-money is lower than emerging areas.",
            "facilities": {
                "hospital": "1 km",
                "airport": "11 km",
                "railway": "4 km",
                "gym": "300 m",
                "school": "1 km",
                "college": "4 km",
                "market": "200 m"
            }
        },
        {
            "id": 4,
            "title": "2 BHK Family Apartment",
            "location": "Mansarovar",
            "price": 5500000,
            "price_text": "₹55,00,000",
            "type": "Apartment",
            "bhk": "2 BHK",
            "purpose": "Buy",
            "sqft": 1250,
            "rent": 19000,
            "image": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=700",
            "details": "1250 sq.ft • Good society • Parking • Market nearby",
            "score": 84,
            "safety_score": 80,
            "appreciation": "7-10%",
            "value_for_money": 88,
            "best_for": "Families and budget buyers",
            "recommendation": "Balanced property for family living with decent safety, connectivity and affordability.",
            "facilities": {
                "hospital": "2 km",
                "airport": "10 km",
                "railway": "8 km",
                "gym": "700 m",
                "school": "800 m",
                "college": "3 km",
                "market": "400 m"
            }
        },
        {
            "id": 5,
            "title": "Affordable PG Room",
            "location": "Vaishali Nagar",
            "price": 8500,
            "price_text": "₹8,500/month",
            "type": "PG",
            "bhk": "Room",
            "purpose": "Rent",
            "sqft": 250,
            "rent": 8500,
            "image": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=700",
            "details": "Single room • WiFi • Security • Food available",
            "score": 86,
            "safety_score": 82,
            "appreciation": "8-12%",
            "value_for_money": 90,
            "best_for": "Students, bachelors, working professionals",
            "recommendation": "Affordable and practical rental choice with good access to markets and facilities.",
            "facilities": {
                "hospital": "1.5 km",
                "airport": "13 km",
                "railway": "7 km",
                "gym": "400 m",
                "school": "1 km",
                "college": "2.5 km",
                "market": "250 m"
            }
        },
        {
            "id": 6,
            "title": "Investment Plot",
            "location": "Ajmer Road",
            "price": 4200000,
            "price_text": "₹42,00,000",
            "type": "Plot",
            "bhk": "Plot",
            "purpose": "Buy",
            "sqft": 1500,
            "rent": 0,
            "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=700",
            "details": "Growth corridor • Good appreciation • Road facing",
            "score": 82,
            "safety_score": 76,
            "appreciation": "11-15%",
            "value_for_money": 89,
            "best_for": "Investors and long-term buyers",
            "recommendation": "Good for long-term appreciation, not ideal if you need immediate rental income.",
            "facilities": {
                "hospital": "4 km",
                "airport": "16 km",
                "railway": "12 km",
                "gym": "2 km",
                "school": "2.5 km",
                "college": "5 km",
                "market": "1.5 km"
            }
        },
        {
            "id": 7,
            "title": "Jagatpura 2 BHK Near Colleges",
            "location": "Jagatpura",
            "price": 3800000,
            "price_text": "₹38,00,000",
            "type": "Apartment",
            "bhk": "2 BHK",
            "purpose": "Buy",
            "sqft": 1050,
            "rent": 16000,
            "image": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=700",
            "details": "Near colleges • High rental demand • Budget-friendly",
            "score": 89,
            "safety_score": 78,
            "appreciation": "12-16%",
            "value_for_money": 94,
            "best_for": "Students, investors, affordable buyers",
            "recommendation": "Strong value-for-money property for investors targeting student rental demand.",
            "facilities": {
                "hospital": "2.7 km",
                "airport": "7 km",
                "railway": "13 km",
                "gym": "700 m",
                "school": "1.5 km",
                "college": "900 m",
                "market": "700 m"
            }
        },
        {
            "id": 8,
            "title": "Jagatpura PG Premium Room",
            "location": "Jagatpura",
            "price": 9500,
            "price_text": "₹9,500/month",
            "type": "PG",
            "bhk": "Room",
            "purpose": "Rent",
            "sqft": 220,
            "rent": 9500,
            "image": "https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?w=700",
            "details": "Food • WiFi • Study table • Near coaching area",
            "score": 93,
            "safety_score": 78,
            "appreciation": "12-16%",
            "value_for_money": 95,
            "best_for": "Students and bachelors",
            "recommendation": "Highly recommended for students needing low rent, facilities and nearby colleges.",
            "facilities": {
                "hospital": "2.2 km",
                "airport": "7 km",
                "railway": "13 km",
                "gym": "600 m",
                "school": "1.4 km",
                "college": "700 m",
                "market": "500 m"
            }
        }
    ]


properties = load_properties()

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


def property_grid(items, context):
    if not items:
        st.warning("No properties found.")
        return

    cols = st.columns(3)

    for index, prop in enumerate(items):
        unique_key = f"{context}_{prop['id']}_{index}"

        with cols[index % 3]:
            st.markdown(f"""
            <div class="property-card">
                <img src="{prop['image']}">
                <div class="property-body">
                    <span class="tag">{prop['purpose']}</span>
                    <span class="tag">{prop['type']}</span>
                    <h3>{prop['title']}</h3>
                    <p>{prop['location']}, Jaipur</p>
                    <div class="price">{prop['price_text']}</div>
                    <p>{prop['details']}</p>
                    <p>🏥 Hospital: {prop['facilities']['hospital']}</p>
                    <p>✈️ Airport: {prop['facilities']['airport']}</p>
                    <p>🏋️ Gym: {prop['facilities']['gym']}</p>
                    <p><b>Value Score:</b> {prop['value_for_money']}/100</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("View Full Property Details", key=f"view_{unique_key}"):
                go_to("Property Details", selected_property_id=prop["id"])

            if st.button(f"Explore {prop['location']}", key=f"area_{unique_key}"):
                go_to("Location Page", selected_location=prop["location"])


def calculate_best_fit(user_budget, purpose, user_type, preferred_location, priority=None):
    scored = []

    for prop in properties:
        score = 0

        if preferred_location == "Any" or prop["location"] == preferred_location:
            score += 25

        if purpose == prop["purpose"]:
            score += 25

        if purpose == "Buy" and prop["price"] <= user_budget:
            score += 20

        if purpose == "Rent" and prop["rent"] <= user_budget:
            score += 20

        if user_type.lower() in prop["best_for"].lower():
            score += 15

        if prop["value_for_money"] >= 85:
            score += 10

        if priority == "Safety":
            score += int(prop["safety_score"] / 20)

        if priority == "Future Growth":
            if "12" in prop["appreciation"] or "15" in prop["appreciation"] or "16" in prop["appreciation"]:
                score += 8

        if priority == "Nearby Facilities":
            score += 7

        scored.append((min(score, 100), prop))

    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:4]


# =========================
# NAVIGATION
# =========================

st.markdown("""
<div class="navbar">
    <div class="logo">🏡 Seek A Nest</div>
    <div class="nav-subtitle">Jaipur Homes • Student Rentals • AI Valuation • Property Intelligence</div>
</div>
""", unsafe_allow_html=True)

pages = [
    "Home",
    "Buy Properties",
    "Rent / PG",
    "Best Fit Calculator",
    "Compare Properties",
    "Sell Property",
    "AI Valuation"
]

if "page" not in st.session_state:
    st.session_state["page"] = "Home"

current_sidebar_index = pages.index(st.session_state["page"]) if st.session_state["page"] in pages else 0

selected_sidebar_page = st.sidebar.radio("Navigate", pages, index=current_sidebar_index)

if selected_sidebar_page != st.session_state["page"] and st.session_state["page"] in pages:
    st.session_state["page"] = selected_sidebar_page

active_page = st.session_state["page"]

# =========================
# PAGES
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
            ["Any", "Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"],
            key="home_location"
        )

    with s2:
        home_need = st.selectbox(
            "Need",
            ["Buy", "Rent"],
            key="home_need"
        )

    with s3:
        home_user = st.selectbox(
            "You are",
            ["Student", "Family", "Investor", "Working Professional"],
            key="home_user"
        )

    with s4:
        home_priority = st.selectbox(
            "Priority",
            ["Budget", "Safety", "Nearby Facilities", "Future Growth", "Lifestyle"],
            key="home_priority"
        )

    with s5:
        st.write("")
        st.write("")
        if st.button("Find Best Options", key="home_search_button"):
            st.session_state["fit_location_pref"] = home_location
            st.session_state["fit_purpose_pref"] = home_need
            st.session_state["fit_user_pref"] = home_user
            st.session_state["fit_priority_pref"] = home_priority
            go_to("Best Fit Calculator")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Start Your Property Journey</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Open a focused page based on what you want to do.</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        info_card("🏠 Buy Properties", "Explore apartments, villas and plots with filters.")
        if st.button("Open Buy Page", key="home_buy"):
            go_to("Buy Properties")

    with c2:
        info_card("🎓 Rent / PG", "Find student flats, PGs and affordable rentals.")
        if st.button("Open Rent Page", key="home_rent"):
            go_to("Rent / PG")

    with c3:
        info_card("🎯 Best Fit Finder", "Answer questions and get ranked suggestions.")
        if st.button("Open Best Fit", key="home_fit"):
            go_to("Best Fit Calculator")

    with c4:
        info_card("🤖 AI Valuation", "Predict price, safety, growth and facilities.")
        if st.button("Open AI Valuator", key="home_ai"):
            go_to("AI Valuation")

    st.markdown('<div class="section-title">Why Seek A Nest?</div>', unsafe_allow_html=True)

    stat1, stat2, stat3 = st.columns(3)

    with stat1:
        st.markdown('<div class="home-stat"><h2>AI Score</h2><p>Compare properties by safety, value and growth.</p></div>', unsafe_allow_html=True)

    with stat2:
        st.markdown('<div class="home-stat"><h2>Jaipur Focus</h2><p>Built around local areas, rentals and student needs.</p></div>', unsafe_allow_html=True)

    with stat3:
        st.markdown('<div class="home-stat"><h2>Smart Fit</h2><p>Get recommendations based on budget and purpose.</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Featured Listings</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Only a few highlights here. Open Buy/Rent pages for full options.</div>', unsafe_allow_html=True)
    property_grid(properties[:3], context="home_featured")


elif active_page == "Buy Properties":
    st.markdown('<div class="section-title">Buy Properties in Jaipur</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Search by location, budget, BHK and property type.</div>', unsafe_allow_html=True)

    search = st.text_input("Search by location, type or keyword", key="buy_search")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        location_filter = st.selectbox(
            "Location",
            ["All", "Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"],
            key="buy_location"
        )

    with col2:
        bhk_filter = st.selectbox(
            "BHK",
            ["All", "1 BHK", "2 BHK", "3 BHK", "4+ BHK", "Plot"],
            key="buy_bhk"
        )

    with col3:
        budget_filter = st.selectbox(
            "Budget",
            ["All", "Below ₹50L", "₹50L - ₹1Cr", "₹1Cr - ₹2Cr", "Above ₹2Cr"],
            key="buy_budget"
        )

    with col4:
        type_filter = st.selectbox(
            "Type",
            ["All", "Apartment", "Villa", "Plot"],
            key="buy_type"
        )

    filtered = [p for p in properties if p["purpose"] == "Buy"]

    if search:
        filtered = [
            p for p in filtered
            if search.lower() in p["title"].lower()
            or search.lower() in p["location"].lower()
            or search.lower() in p["type"].lower()
        ]

    if location_filter != "All":
        filtered = [p for p in filtered if p["location"] == location_filter]

    if bhk_filter != "All":
        filtered = [p for p in filtered if p["bhk"] == bhk_filter]

    if type_filter != "All":
        filtered = [p for p in filtered if p["type"] == type_filter]

    if budget_filter == "Below ₹50L":
        filtered = [p for p in filtered if p["price"] < 5000000]
    elif budget_filter == "₹50L - ₹1Cr":
        filtered = [p for p in filtered if 5000000 <= p["price"] <= 10000000]
    elif budget_filter == "₹1Cr - ₹2Cr":
        filtered = [p for p in filtered if 10000000 < p["price"] <= 20000000]
    elif budget_filter == "Above ₹2Cr":
        filtered = [p for p in filtered if p["price"] > 20000000]

    property_grid(filtered, context="buy")


elif active_page == "Rent / PG":
    st.markdown('<div class="section-title">Rentals & PGs in Jaipur</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Perfect for students, bachelors and working professionals.</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        location_filter = st.selectbox(
            "Location",
            ["All", "Jagatpura", "Vaishali Nagar", "Mansarovar", "Malviya Nagar"],
            key="rent_location"
        )

    with col2:
        max_rent = st.slider(
            "Max Monthly Rent",
            5000,
            50000,
            15000,
            key="rent_budget"
        )

    with col3:
        room_type = st.selectbox(
            "Type",
            ["All", "PG", "Student Rental", "Apartment"],
            key="rent_type"
        )

    filtered = [p for p in properties if p["purpose"] == "Rent" and p["rent"] <= max_rent]

    if location_filter != "All":
        filtered = [p for p in filtered if p["location"] == location_filter]

    if room_type != "All":
        filtered = [p for p in filtered if p["type"] == room_type]

    property_grid(filtered, context="rent")


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

    st.markdown('<div class="section-title">Available Options Here</div>', unsafe_allow_html=True)

    local_properties = [p for p in properties if p["location"] == location]
    property_grid(local_properties, context=f"location_{location}")

    if st.button("Back to Home", key="back_home_location"):
        go_to("Home")


elif active_page == "Property Details":
    prop_id = st.session_state.get("selected_property_id")
    prop = next((p for p in properties if p["id"] == prop_id), properties[0])

    left, right = st.columns([1.3, 1])

    with left:
        st.image(prop["image"], use_container_width=True)

    with right:
        st.markdown(f"## {prop['title']}")
        st.write(f"### {prop['location']}, Jaipur")
        st.markdown(f'<div class="price">{prop["price_text"]}</div>', unsafe_allow_html=True)
        st.write(prop["details"])
        st.write(f"**Property Type:** {prop['type']}")
        st.write(f"**Size:** {prop['sqft']} sq.ft")
        st.write(f"**Best For:** {prop['best_for']}")

    st.markdown('<div class="section-title">Property Intelligence</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        info_card("Safety Score", f"{prop['safety_score']}/100")
    with c2:
        info_card("Future Appreciation", prop["appreciation"])
    with c3:
        info_card("Value For Money", f"{prop['value_for_money']}/100")
    with c4:
        info_card("Fit Score", f"{prop['score']}/100")

    st.markdown('<div class="section-title">Nearby Facilities</div>', unsafe_allow_html=True)

    f1, f2, f3, f4 = st.columns(4)

    with f1:
        facility_chip("🏥", "Hospital", prop["facilities"]["hospital"])
    with f2:
        facility_chip("✈️", "Airport", prop["facilities"]["airport"])
    with f3:
        facility_chip("🚆", "Railway", prop["facilities"]["railway"])
    with f4:
        facility_chip("🏋️", "Gym", prop["facilities"]["gym"])

    f5, f6, f7 = st.columns(3)

    with f5:
        facility_chip("🏫", "School", prop["facilities"]["school"])
    with f6:
        facility_chip("🎓", "College", prop["facilities"]["college"])
    with f7:
        facility_chip("🛒", "Market", prop["facilities"]["market"])

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
        value=15000 if prop["purpose"] == "Rent" else 5000000,
        step=5000,
        key="detail_budget"
    )

    priority = st.selectbox(
        "Your Priority",
        ["Budget", "Safety", "Future Growth", "Nearby Facilities", "Lifestyle"],
        key="detail_priority"
    )

    if st.button("Check If This Property Is Good For Me", key="detail_recommend"):
        match_score = prop["score"]

        if user_type.lower() in prop["best_for"].lower():
            match_score += 8

        if priority == "Safety":
            match_score += int(prop["safety_score"] / 20)

        if priority == "Future Growth":
            match_score += 5

        if priority == "Nearby Facilities":
            match_score += 5

        if prop["purpose"] == "Rent" and prop["rent"] <= user_budget:
            match_score += 10

        if prop["purpose"] == "Buy" and prop["price"] <= user_budget:
            match_score += 10

        match_score = min(match_score, 100)

        st.success(f"Compatibility Score: {match_score}/100")
        st.write(prop["recommendation"])

        if match_score >= 85:
            st.write("✅ Strongly recommended for your requirement.")
        elif match_score >= 70:
            st.write("⚠️ Good option, but compare with alternatives.")
        else:
            st.write("❌ Not the best fit for your requirement.")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Similar Properties</div>', unsafe_allow_html=True)

    similar = [p for p in properties if p["location"] == prop["location"] and p["id"] != prop["id"]]
    property_grid(similar if similar else properties[:3], context=f"similar_{prop_id}")


elif active_page == "Best Fit Calculator":
    st.markdown('<div class="section-title">Best Property For You</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Answer a few questions. We compare options and recommend the best fit.</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        user_type = st.selectbox(
            "Who are you?",
            ["Student", "Family", "Investor", "Working Professional"],
            index=["Student", "Family", "Investor", "Working Professional"].index(
                st.session_state.get("fit_user_pref", "Student")
            ),
            key="fit_user"
        )

        purpose = st.selectbox(
            "What do you need?",
            ["Buy", "Rent"],
            index=["Buy", "Rent"].index(
                st.session_state.get("fit_purpose_pref", "Buy")
            ),
            key="fit_purpose"
        )

        preferred_location = st.selectbox(
            "Preferred Location",
            ["Any", "Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"],
            index=["Any", "Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"].index(
                st.session_state.get("fit_location_pref", "Any")
            ),
            key="fit_location"
        )

    with col2:
        if purpose == "Buy":
            budget = st.number_input(
                "Buying Budget",
                min_value=500000,
                value=5000000,
                step=100000,
                key="fit_buy_budget"
            )
        else:
            budget = st.number_input(
                "Monthly Rent Budget",
                min_value=5000,
                value=15000,
                step=1000,
                key="fit_rent_budget"
            )

        priority = st.selectbox(
            "Main Priority",
            ["Budget", "Safety", "Nearby Facilities", "Future Growth", "Lifestyle"],
            index=["Budget", "Safety", "Nearby Facilities", "Future Growth", "Lifestyle"].index(
                st.session_state.get("fit_priority_pref", "Budget")
            ),
            key="fit_priority"
        )

        near_college = st.checkbox("Need college nearby?")
        need_airport = st.checkbox("Need airport access?")
        need_market = st.checkbox("Need market nearby?")

    if st.button("Compare And Recommend", key="fit_button"):
        matches = calculate_best_fit(
            budget,
            purpose,
            user_type,
            preferred_location,
            priority
        )

        st.markdown("## Compared Options")

        best_score = -1
        best_property = None

        for index, (score, prop) in enumerate(matches):
            final_score = score

            if near_college and prop["facilities"]["college"] in ["700 m", "900 m", "1.5 km"]:
                final_score += 8

            if need_airport and prop["facilities"]["airport"] in ["3 km", "7 km"]:
                final_score += 6

            if need_market and prop["facilities"]["market"] in ["200 m", "250 m", "300 m", "500 m", "600 m"]:
                final_score += 6

            final_score = min(final_score, 100)

            if final_score > best_score:
                best_score = final_score
                best_property = prop

            st.markdown(f"""
            <div class="card">
                <h3>{prop['title']}</h3>
                <p>{prop['location']}, Jaipur</p>
                <div class="price">{prop['price_text']}</div>
                <p>{prop['details']}</p>
                <p><b>Safety:</b> {prop['safety_score']}/100</p>
                <p><b>Future Appreciation:</b> {prop['appreciation']}</p>
                <p><b>Value For Money:</b> {prop['value_for_money']}/100</p>
                <h3>Final Match Score: {final_score}/100</h3>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"View Full Details - {prop['title']}", key=f"fit_view_{prop['id']}_{index}"):
                go_to("Property Details", selected_property_id=prop["id"])

        if best_property:
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown("## Final AI Recommendation")
            st.write(f"Best match for you is **{best_property['title']}** in **{best_property['location']}**.")
            st.write(f"Final Score: **{best_score}/100**")
            st.write(best_property["recommendation"])
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


elif active_page == "Compare Properties":
    st.markdown('<div class="section-title">Compare Properties</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Compare property safety, value, facilities and appreciation side by side.</div>', unsafe_allow_html=True)

    names = [p["title"] for p in properties]

    col1, col2 = st.columns(2)

    with col1:
        p1_name = st.selectbox("Property 1", names, key="compare_1")

    with col2:
        p2_name = st.selectbox("Property 2", names, index=1, key="compare_2")

    p1 = next(p for p in properties if p["title"] == p1_name)
    p2 = next(p for p in properties if p["title"] == p2_name)

    for col, prop in zip(st.columns(2), [p1, p2]):
        with col:
            st.image(prop["image"], use_container_width=True)
            st.markdown(f"## {prop['title']}")
            st.write(f"**Location:** {prop['location']}")
            st.write(f"**Price:** {prop['price_text']}")
            st.write(f"**Safety:** {prop['safety_score']}/100")
            st.write(f"**Appreciation:** {prop['appreciation']}")
            st.write(f"**Value For Money:** {prop['value_for_money']}/100")
            st.write(f"**Best For:** {prop['best_for']}")
            st.write(f"**Hospital:** {prop['facilities']['hospital']}")
            st.write(f"**Airport:** {prop['facilities']['airport']}")
            st.write(f"**Market:** {prop['facilities']['market']}")


elif active_page == "Sell Property":
    st.markdown('<div class="section-title">Sell Your Property</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Share your property details and highlight nearby facilities.</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    name = st.text_input("Your Name", key="sell_name")
    phone = st.text_input("Phone Number", key="sell_phone")
    property_type = st.selectbox("Property Type", ["Apartment", "Villa", "Independent House", "Plot", "Commercial"], key="sell_type")
    location = st.selectbox("Property Location", ["Jagatpura", "Malviya Nagar", "Mansarovar", "Vaishali Nagar", "C-Scheme", "Ajmer Road"], key="sell_location")
    expected_price = st.number_input("Expected Selling Price", min_value=100000, value=5000000, key="sell_price")
    urgency = st.selectbox("Selling Urgency", ["Immediately", "Within 1 month", "Within 3 months", "Just exploring"], key="sell_urgency")

    st.write("### Highlight Your Property Features")
    near_hospital = st.checkbox("Near hospital")
    near_airport = st.checkbox("Near airport")
    near_railway = st.checkbox("Near railway station")
    near_gym = st.checkbox("Near gym")
    near_college = st.checkbox("Near school/college")
    near_market = st.checkbox("Near market")

    if st.button("Submit Property", key="sell_submit"):
        selected_features = []
        if near_hospital:
            selected_features.append("Hospital nearby")
        if near_airport:
            selected_features.append("Airport access")
        if near_railway:
            selected_features.append("Railway nearby")
        if near_gym:
            selected_features.append("Gym nearby")
        if near_college:
            selected_features.append("School/College nearby")
        if near_market:
            selected_features.append("Market nearby")

        st.success("Property submitted. In real version this will save to database/admin dashboard.")
        st.write("Highlighted Features:", ", ".join(selected_features) if selected_features else "No features selected")


elif active_page == "AI Valuation":
    st.markdown('<div class="section-title">AI Property Valuation</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Get price prediction, locality intelligence, safety score, future growth and AI recommendations.</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    left, right = st.columns(2)

    with left:
        purpose = st.selectbox("Why do you need valuation?", ["Buying", "Selling", "Investment", "Rent Estimation"], key="ai_purpose")
        property_type = st.selectbox("Property Type", ["Apartment", "Villa", "Independent House", "PG / Hostel", "Commercial"], key="ai_type")
        location = st.selectbox("Location", ["Malviya Nagar", "Mansarovar", "Vaishali Nagar", "Jagatpura", "C-Scheme"], key="ai_location")
        sqft = st.number_input("Square Feet", min_value=500, max_value=10000, value=1500, key="ai_sqft")
        bedrooms = st.slider("Bedrooms", 1, 10, 3, key="ai_bedrooms")
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
            backend_purpose = "Buy" if purpose in ["Buying", "Selling", "Investment"] else "Rent"

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
                "purpose": backend_purpose
            }

            files = {"file": (img_file.name, img_file.getvalue(), img_file.type)}

            try:
                response = requests.post(f"{API_URL}/predict", data=data, files=files, timeout=20)

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

                    for item in result["similar_properties"]:
                        st.markdown(f"""
                        <div class="card">
                            <h3>{item['title']}</h3>
                            <p>Location: {item['location']}</p>
                            <p>Purpose: {item['purpose']}</p>
                            <p>Price: ₹{int(item['price']):,}</p>
                            <p>Match Score: {item['match_score']}/100</p>
                        </div>
                        """, unsafe_allow_html=True)

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

                    st.markdown('</div>', unsafe_allow_html=True)

            except requests.exceptions.ConnectionError:
                st.error("Backend is not running. Start backend using: uvicorn main:app --reload")
            except requests.exceptions.Timeout:
                st.error("Backend took too long to respond.")
            except Exception as e:
                st.error(f"Frontend error: {e}")


st.markdown("""
<div class="footer">
    <h2>Seek A Nest AI</h2>
    <p>Jaipur homes • Student rentals • AI valuation • Facilities • Safety • Appreciation • Smart recommendations</p>
</div>
""", unsafe_allow_html=True)