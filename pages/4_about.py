import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.markdown("---")

st.header("📌 Project Title")

st.write("""
**AI-Based Fashion Trend Forecasting using Machine Learning**
""")

st.header("🎯 Project Objective")

st.write("""
The objective of this project is to predict fashion trends using
Machine Learning. The system analyzes historical sales, search
volume, customer engagement, season, category, and other features
to identify whether a product is likely to become a Low, Medium,
or High Trend.
""")

st.header("🛠️ Technologies Used")

st.markdown("""
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Random Forest Classifier
- Streamlit
- Joblib
""")

st.header("📊 Dataset")

st.write("""
The dataset contains around **10,000 fashion products** with
features such as:

- Season
- Category
- Color
- Region
- Price
- Historical Sales
- Search Volume
- Customer Rating
- Social Media Engagement
""")

st.header("🤖 Machine Learning Model")

st.write("""
The project uses a **Random Forest Classifier** to predict whether
a product is:

- 🔥 High Trend
- 📈 Medium Trend
- 📉 Low Trend
""")

st.header("✨ Key Features")

st.markdown("""
- 📊 Interactive Dashboard
- 🤖 AI Trend Prediction
- 📈 Business Insights
- 🏆 Top Trending Products
- 🎨 Clean User Interface
""")

st.header("🚀 Future Scope")

st.markdown("""
- Real-time trend prediction
- Social media integration
- Deep Learning models
- Personalized recommendations
- Cloud deployment
""")

st.markdown("---")

st.caption("👨‍💻 Developed by Mohd Fahad")