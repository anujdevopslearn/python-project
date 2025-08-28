import streamlit as st

st.title("Sleep Predictor AI 🧠")

# Input from user
hours = st.slider("How many hours did you sleep?", 0, 12, 6)

# Basic ML-like logic
def predict(hours_slept):
    return "no energy" if hours_slept < 6 else "Not Tired 😃"
# where are you now
#i am here
# Show prediction
prediction = predict(hours)
st.write(f"Prediction: **{prediction}**")
st.write("*where are you*")
# using command line to save changes
api_key = st.secrets["API_KEY"]

# Fetch another secret
db_password = st.secrets["DB_PASSWORD"]
# new for cli2
#new branch1 is created
"new on"
st.write("✅ Secrets fetched successfully!")
st.write(f"API key length: {len(api_key)}")  # Don't print actual keys in production
