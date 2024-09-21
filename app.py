import streamlit as st
from transformers import pipeline

# Title for the web app
st.title("Speech-to-Text Transcription App")

# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])

if uploaded_file is not None:
    # Load the Whisper model from Hugging Face
    transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-small")

    # Perform transcription
    transcription = transcriber(uploaded_file)

    # Display the transcription text
    st.write("Transcription: ", transcription['text'])
