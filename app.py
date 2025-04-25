import streamlit as st
from doc_similarity import ResumeDoc2VecAnalyzer
from pdf_reading import extract_pdf

# Function to handle file uploads and process them
def upload_and_analyze():
    uploaded_resume = st.file_uploader("Upload your resume", type=["pdf"])
    uploaded_job_desc = st.file_uploader("Upload the job description", type=["pdf"])

    if uploaded_resume and uploaded_job_desc:
        # Read and extract text from the PDFs
        resume_text = extract_pdf(uploaded_resume)
        job_desc_text = extract_pdf(uploaded_job_desc)

        # Instantiate the analyzer and compute similarity
        analyzer = ResumeDoc2VecAnalyzer()
        similarity_score = analyzer.compare_documents(resume_text, job_desc_text)

        # Display the similarity score
        st.write(f"Similarity Score: {similarity_score:.5f}")
        
        # Display recommendation based on similarity score
        if similarity_score > 0.8:
            st.success("Your resume is a good match for the job description!")
        elif similarity_score > 0.5:
            st.warning("Your resume is somewhat relevant. Consider improving it.")
        else:
            st.error("Your resume does not match well with the job description.")
        view_option = st.selectbox(
            "Optional: View extracted text",
            ("None", "Resume Text", "Job Description Text")
        )

        if view_option == "Resume Text":
            st.subheader("Extracted Resume Text")
            st.write(resume_text)
        elif view_option == "Job Description Text":
            st.subheader("Extracted Job Description Text")
            st.write(job_desc_text)

# Run the function when the app starts
if __name__ == "__main__":
    st.title("Resume vs Job Description Analyzer")
    upload_and_analyze()
