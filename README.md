# Resume Similarity Web App

This project allows you to analyze the similarity between a job title and a resume using a trained Doc2Vec model.

## Prerequisites

To run this project, you will  need **Conda** to manage dependencies and an environment with the necessary packages.

### **1. Setting up the Environment**

First, create a conda environment for the project:

```bash
conda create -n resume_similarity_app python=3.10
conda activate resume_similarity_app
```

### **2. Installing Dependencies**

Install the required packages using the conda and pip commands below:

```bash
#install packages from conda-forge channel
conda install -c conda-forge nltk streamlit gensim scipy

#install PyMuPDF for PDF processing using pip
pip install pymupdf
```

### **3. Project Files**

The following files are included in the project
* doc_similarity.py: Contains logic for ResumeDoc2VecAnalyzer class, which handles the tokenization and similarity analysis of the resume and job title
* pdf_reading.py: Contains functions that extract texts from PDF uploads and cleans the extracted text
* app.py: Streamlit app that allows user to input job title and upload a resume PDF, which then calculates the similarity between the two
* TaggedVectors: The trained dataset file that contains previously trained Doc2Vec vectors, which are used for similarity calculations.

### **4. Download TaggedVectors**

TaggedVectors file is too large to include in the repo, so please download the trained dataset from the link below and place in the project directory:

[Download TaggedVectors](https://drive.google.com/file/d/19CinPVHcqvqBgrikBKA2GEJ3Iy1Y09Mh/view?usp=sharing)

## **Running the App**

After installing the neccessary dependencies and preparing the environment, you can run the app with the following command:

```
streamlit run app.py
```

This will start the Streamlit server and open a local web page in your browser where you can interact with the app.

## **Using the App**

Once the app is running, you will see the following prompts:

1. Enter Job Title: Type in the job title (e.g., "Software Engineer").

2. Upload Resume PDF: Upload a PDF containing the resume you want to analyze.

3. Display Similarity: The app will calculate and display the similarity between the job title and the resume text

## **Interpreting Results**

* 1.0 -> Perfect match: The resume is extremely algined with the job title.
* 0.8 - 0.99 -> Strong match: The resume is highly relevant to the job title.
* 0.5 - 0.79 -> Moderate match: Some relevant keywords and concepts are present, but only partial alignment.
* 0.3 - 0.49 -> Weak match: The resume has little in common with the job title.
* 0.0 - 0.29 -> Poor or no match: The resume is likely irrelevant to the job title.

### **Key Considerations**

The score is contextual, so your score can be a good match in a broader field but considered weak in a more specialized area.

High scores suggest that there is shared semantic content such as relevant skills, experience, or keywords

Low scores can result from
  * Resume being in an unrelated field
  * Generic content in the resume
  * Lack of training data covering the job title domain (Model trained on limited examples)
