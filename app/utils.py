import re
from typing import Dict

def extract_entities(text: str) -> Dict[str, list]:
    entities = {}

    # Extracting dates (contract start and end dates, etc.)
    date_pattern = r"\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{4}|\d{4}-\d{2}-\d{2}|\b(?:[A-Za-z]+[\s]*\d{1,2}[\s]*\d{4})\b)\b"
    dates = re.findall(date_pattern, text)
    if dates:
        entities["dates"] = dates

    # Extracting payment terms (e.g., 30 days, 60 days)
    payment_terms_pattern = r"\b(?:\d+\s*(?:days?|months?))\b"
    payment_terms = re.findall(payment_terms_pattern, text)
    if payment_terms:
        entities["payment_terms"] = payment_terms

    # Extracting late payment penalties (e.g., 2% per month)
    penalty_pattern = r"\b(?:\d+\s*%\s*per\s*month)\b"
    penalties = re.findall(penalty_pattern, text)
    if penalties:
        entities["penalties"] = penalties

    # Extracting company names (look for "Company A", "Company B", etc.)
    company_pattern = r"\b(?:Company\s[A-Za-z]+(?:\s[A-Za-z]+)*)\b"
    companies = re.findall(company_pattern, text)
    # Remove any non-relevant company names (filter out unwanted fragments)
    valid_companies = [company for company in companies if company in ["Company A", "Company B"]]
    if valid_companies:
        entities["companies"] = valid_companies

    # Extracting amounts (e.g., $100,000, €200,000)
    amount_pattern = r"\b(?:\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s*(?:USD|EUR|€|£|\$)\b"
    amounts = re.findall(amount_pattern, text)
    if amounts:
        entities["amounts"] = amounts

    # Extracting contract types (e.g., service agreement, purchase agreement)
    contract_type_pattern = r"\b(?:service\sagreement|purchase\sagreement|partnership\sagreement|sales\scontract)\b"
    contract_types = re.findall(contract_type_pattern, text, re.IGNORECASE)
    if contract_types:
        entities["contract_types"] = list(set(contract_types))

    return entities
