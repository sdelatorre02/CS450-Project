from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
import pickle

# nltk.download("punkt_tab")

class ResumeDoc2VecAnalyzer:
    def __init__(self):
        self.model = None

    def prepare_documents(self, job_desc, resume_text):
        """ Osvaldo's note: The model should have more than two samples to work from. 
            tokenize_doc was made to be able to tokenize one entry at a time. 
            I will leave this function alone just in case. The team can decide how to handle this
        """
        documents = [
            TaggedDocument(words=word_tokenize(job_desc.lower()), tags=["JOB"]),
            TaggedDocument(words=word_tokenize(resume_text.lower()), tags=["RESUME"])
        ]
        return documents
    
    def tokenize_doc(self, doc: str, tag: list[str]) -> list:
        # Take a string containing the body you wish to tokenize, and a list of strings consisting of the tags that will apply to the resulting tokens
        try:
            tagged_doc = TaggedDocument(words=word_tokenize(doc.lower()), tags=tag)
        except AttributeError or TypeError:
            tagged_doc = TaggedDocument(words=word_tokenize(doc), tags=tag)
        return tagged_doc

    def train_model(self, documents: list[TaggedDocument]):
        # Trains a model off the list of TaggedDocument objects
        model = Doc2Vec(vector_size=300, window=2, min_count=1, workers=4, epochs=40)
        model.build_vocab(documents)
        model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)
        self.model = model

    def compare_documents(self, job_desc, resume_text):
        documents = self.prepare_documents(job_desc, resume_text)
        self.train_model(documents)
        return self.model.dv.similarity("JOB", "RESUME")
    

    def find_similarity(self,tag1: str, tag2: str):
        # Pass two tags from  the model and compare their similarities.
        return self.model.dv.similarity(tag1, tag2)
    
    def save_vectors(self, documents: list[TaggedDocument]):
        # Saves vectors to TaggedVectors directory
        if all(isinstance(i, TaggedDocument) for i in documents):       # Check that all elements are a TaggedDocument object. Saves nothing if other objects found.
            vecs = open("TaggedVectors", "wb")
            pickle.dump(documents, vecs)
            vecs.close()
    
    """I tried to make a function to save vectors but it keeps getting an EOF error."""
    # def load_vectors(self) -> list:
    #     # Loads the previously saved vectors
    #         if os.path.exists("TaggedVectors"):
    #             with open("TaggedVectors", "rb") as vecs:
    #                 data = pickle.load(vecs)
    #             return data
    #         else:
    #             print("No vector file found. Returning an empty list")
    #             return []