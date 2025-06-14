import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from loader import loader
from preprocessing import clean_pdf_text
from chunker import semantic_chunk

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
         st.write(f"**Extracted text from **: {pdf.name}")
         st.write("**Before Preprocessing.**")
         st.write(raw_text)
         st.write("**After preprocessing.**")
         distilled_text = clean_pdf_text(raw_text)
         st.write(distilled_text)
         st.write("**Sentences splitter:**")
         splitter = semantic_chunk(distilled_text)
         st.write(splitter)
         

if __name__ == "__main__":
    main()
