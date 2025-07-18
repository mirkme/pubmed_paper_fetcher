from typing import List, Dict

# LLM variants (comment/uncomment depending on what you use)
#from pubmed_paper_fetcher.llm_helper import is_industry_affiliation_llm #huggingface
#from pubmed_paper_fetcher.llm_helperopenai import is_industry_affiliation_llm  #openai
from pubmed_paper_fetcher.llm_helper_ollama import is_industry_affiliation_llm  #ollama




# Define keywords to detect companies
COMPANY_KEYWORDS = [
    "pharma", "biotech", "therapeutics", "inc", "ltd", "llc", "company", "gmbh",
    "corporation", "technologies", "labs", "pvt", "diagnostics", "industries", "solutions", "genomics"
]

ACADEMIC_KEYWORDS = [
    "university", "institute", "college", "hospital", "school", "faculty", "dept", "department of"
]


def is_non_academic(affiliation: str, use_llm: bool = False) -> bool:
    # Determines if an affiliation is from a company (non-academic).If unsure, optionally uses LLM to decide.
    if not affiliation:
        return False   # If there's no affiliation, assume it's not non-academic

    affil = affiliation.lower()  # for case-insensitive comparison

    # Keyword match for company indicators
    for keyword in COMPANY_KEYWORDS:
        if keyword in affil:
            return True

    # If academic keyword found, treat it as academic
    for keyword in ACADEMIC_KEYWORDS:
        if keyword in affil:
            return False

    # If heuristics can't decide, use LLM to make the judgment
    if use_llm:
        return is_industry_affiliation_llm(affiliation)

    return False  # Default to academic if no match and LLM is not used


def filter_non_academic_authors(papers: List[Dict], debug: bool = False) -> List[Dict]:
    # Goes through each paper and includes only those with at least one non-academic (company) author.Extracts details like non-academic author names, affiliations, and contact email.
    
    result = []

    for paper in papers:
        non_acad_authors = []   # Names of authors flagged as non-academic
        company_names = set()   # Unique company affiliations
        email = ""              # Corresponding author email (if any)

        for author in paper.get("authors", []):
            affil = author.get("affiliation", "")
            
            # Use LLM if heuristics are unsure
            if is_non_academic(affil, use_llm=True): # Set use_llm=True to always use AI
                non_acad_authors.append(author["name"])
                company_names.add(affil)
                 # Store the first found email
                if not email and author.get("email"):
                    email = author["email"]
        # If there are any non-academic authors, store the paper's data
        if non_acad_authors:
            result.append({
                "PubmedID": paper["pmid"],
                "Title": paper["title"],
                "Publication Date": paper["publication_date"],
                "Non-academic Author(s)": ", ".join(non_acad_authors),
                "Company Affiliation(s)": "; ".join(company_names),
                "Corresponding Author Email": email
            })
            # for debugging
            if debug:
                print(f"[DEBUG] Included paper: {paper['title'][:50]}... with {len(non_acad_authors)} company authors")

    return result
