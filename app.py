import streamlit as st
import requests
from PIL import Image

st.set_page_config(
    page_title="Seek A Nest AI",
    page_icon="🏡",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/predict"

st.markdown("""
<style>
.stApp {
    background: #f7f3ea;
    color: #1f2933;
}

.block-container {
    padding-top: 0;
    max-width: 1200px;
}

.navbar {
    background: #ffffff;
    padding: 18px 35px;
    border-radius: 0 0 22px 22px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.07);
    margin-bottom: 28px;
}

.logo {
    font-size: 28px;
    font-weight: 900;
    color: #1f4d3a;
}

.nav {
    color: #6b7280;
    font-weight: 600;
}

.hero {
    background: linear-gradient(rgba(20,45,34,0.72), rgba(20,45,34,0.72)),
                url("https://images.unsplash.com/photo-1600585154340-be6161a56a0c");
    background-size: cover;
    background-position: center;
    padding: 90px 55px;
    border-radius: 28px;
    color: white;
    margin-bottom: 45px;
}

.hero h1 {
    font-size: 62px;
    line-height: 1.05;
    font-weight: 900;
    max-width: 760px;
}

.hero p {
    font-size: 20px;
    max-width: 680px;
    color: #f3f4f6;
}

.cta {
    display: inline-block;
    margin-top: 22px;
    padding: 14px 24px;
    background: #d97706;
    color: white;
    border-radius: 999px;
    font-weight: 800;
}

.section-title {
    text-align: center;
    font-size: 38px;
    font-weight: 900;
    color: #1f4d3a;
    margin-top: 45px;
}

.section-subtitle {
    text-align: center;
    color: #6b7280;
    font-size: 17px;
    margin-bottom: 30px;
}

.card {
    background: white;
    border-radius: 24px;
    padding: 28px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.07);
    min-height: 190px;
}

.card h3 {
    color: #1f4d3a;
    font-size: 24px;
}

.card p {
    color: #6b7280;
}

.property-card {
    background: white;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
}

.property-img {
    height: 180px;
    background: linear-gradient(135deg, #d9c7a3, #8fa98c);
}

.property-body {
    padding: 24px;
}

.price {
    color: #1f4d3a;
    font-size: 26px;
    font-weight: 900;
}

.ai-panel {
    background: #ffffff;
    padding: 35px;
    border-radius: 28px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
    margin-top: 20px;
}

.result-box {
    background: #1f4d3a;
    color: white;
    padding: 30px;
    border-radius: 24px;
    margin-top: 28px;
}

.metric-card {
    background: rgba(255,255,255,0.12);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
}

.metric-number {
    font-size: 26px;
    font-weight: 900;
}

.metric-label {
    color: #e5e7eb;
}

.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 999px;
    border: none;
    background: #d97706;
    color: white;
    font-weight: 900;
    font-size: 16px;
}

.stButton > button:hover {
    background: #b45309;
    color: white;
}

.footer {
    background: #1f4d3a;
    color: white;
    margin-top: 55px;
    padding: 35px;
    border-radius: 28px 28px 0 0;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="navbar">
    <div class="logo">🏡 Seek A Nest</div>
    <div class="nav">Buy Homes &nbsp; • &nbsp; Rent & PGs &nbsp; • &nbsp; Sell &nbsp; • &nbsp; Compare &nbsp; • &nbsp; AI Valuation</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Find your perfect nest in Jaipur.</h1>
    <p>
        Discover homes, student rentals, investment properties and AI-powered valuation reports
        built specially for Jaipur buyers, sellers and renters.
    </p>
    <div class="cta">Explore Properties</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Naturally Simple Property Search</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Buy, rent, sell and compare properties with smarter AI insights.</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <h3>🏠 Buy Properties</h3>
        <p>Explore Jaipur homes by location, price, area, furnishing and nearby facilities.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h3>🎓 Student Rentals</h3>
        <p>Find PGs and flats near colleges like JECRC, SKIT, Poornima and Manipal Jaipur.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h3>📊 Compare Properties</h3>
        <p>Compare homes by price, ROI, location, furnishing, parking and amenities.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">Featured Jaipur Homes</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Curated listings for families, students and investors.</div>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

items = [
    ("3 BHK Apartment", "Malviya Nagar", "₹82,00,000", "1800 sq.ft • Semi-Furnished • Parking"),
    ("Student PG Room", "Jagatpura", "₹9,500/month", "Near college • WiFi • Food included"),
    ("Premium Villa", "C-Scheme", "₹1.85 Cr", "3000 sq.ft • Fully Furnished • Luxury area")
]

for col, item in zip([p1, p2, p3], items):
    with col:
        st.markdown(f"""
        <div class="property-card">
            <div class="property-img"></div>
            <div class="property-body">
                <h3>{item[0]}</h3>
                <p>{item[1]}, Jaipur</p>
                <div class="price">{item[2]}</div>
                <p>{item[3]}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="section-title">AI Property Valuation</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Use your ML model as a premium feature inside the website.</div>', unsafe_allow_html=True)

st.markdown('<div class="ai-panel">', unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    st.subheader("Enter Property Details")

    location = st.selectbox(
        "Location",
        ["Malviya Nagar", "Mansarovar", "Vaishali Nagar", "Jagatpura", "C-Scheme"]
    )

    sqft = st.number_input("Square Feet", min_value=500, max_value=10000, value=1500)
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    bathrooms = st.slider("Bathrooms", 1, 10, 2)
    balcony = st.slider("Balcony", 0, 5, 1)
    age_of_property = st.slider("Age of Property", 0, 30, 5)

    furnishing = st.selectbox(
        "Furnishing",
        ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
    )

    parking = st.slider("Parking Slots", 0, 5, 1)
    nearby_facilities = st.slider("Nearby Facilities Score", 1, 10, 7)

    img_file = st.file_uploader("Upload Property Image", type=["jpg", "jpeg", "png"])

    submit = st.button("Generate Valuation Report")

with right:
    st.subheader("Property Preview")

    if img_file:
        image = Image.open(img_file)
        st.image(image, use_container_width=True)
    else:
        st.info("Upload property image to preview.")

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
            "nearby_facilities": str(nearby_facilities)
        }

        files = {
            "file": (
                img_file.name,
                img_file.getvalue(),
                img_file.type
            )
        }

        try:
            response = requests.post(API_URL, data=data, files=files)

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
                st.write(f"**Location:** {location}, Jaipur")

                r1, r2, r3 = st.columns(3)

                with r1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-number">₹{low_price:,}</div>
                        <div class="metric-label">Best Selling Price</div>
                    </div>
                    """, unsafe_allow_html=True)

                with r2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-number">₹{estimated_price:,}</div>
                        <div class="metric-label">Fair Market Price</div>
                    </div>
                    """, unsafe_allow_html=True)

                with r3:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-number">₹{high_price:,}</div>
                        <div class="metric-label">Premium Asking Price</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.write("### AI Insights")
                st.write(f"Condition: **{result['property_condition']}**")
                st.write(f"Investment Score: **{result['investment_score']}/100**")
                st.write(result["future_growth_prediction"])
                st.success(result["ai_recommendation"])

                st.markdown('</div>', unsafe_allow_html=True)

        except requests.exceptions.ConnectionError:
            st.error("Backend is not running. Start backend using: uvicorn main:app --reload")
        except Exception as e:
            st.error(f"Frontend error: {e}")

st.markdown("""
<div class="footer">
    <h2>Seek A Nest AI</h2>
    <p>Jaipur homes • Student rentals • AI valuation • Property comparison</p>
</div>
""", unsafe_allow_html=True)