from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from app.pdf_processing import extract_text_from_pdf
from app.summarizer import summarize_text
from app.utils import extract_entities
import fitz  # PyMuPDF

app = FastAPI()

class SummaryResponse(BaseModel):
    summary: str
    entities: dict

@app.post("/summarize_pdf/", response_model=SummaryResponse)
async def summarize_pdf(file: UploadFile = File(...)):
    # Read the uploaded PDF file
    pdf_file = await file.read()

    # Check the number of pages in the PDF (using PyMuPDF)
    pdf_document = fitz.open(stream=pdf_file, filetype="pdf")
    page_count = pdf_document.page_count

    # If the PDF has more than 3 pages, raise an error
    if page_count > 3:
        raise HTTPException(status_code=400, detail="PDF must not exceed 3 pages.")

    # Extract text from PDF
    text = extract_text_from_pdf(pdf_file)

    # Summarize the text
    summary = summarize_text(text)

    # Extract important information (like dates, payment terms, etc.)
    entities = extract_entities(text)

    # Return the summary and entities
    return SummaryResponse(summary=summary, entities=entities)
