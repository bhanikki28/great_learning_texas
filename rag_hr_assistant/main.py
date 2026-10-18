from pdfparser import extract_text_from_pdf
from dotenv import load_dotenv
import os
load_dotenv()
def main():
    print("Hello from rag-hr-assistant!")
    pdf_content = extract_text_from_pdf('resources/Human_Resources_Manual.pdf')
    print(pdf_content[:500])
    open_ai_key = os.getenv("OPENAI_API_KEY")
    print(open_ai_key)


if __name__ == "__main__":
    main()
