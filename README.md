#  Task : PDF File Summarizer API

##  Task Description

This project implements a FastAPI-based service to summarize long **contract** or **invoice** PDF documents and extract key entities. It fulfills the following requirements:

- Accept a **PDF (maximum 3 pages)**
- Extract text using **PyMuPDF** (`fitz`)
- Use a **transformers-based summarization model** (Huggingface)
- Return a **JSON response** with:
  - A generated summary
  - Detected entities such as:
    - Dates
    - Payment terms
    - Penalties
    - Companies
    - Contract types

---

##  Tech Stack

- **Python 3.10+**
- **FastAPI** for API framework
- **PyMuPDF (fitz)** for PDF text extraction
- **Huggingface Transformers** for LLM summarization
- **Uvicorn** for running the API server

---

## Project Structure

pdf-summarizer-api/
├── app/
│ ├── main.py # FastAPI app & endpoint
│ ├── pdf_processing.py # PDF text extraction using PyMuPDF
│ ├── summarizer.py # Huggingface summarizer logic
│ └── utils.py # Entity extraction logic
├── requirements.txt # Python dependencies
├── README.md # Project documentation


---

##  Installation & Setup

1. **Clone the repo**

git clone <url>
cd pdf-summarizer-api

2. Create a virtual environment

python -m venv venv
 # mac  : source venv/bin/activate 
 # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Run the API locally

uvicorn app.main:app --reload

API will be running at: http://127.0.0.1:8000

How to Test with Postman
1. Open Postman and create a new POST request:

http://127.0.0.1:8000/summarize_pdf/

2. Set the body type to form-data:
Key: file

Type: File

Upload a PDF file (max 3 pages)

3. Click Send and you'll get a JSON response like:
{
  "summary": "Contract Agreement between Company A and Company B...",
  "entities": {
    "payment_terms": ["30 days"],
    "penalties": ["2% per month"],
    "companies": ["Company A", "Company B"],
    "contract_types": ["Service Agreement"]
  }
}


**Features**
*Rejects PDFs over 3 pages

*Summarizes text using LLM

*Extracts critical contract metadata

Returns structured, API-friendly JSON
