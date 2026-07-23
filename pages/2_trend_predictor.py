import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Trend Predictor",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Load Files
# -----------------------------
model = joblib.load("fashion_trend_model.pkl")
encoders = joblib.load("label_encoders.pkl")
df = pd.read_csv("fashion_trend.csv")

# -----------------------------
# Title
# -----------------------------
st.title("🤖 AI Fashion Trend Predictor")

st.write(
    "Predict whether a fashion product is likely to be **Trending** or **Not Trending**."
)

st.divider()

# -----------------------------
# Inputs
# -----------------------------

st.subheader("Product details")
left, right = st.columns(2)

with left:
    season = st.selectbox("🌤 Season", sorted(df["season"].unique()))
    category = st.selectbox("👕 Category", sorted(df["category"].unique()))
    color = st.selectbox("🎨 Color", sorted(df["color"].unique()))
    fabric = st.selectbox("🧵 Fabric", sorted(df["fabric"].unique()))

with right:
    region = st.selectbox("🌍 Region", sorted(df["region"].unique()))
    price_usd = st.number_input("💲 Price ($)", min_value=0.0, value=60.0)
    historical_sales_units = st.number_input(
        "📦 Historical Sales", min_value=0, value=1500
    )
    discount_pct = st.slider("🏷️ Discount (%)", 0.0, 65.0, 15.0)

st.subheader("Social & engagement signals")

s1, s2 = st.columns(2)

with s1:
    search_volume_index = st.slider("🔍 Search Volume Index", 0, 100, 49)
    social_media_mentions = st.slider("📣 Social Media Mentions", 0, 11000, 3000)
    instagram_hashtag_count = st.slider("📸 Instagram Hashtag Count", 0, 33000, 7900)
    tiktok_video_count = st.slider("🎵 TikTok Video Count", 0, 5300, 1200)
    influencer_mentions = st.slider("🌟 Influencer Mentions", 0, 32, 15)

with s2:
    customer_rating = st.slider("⭐ Customer Rating", 0.0, 5.0, 4.1)
    return_rate_pct = st.slider("↩️ Return Rate (%)", 0.0, 35.0, 12.0)
    stock_availability_pct = st.slider("📦 Stock Availability (%)", 0.0, 100.0, 75.0)
    repeat_purchase_rate_pct = st.slider("🔁 Repeat Purchase Rate (%)", 0.0, 56.0, 20.0)
    website_click_through_rate = st.slider("🖱️ Click-Through Rate (%)", 0.0, 10.0, 3.5)

st.divider()

# -----------------------------
# Prediction
# -----------------------------

if st.button("🚀 Predict Trend", use_container_width=True):

    
    if price_usd < 30:
        price_tier = "Budget"
    elif price_usd < 70:
        price_tier = "Mid"
    else:
        price_tier = "Premium"

    season_enc = encoders["season"].transform([season])[0]
    region_enc = encoders["region"].transform([region])[0]
    category_enc = encoders["category"].transform([category])[0]
    color_enc = encoders["color"].transform([color])[0]
    fabric_enc = encoders["fabric"].transform([fabric])[0]
    price_tier_enc = encoders["price_tier"].transform([price_tier])[0]

    popularity_score = (
        historical_sales_units * 0.4
        + search_volume_index * 0.3
        + social_media_mentions * 0.2
        + customer_rating * 10 * 0.1
    )

    social_buzz = (
        instagram_hashtag_count
        + tiktok_video_count
        + influencer_mentions
    )

    engagement = (
        website_click_through_rate * repeat_purchase_rate_pct
    )

    input_data = pd.DataFrame([{
        "season": season_enc,
        "region": region_enc,
        "category": category_enc,
        "color": color_enc,
        "fabric": fabric_enc,
        "price_tier": price_tier_enc,
        "price_usd": price_usd,
        "discount_pct": discount_pct,
        "historical_sales_units": historical_sales_units,
        "search_volume_index": search_volume_index,
        "social_media_mentions": social_media_mentions,
        "instagram_hashtag_count": instagram_hashtag_count,
        "tiktok_video_count": tiktok_video_count,
        "influencer_mentions": influencer_mentions,
        "customer_rating": customer_rating,
        "return_rate_pct": return_rate_pct,
        "stock_availability_pct": stock_availability_pct,
        "repeat_purchase_rate_pct": repeat_purchase_rate_pct,
        "website_click_through_rate": website_click_through_rate,
        "popularity_score": popularity_score,
        "social_buzz": social_buzz,
        "engagement": engagement
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data).max() * 100

    st.divider()

    if prediction == "Trending":
        st.success("🔥 Trending")
        st.info("""
        **Recommendation**

        ✅ Increase stock by 20–30%

        ✅ Promote on social media

        ✅ Keep premium pricing
        """)
    else:
        st.error("📉 Not Trending")
        st.info("""
        **Recommendation**

        ✅ Avoid overstocking

        ✅ Offer discounts

        ✅ Re-evaluate marketing strategy
        """)

    st.metric("Prediction Confidence", f"{probability:.2f}%")
    st.markdown("---")

st.caption(
    "👨‍💻 Developed by Mohd Fahad | AI Fashion Trend Forecasting "
)