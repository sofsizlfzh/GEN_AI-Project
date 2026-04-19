import streamlit as st
from groq import Groq
import PyPDF2
import docx

st.set_page_config(
    page_title="Smart Email Generator",
    page_icon="✉️",
    layout="wide"
)

API_KEY = "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"
client = Groq(api_key=API_KEY)

DOCUMENT_TYPES = [
    "Professional Email",
    "Cover Letter",
    "Formal Application",
    "Job Application",
    "Business Proposal",
    "Complaint Letter",
    "Thank You Letter"
]

TONES = [
    "Professional",
    "Friendly",
    "Formal",
    "Persuasive",
    "Urgent",
    "Empathetic"
]

LENGTHS = {
    "Short": 120,
    "Medium": 220,
    "Detailed": 350,
    "Long": 500
}

st.markdown("""
<style>
html, body, [class*="css"]{font-family:Arial;}
.stApp{background:linear-gradient(135deg,#020617,#071226,#0f172a);}
.main-title{font-size:42px;font-weight:800;color:white;}
.sub-title{color:#cbd5e1;margin-bottom:25px;}
.card,.output-box{
background:rgba(255,255,255,0.03);
border:2px solid #38bdf8;
border-radius:18px;
padding:20px;
}
label{color:#e0f2fe !important;font-weight:600 !important;}
input,textarea{
background:white !important;
color:#111827 !important;
border:2px solid #38bdf8 !important;
border-radius:12px !important;
}
div[data-baseweb="select"] > div{
background:white !important;
color:#111827 !important;
border:2px solid #38bdf8 !important;
border-radius:12px !important;
}
.stButton > button{
width:100%;
background:linear-gradient(90deg,#0ea5e9,#2563eb);
color:white !important;
font-weight:700;
border:none;
border-radius:14px;
padding:14px;
}
h3{color:white !important;}
</style>
""", unsafe_allow_html=True)

def read_file(uploaded_file):
    text = ""
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".txt"):
            text = uploaded_file.read().decode("utf-8")

        elif uploaded_file.name.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"

        elif uploaded_file.name.endswith(".docx"):
            doc = docx.Document(uploaded_file)
            for para in doc.paragraphs:
                text += para.text + "\n"

    return text

def make_prompt(doc_type, sender, recipient, subject, info, tone, length, language):
    words = LENGTHS[length]

    return f"""
Write a professional {doc_type}.

Sender: {sender}
Recipient: {recipient}
Subject: {subject}
Tone: {tone}
Language: {language}
Length: {words} words

Use this resume/details:
{info}

Use greeting, paragraphs and strong ending.
Return only final draft.
"""

def generate_text(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

if "result" not in st.session_state:
    st.session_state.result = ""

st.markdown('<div class="main-title">✉️ Smart Email & Letter Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Generate emails, applications and letters using AI.</div>', unsafe_allow_html=True)

left,right = st.columns(2,gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    doc_type = st.selectbox("Document Type", DOCUMENT_TYPES)
    sender = st.text_input("Your Name","Aditya")
    recipient = st.text_input("Recipient Name / Company")
    subject = st.text_input("Subject / Role")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF / DOCX / TXT)",
        type=["pdf","docx","txt"]
    )

    file_text = read_file(uploaded_file)

    info = st.text_area(
        "Additional Information",
        value=file_text,
        height=220,
        placeholder="Upload resume or write details manually..."
    )

    tone = st.selectbox("Tone",TONES)
    length = st.selectbox("Length",list(LENGTHS.keys()))
    language = st.selectbox("Language",["English","Hindi","French","Spanish"])

    if st.button("✨ Generate Professional Draft"):
        if subject.strip()=="":
            st.error("Please enter subject.")
        else:
            with st.spinner("Generating..."):
                prompt = make_prompt(
                    doc_type,sender,recipient,
                    subject,info,tone,length,language
                )
                st.session_state.result = generate_text(prompt)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="output-box">', unsafe_allow_html=True)

    st.subheader("Generated Output")

    st.text_area(
        "Output",
        st.session_state.result,
        height=520,
        label_visibility="collapsed"
    )

    if st.session_state.result:
        st.download_button(
            "⬇ Download TXT",
            st.session_state.result,
            file_name="document.txt",
            mime="text/plain",
            use_container_width=True
        )

    st.markdown('</div>', unsafe_allow_html=True)
