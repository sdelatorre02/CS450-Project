import fitz
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag, ne_chunk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
import string

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("maxent_ne_chunker_tab")
nltk.download("words")

def extract_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    stop_words = set(stopwords.words("english"))
    tokens_to_remove = set()

    # Tokenize into sentences first
    for sent in sent_tokenize(text):
        words = word_tokenize(sent)
        tagged = pos_tag(words)
        chunks = ne_chunk(tagged)

        for chunk in chunks:
            if isinstance(chunk, Tree):
                label = chunk.label()
                if label in ["GPE", "PERSON", "ORGANIZATION", "DATE", "TIME"]:
                    for leaf in chunk.leaves():
                        tokens_to_remove.add(leaf[0].lower())

    # Final filtering
    words = word_tokenize(text.lower())
    filtered = [w for w in words if w.isalpha() and w not in stop_words and w not in tokens_to_remove]
    return " ".join(filtered)
