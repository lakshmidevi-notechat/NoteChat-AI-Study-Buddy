import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
import os

# Page setup
st.set_page_config(page_title="NoteChat", page_icon="📝")
st.title("📝 NoteChat - Your Study Buddy")
st.write("PDF upload panni question kelu, AI answer pannum!")

# API Key setup
GOOGLE_API_KEY = st.text_input("Gemini API Key ah inga paste pannu:", type="password")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # PDF upload
    pdf = st.file_uploader("PDF file upload pannu", type="pdf")
    
    if pdf:
        # PDF ah read pannu
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        st.success("PDF read aachu! Ippo question kelu 👇")
        
        # Question kelunga
        question = st.text_input("Unnoda question:")
        
        if st.button("Answer sollu"):
            if question:
                with st.spinner("AI yosikuthu..."):
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    prompt = f"PDF Content: {text}\n\nQuestion: {question}\n\nAnswer in Tamil and English. Simple ah sollu."
                    response = model.generate_content(prompt)
                    st.write("### Answer:")
                    st.write(response.text)
            else:
                st.warning("Question type pannu da!")
else:
    st.info("Mela API Key poda da. aistudio.google.com la free ah kedaikum.")