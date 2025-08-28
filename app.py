import streamlit as st

st.title("Sleep Predictor AI 🧠")


hours = st.slider("How many hours did you sleep?", 0, 12, 6)

def predict(hours_slept):
    return "Tired 😴" if hours_slept < 6 else "Not Tired 😃"
#changes made by MB
#new changes
prediction = predict(hours)
st.write(f"Prediction: **{prediction}**")


api_key = st.secrets["API_KEY"]

db_password = st.secrets["DB_PASSWORD"]

st.write("✅ Secrets fetched successfully!")
st.write(f"API key length: {len(api_key)}")  # Don't print actual keys in production
#Changes made in branch two..
