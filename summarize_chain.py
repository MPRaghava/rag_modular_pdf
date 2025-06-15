from qa_chain import get_llm_chain
from langchain.chains.summarize import load_summarize_chain
from langchain_core.documents import Document

llm = get_llm_chain()

def summarize_doc():
    return load_summarize_chain(llm,chain_type="map_reduce",return_intermediate_steps=True)

def only_docs(docs):
    only_docs =[]
    for d in docs:
            if isinstance(d,Document):
                    return only_docs.append(d)
            elif isinstance(d, (list, tuple)) and isinstance(d[0], Document):
                    return only_docs.append(d[0])
            else:
                raise ValueError(f"Unexpected type in docs: {type(d)} with value: {d}")