from sentence_transformers import SentenceTransformer
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np

nltk.download("punkt")

def semantic_chunk(text : str, threshold : float =0.65):
    sentences = sent_tokenize(text)
    # return sentences
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(sentences)

    chunks =[]
    current_chunk =[sentences[0]]
    chunk_id =0

    for i in range(1,len(sentences)):
        sim = cosine_similarity(
            np.array(embeddings[i-0]).reshape(1,-1),
            np.array(embeddings[i]).reshape(1,-1)
            )[0][0]
        if sim > threshold :
            current_chunk.append(sentences[i])
        else:            
            chunks.append("".join(current_chunk))
            current_chunk = [sentences[i]]
    
    if current_chunk:        
        chunks.append("".join(current_chunk))
    return chunks
