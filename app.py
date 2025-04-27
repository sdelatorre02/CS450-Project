import pickle
import streamlit as st
from doc_similarity2 import ResumeDoc2VecAnalyzer as DocSim
from pdf_reading import extract_pdf, clean_text  # Assuming extract_pdf cleans and extracts text

# Load model and preprocessed vectors
model = DocSim()
with open('TaggedVectors', 'rb') as vecs:
    ser = pickle.load(vecs)  # Load previously processed vectors into ser

# Function to analyze resume similarity
def analyze_resume(job_title, resume_pdf):
    # Extract and clean the text from the uploaded PDF resume
    resume_text = extract_pdf(resume_pdf)
    clean_resume_text = clean_text(resume_text)
    # Tokenize the resume and job title into 'resume' and 'irr' (irrelevant) for comparison
    ser.append(model.tokenize_doc(resume_text, ["resume"]))
    ser.append(model.tokenize_doc(job_title, ["irr"]))
    
    # Train the model with the new resume
    model.train_model(ser)
    
    # Find the similarity score
    similarity_score = model.find_similarity(job_title, 'resume')  # Compare job title with resume
    
    return similarity_score, resume_text

# Streamlit app layout
st.title("Resume Job Title Fit Analyzer")
st.write("Upload your resume and specify the job title to analyze resume fit.")

# User input for job title
job_title = st.text_input("Enter Job Title", "")

# Upload file for resume
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_resume and job_title:
    # Analyze the resume and job title
    similarity_score, extracted_resume_text = analyze_resume(job_title, uploaded_resume)
    
    # Display the similarity result
    st.write(f"Similarity Score for Job Title: '{job_title}' and Resume: {similarity_score}")
    
    # Dropdown to select between extracted resume text or just the similarity score
    display_option = st.selectbox("Select option to display:", ["Similarity Score", "Extracted Resume Text"])
    
    if display_option == "Extracted Resume Text":
        # Display the extracted resume text
        st.subheader("Extracted Resume Text")
        st.write(extracted_resume_text)
else:
    st.write("Please provide both a job title and a PDF resume.")
