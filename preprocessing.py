import re

def clean_pdf_text(raw_text :str)->str:
    # Step 1: Remove long sequences of non-word characters (dots, dashes, etc.)
    text = re.sub(r'[.\-=_~]{5,}', ' ', raw_text)

    # Step 2: remove standard page numbers
    text = re.sub(r'\b\d{1,3}\b', '', text)

    # Step 3: Remove extra spaces
    text = re.sub(r'\s{2,}', ' ', text)

    # Step 4 : Remove leading spaces on each line
    lines = text.split('\n')
    cleaned_lines = [line.strip() for line in lines if line.strip()]
   
    # Step 5 : Join back into cleaned string
    cleaned_text = '\n'.join(cleaned_lines)

    return cleaned_text



