from langchain.chains.question_answering import load_qa_chain
from langchain_groq import ChatGroq
from config import GROQ_API_KEY


def get_llm_chain():
    llm = ChatGroq(model_name ="gemma2-9b-it", api_key=GROQ_API_KEY)
    return load_qa_chain(llm = llm, chain_type="map_reduce")

