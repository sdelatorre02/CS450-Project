# Resume Similarity Web App

This project allows you to analyze the similarity between a job title and a resume using a trained Doc2Vec model.

## 1. Prerequisites

To run this project, you will  need **Conda** to manage dependencies and an environment with the necessary packages.

### **Setting up the Environment**

First, create a conda environment for the project:

```bash
conda create -n resume_similarity_app python=3.10
conda activate resume_similarity_app
```

## 2. Installing Dependencies

Install the required packages using the conda and pip commands below:

```bash
#install packages from conda-forge channel
conda install -c conda-forge nltk streamlit gensim scipy

#install PyMuPDF for PDF processing using pip
pip install pymupdf
```

## 3. Project Files

The following files are included in the project
* doc_similarity.py: Contains logic for ResumeDoc2VecAnalyzer class, which handles the tokenization and similarity analysis of the resume and job title
* pdf_reading.py: Contains functions that extract texts from PDF uploads and cleans the extracted text
* app.py: Streamlit app that allows user to input job title and upload a resume PDF, which then calculates the similarity between the two
* TaggedVectors: A file that contains previously trained Doc2Vec vectors, which are used for similarity calculations.

## 4. Download TaggedVectors

TaggedVectors file is too large to include in the repo, so please download it from the link below and place in the project directory:

[Download TaggedVectors](https://drive.google.com/file/d/19CinPVHcqvqBgrikBKA2GEJ3Iy1Y09Mh/view?usp=sharing)

## 5. Running the App

After installing the neccessary dependencies and preparing the environment, you can run the app with the following command:

```
streamlit run app.py
```

This will start the Streamlit server and open a local web page in your browser where you can interact with the app.

## 6. Using the App

Once the app is running, you will see the following prompts:

1. Enter Job Title: Type in the job title (e.g., "Software Engineer").

2. Upload Resume PDF: Upload a PDF containing the resume you want to analyze.

3. Display Similarity: The app will calculate and display the similarity between the job title and the resume text, as well as any missing keywords or suggestions for improvement.
