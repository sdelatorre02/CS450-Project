import numpy as np
from numpy.linalg import norm


def GetCosineSim(a, b):
    # Pass in list a and list b to get their cosine similarity
    return np.dot(a,b)/(norm(a)*norm(b))