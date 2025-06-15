import os
import pickle
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from embedder import get_embedder

def get_or_create_vectorstore(chunks,store_name):
    embedder = get_embedder()
    store_file = f"{store_name}.pkl"

    if os.path.exists(store_file):
        with open(store_file,"rb") as f:
            return pickle.load(f)
    else:
        vectorstore = FAISS.from_texts(chunks,embedder)
        with open(store_file,"wb") as f:
            pickle.dump(vectorstore,f)
        return vectorstore
    
