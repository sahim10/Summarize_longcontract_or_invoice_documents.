from transformers import pipeline

# Initialize the summarizer pipeline
summarizer = pipeline("summarization")

def summarize_text(text: str) -> str:
    # Summarize the text using Huggingface transformer model
    summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
    return summary[0]["summary_text"]
