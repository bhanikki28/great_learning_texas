from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    print(f'Going to parse the pdf file {pdf_path}')
    # Initialize the reader
    reader = PdfReader(pdf_path)

    # Check the total no of pages
    total_pages = len(reader.pages)
    print(f'Total no of pages {total_pages}')

    full_text = []

    # Loop through each page and extract text

    for index,page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            full_text.append(text)
        else:
            print(f"Warning Page : {index + 1} appears to be  empty or an image")
    
    # combine all pages into full string
        return "\n".join(full_text)
    
    
        