from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt_tab")

class ResumeDoc2VecAnalyzer:
    def __init__(self):
        self.model = None

    def prepare_documents(self, job_desc, resume_text):
        documents = [
            TaggedDocument(words=word_tokenize(job_desc.lower()), tags=["JOB"]),
            TaggedDocument(words=word_tokenize(resume_text.lower()), tags=["RESUME"])
        ]
        return documents

    def train_model(self, documents):
        model = Doc2Vec(vector_size=50, window=2, min_count=1, workers=4, epochs=40)
        model.build_vocab(documents)
        model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)
        self.model = model

    def compare_documents(self, job_desc, resume_text):
        documents = self.prepare_documents(job_desc, resume_text)
        self.train_model(documents)
        return self.model.dv.similarity("JOB", "RESUME")
