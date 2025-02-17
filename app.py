import streamlit as st
import pandas as pd
from textblob import TextBlob

# Title of the web app
st.title("📢 Real-Time Sentiment Analysis App")

# Description
st.write("Enter a sentence or paragraph below to analyze its sentiment.")

# User input text box
user_input = st.text_area("Enter text for sentiment analysis:")

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment_score = TextBlob(text).sentiment.polarity
    if sentiment_score > 0:
        return "😊 Positive"
    elif sentiment_score < 0:
        return "😠 Negative"
    else:
        return "😐 Neutral"

# Analyze when button is clicked
if st.button("Analyze Sentiment"):
    if user_input.strip():
        sentiment_result = analyze_sentiment(user_input)
        st.write(f"### Sentiment Result: {sentiment_result}")
    else:
        st.warning("Please enter some text to analyze!")

# Option to upload CSV file for batch analysis
st.subheader("📂 Upload a CSV File for Bulk Sentiment Analysis")
uploaded_file = st.file_uploader("Upload CSV (Must have a 'text' column)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    if "text" in df.columns:
        st.write("✅ File uploaded successfully!")
        df["Sentiment"] = df["text"].apply(analyze_sentiment)
        st.write(df.head())  # Display the first few rows with sentiment
        st.download_button("Download Results", df.to_csv(index=False), file_name="sentiment_results.csv", mime="text/csv")
    else:
        st.error("❌ The CSV file must contain a 'text' column.")
