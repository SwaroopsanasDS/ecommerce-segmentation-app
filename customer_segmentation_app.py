import streamlit as st

# Page configuration
st.set_page_config(page_title="Customer Segmentation App", layout="centered")

# Custom CSS: cleaner, modern style
st.markdown("""
    <style>
    .stButton>button {
        background-color: #6e00ff;
        color: white;
        font-weight: 600;
        padding: 10px 20px;
        font-size: 15px;
        border: none;
        border-radius: 8px;
        margin-top: 15px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #5800cc;
    }

    h1, h2, h3, label {
        font-family: 'Segoe UI', sans-serif;
        color: #dddddd;
    }

    .result-box {
        font-size: 18px;
        font-weight: 600;
        color: #ffffff;
        background-color: #222;
        border-left: 5px solid #6e00ff;
        padding: 15px;
        border-radius: 6px;
        margin-top: 20px;
    }

    .stApp {
        background-color: #111;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 style='text-align: center;'>Customer Segmentation App</h1>", unsafe_allow_html=True)
st.markdown("### 🔍 Adjust the RFM values to see which segment your customer belongs to.")

# Sliders
recency = st.slider("📅 Recency (days since last purchase)", 0, 100, 50)
frequency = st.slider("🔁 Frequency (purchase count)", 0, 100, 50)
monetary = st.slider("💵 Monetary (total spend in $)", 0, 2000, 1000)

# Prediction function
def predict_customer(recency, frequency, monetary):
    score = recency * 0.5 + frequency * 0.3 + monetary * 0.2
    if score < 20:
        return "🧊 Churned Customer"
    elif score < 50:
        return "😐 Mid-Value Customer"
    elif score < 80:
        return "💰 Low-Value Customer"
    else:
        return "🌟 High-Value Customer"

# Button + Output
if st.button("🔮 Predict Customer Segment"):
    result = predict_customer(recency, frequency, monetary)
    st.markdown(f"<div class='result-box'>{result}</div>", unsafe_allow_html=True)
