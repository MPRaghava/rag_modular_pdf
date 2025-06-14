from PyPDF2 import PdfReader

def loader(file)-> str:
   """ Reads and extracts the text from an uploaded PDF file
   this method accepts file -like object(typically from a web UI like Streamlit) 
   Args:
        uploaded_file: A file-like object representing a PDF (e.g., from Streamlit's file_uploader).

    Returns:
        str: The extracted raw text from the PDF.

    Raises:
        ValueError: If the uploaded file is not a PDF or is empty.
        ImportError: If required PDF libraries are not available.

    Example:
        >>> uploaded_text = handle_uploaded_file(pdf_file)
        >>> print(uploaded_text[:100])
    """
   reader = PdfReader(file)
   text =""
   for page in reader.pages:
        text += page.extract_text()
   return text


