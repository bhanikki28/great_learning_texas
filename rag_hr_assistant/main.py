from pdfparser import extract_text_from_pdf
def main():
    print("Hello from rag-hr-assistant!")
    extract_text_from_pdf('resources/Human_Resources_Manual.pdf')


if __name__ == "__main__":
    main()
