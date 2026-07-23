import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Pastel Colors
season_color = "#A8DADC"      # Light Cyan
category_color = "#FFD6A5"    # Light Orange
color_color = "#BDE0FE"       # Light Blue
region_color = "#CDB4DB"      # Lavender
trend_color = "#90EE90"       # Light Green

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="Fashion Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------
df = pd.read_csv("fashion_trend.csv")

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------
with st.sidebar:
    st.title("👕 Fashion Trend AI")
    st.write("📈 Streamlit Dashboard")

# -------------------------------------------------------
# Title
# -------------------------------------------------------
st.markdown("""
# 👔 AI Fashion Trend Forecasting Dashboard
### Predict • Analyze • Forecast Fashion Trends with Machine Learning
""")

st.subheader("Business Overview")
st.info(
    "📈 Monitor fashion trends, customer behavior, product performance and business insights in one place."
)

# -------------------------------------------------------
# KPI Cards
# -------------------------------------------------------

st.subheader("📈 Business Overview")

with st.container(border=True):

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="👕 Total Products",
            value=len(df)
        )

    with col2:
        st.metric(
            label="🔥 Trending Products",
            value=int(df["is_trending"].sum())
        )

    with col3:
        st.metric(
            label="⭐ Average Rating",
            value=round(df["customer_rating"].mean(), 2)
        )

    with col4:
        st.metric(
            label="💰 Average Price",
            value=f"${round(df['price_usd'].mean(),2)}"
        )

    with col5:
        st.metric(
            label="📈 Trend Score",
            value=round(df["trending_score"].mean(),2)
        )
st.divider()

# =======================================================
# Row 1
# =======================================================

left, right = st.columns(2)

# Products by Season
with left:

    st.subheader("📅 Products by Season")

    season = df["season"].value_counts()

    fig, ax = plt.subplots(figsize=(6,4))

    ax.bar(
    season.index,
    season.values,
    color=season_color,
    width=0.55
)

    ax.grid(axis="y", alpha=0.3)

    ax.set_xlabel("Season")
    ax.set_ylabel("Products")
    ax.set_title("Products by Season")

    plt.xticks(rotation=45)

    st.pyplot(fig)

# Top Categories
with right:

    st.subheader("📦 Top Product Categories")

    category = df["category"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(6,4))

    ax.bar(
    category.index,
    category.values,
    color=category_color,
    width=0.55
)

    ax.grid(axis="y", alpha=0.3)
    ax.set_xlabel("Category")
    ax.set_ylabel("Products")
    ax.set_title("Top Categories")

    plt.xticks(rotation=45)

    st.pyplot(fig)

# =======================================================
# Row 2
# =======================================================

left2, right2 = st.columns(2)

# Top Colors
with left2:

    st.subheader("🎨 Top 5 Colors")

    colors = df["color"].value_counts().head(5)

    fig, ax = plt.subplots(figsize=(6,4))

    ax.bar(
    colors.index,
    colors.values,
    color=color_color,
    width=0.55
)

    ax.grid(axis="y", alpha=0.3)

    ax.set_xlabel("Color")
    ax.set_ylabel("Products")
    ax.set_title("Top 10 Colors")

    plt.xticks(rotation=45)

    st.pyplot(fig)

# Products by Region
with right2:

    st.subheader("🌍 Regional Distribution")

    region = df["region"].value_counts()

    fig, ax = plt.subplots(figsize=(6,4))

    ax.bar(
    region.index,
    region.values,
    color=region_color,
    width=0.55
)

    ax.grid(axis="y", alpha=0.3)
    ax.set_xlabel("Region")
    ax.set_ylabel("Products")
    ax.set_title("Products by Region")

    plt.xticks(rotation=45)

    st.pyplot(fig)

# =======================================================
# Trending Label
# =======================================================

st.subheader("🔥 Trending Label Distribution")

trend = df["trending_label"].value_counts()

fig, ax = plt.subplots(figsize=(6,3))

ax.barh(
    trend.index,
    trend.values,
    color=trend_color,
    height=0.4
)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.grid(axis="x", alpha=0.3)

st.pyplot(fig)


# =======================================================
# Top Trending Products
# =======================================================

st.subheader("🏆 Top 10 Trending Products")

top_products = (
    df.sort_values(
        by="trending_score",
        ascending=False
    )[[
        "product_name",
        "category",
        "color",
        "season",
        "trending_score"
    ]]
    .head(10)
)

st.dataframe(top_products, use_container_width=True)

# =======================================================
# Dataset Preview
# =======================================================

st.subheader("📄 Dataset Preview")

st.write(f"**Dataset Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

st.dataframe(df.head(10), use_container_width=True)

# =======================================================
# Footer
# =======================================================

st.markdown("---")

st.caption(
    "👨‍💻 AI Fashion Trend Forecasting System"
)
