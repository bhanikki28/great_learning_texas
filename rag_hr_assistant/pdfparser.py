from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    print(f'Going to parse the pdf file {pdf_path}')
    # Initialize the reader
    reader = PdfReader(pdf_path)

    # Check the total no of pages
    total_pages = len(reader.pages)
    print(f'Total no of pages {total_pages}')