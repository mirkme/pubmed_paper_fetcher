 # For making HTTP requests to PubMed API
import requests 

# Type hints for better code clarity and tooling support
from typing import List, Dict

# Base URL for PubMed's Entrez API endpoints
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# Optional email as per NCBI's recommendation for identification and contact in heavy use cases
EMAIL = "shelarcharuta04@gmail.com"  # Optional: NCBI recommends this for heavy use


def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    if debug:
        print(f"[DEBUG] Searching PubMed for: {query}")

    # Construct search endpoint and parameters to get matching PubMed IDs
    search_url = f"{BASE_URL}esearch.fcgi"
    search_params = {
        "db": "pubmed",   # target PubMed database
        "term": query,    # The user’s search query
        "retmax": 20,     # Limit to 20 results for now
        "retmode": "json",# Get results in JSON format
        "email": EMAIL    # Include email for good practice
    }

    # Make the search request
    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()

    # Extract list of paper IDs from the response
    ids = search_data.get("esearchresult", {}).get("idlist", [])

    if debug:
        print(f"[DEBUG] Found {len(ids)} papers.")

    if not ids:
        return []  # Return empty list if no IDs found

    # Construct fetch endpoint to get metadata of found papers
    fetch_url = f"{BASE_URL}efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),  # Join all paper IDs into comma-separated string
        "retmode": "xml",     # Return metadata in XML format
        "email": EMAIL
    }
    
    # Fetch the detailed paper metadata
    fetch_response = requests.get(fetch_url, params=fetch_params)
    if fetch_response.status_code != 200:
        raise Exception("Error fetching paper details")
    
    # Parse and return structured data from the XML response
    return parse_pubmed_xml(fetch_response.text)


def parse_pubmed_xml(xml_data: str) -> List[Dict]:
    # XML parsing library
    import xml.etree.ElementTree as ET

    root = ET.fromstring(xml_data)  # Convert string to XML tree
    results = []  # List to collect parsed paper data

    for article in root.findall(".//PubmedArticle"):   # Loop through each article
        try:
             # Extract metadata from XML tags
            pmid = article.findtext(".//PMID")
            title = article.findtext(".//ArticleTitle")
            pub_date = article.findtext(".//PubDate/Year") or "Unknown"
            
            # Extract authors, names, affiliations, and attempt to extract emails
            authors = [
                {
                    "name": f"{a.findtext('ForeName', '')} {a.findtext('LastName', '')}".strip(),
                    "affiliation": a.findtext(".//AffiliationInfo/Affiliation", default=""),
                    "email": extract_email(a.findtext(".//AffiliationInfo/Affiliation", default=""))
                }
                for a in article.findall(".//Author")
            ]
            # Append all extracted data as one dict into results
            results.append({
                "pmid": pmid,
                "title": title,
                "publication_date": pub_date,
                "authors": authors
            })
        except Exception as e:
            print(f"[WARN] Skipping article due to error: {e}")

    return results


def extract_email(text: str) -> str:
    # Extracts email from affiliation string if present.
    import re
    if not text:
        return "" # Return empty if no text
    match = re.search(r"[\w\.-]+@[\w\.-]+", text)  # Simple regex for email detection
    return match.group(0) if match else ""  # Return email if found
