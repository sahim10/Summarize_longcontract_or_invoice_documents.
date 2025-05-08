import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_data: bytes) -> str:
    # Open the PDF file using PyMuPDF
    pdf_document = fitz.open(stream=pdf_data, filetype="pdf")
    text = ""

    # Loop through each page and extract the text
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    return text
    