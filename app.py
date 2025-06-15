import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from loader import loader
from preprocessing import clean_pdf_text
from chunker import semantic_chunk
from vectorstore import get_or_create_vectorstore
from qa_chain import get_llm_chain
from summarize_chain import summarize_doc, only_docs
from langchain_core.documents import Document


st.set_page_config(page_title="Semantic RAG Chat",layout="centered")

with st.sidebar:
    st.title('LLM Chat App')
    st.markdown('''
    ## About
    This app is LLM-powered chat with PDF using:
    - Streamlit
    - Langchain
    - Sentence- Transformers
    - Groq + gemma 
''')
    add_vertical_space(4)
    st.write('Made with ❤️ by Prompt Engineer')

def main():
    st.title("Chat with PDF  🗨️")
    pdf = st.file_uploader("Upload your file", type ='pdf')
    if pdf:
         raw_text = loader(pdf)
         st.write(f"**Extracted text from : {pdf.name}**")
        #  st.write("**Before Preprocessing.**")
        #  st.write(raw_text)
        #  st.write("**After preprocessing.**")
         distilled_text = clean_pdf_text(raw_text)
        #  st.write(distilled_text)
         st.write("**Sentences splitter:**")
         chunks = semantic_chunk(distilled_text)
        #  st.write(splitter)
         store_name = pdf.name.replace(".pdf", "")
         vectorestore = get_or_create_vectorstore(chunks, store_name)

         query = st.text_input("Ask a question about your document: ")
         if query:
             docs = vectorestore.similarity_search(query,k=2)
            #  only_text = only_docs(docs=docs)
             summarize_chain = summarize_doc()
             summary = summarize_chain.invoke(only_docs)
            #  docs = vectorestore.as_retriever(query,k=3)
             llm_chain = get_llm_chain()
             response = llm_chain.run(input_documents = summary, question = query)
             st.write("🧠 Answer:", response)


if __name__ == "__main__":
    main()
