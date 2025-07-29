import streamlit as st
import pandas as pd

# Load CSV files
health_data = pd.read_csv("patient_health.csv", parse_dates=["timestamp"])
score_data = pd.read_csv("student_scores.csv", parse_dates=["time"])

# Streamlit setup
st.set_page_config(page_title="Health & Education Dashboard", layout="wide")
st.title("📊 Health & Education Monitoring Dashboard")

# Create tabs
tab1, tab2 = st.tabs(["💓 Health Monitoring", "📚 Student Scores"])

with tab1:
    st.subheader("Heart Rate, BP & Oxygen Levels Over Time")
    st.line_chart(health_data.set_index("timestamp")[["heart_rate", "bp", "oxygen"]])

    st.subheader("⚠️ Health Alerts")
    if (health_data["oxygen"] < 94).any():
        st.warning("Low oxygen detected!")
    if (health_data["heart_rate"] > 100).any():
        st.error("High heart rate detected!")

with tab2:
    st.subheader("Student Score Trend")
    st.line_chart(score_data.set_index("time")[["score"]])

    st.subheader("📉 Low Score Alerts")
    if (score_data["score"] < 50).any():
        st.error("Low scores detected!")