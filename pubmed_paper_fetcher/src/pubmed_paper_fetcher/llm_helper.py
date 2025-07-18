import requests
import os # Used to access environment variables like the API token

HF_TOKEN = os.getenv("HF_API_TOKEN")  # Get your Hugging Face token from environment variables

# You can switch between different models here.
# Example below uses a model fine-tuned for NLI (Natural Language Inference)
#API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
API_URL = "https://api-inference.huggingface.co/models/MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"

# Set the request headers to authorize with the Hugging Face token
headers = {"Authorization": f"Bearer {HF_TOKEN}"}


def is_industry_affiliation_llm(affiliation: str) -> bool:
    # Uses Hugging Face LLM to classify affiliation as academic or industry.
    if not affiliation:
        return False # If empty or None, it's not an industry

    payload = {
        "inputs": affiliation,  # The text you want to classify
        "parameters": {
            "candidate_labels": ["academic", "industry"]  # Two possible labels
        }
    }

    try:
        # Send the classification request to Hugging Face's inference API
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise error if request fails
        result = response.json()     # Parse JSON result

        # Get the label with the highest confidence score
        top_label = result["labels"][0]
        return top_label.lower() == "industry" # Return True only if it’s “industry”

    except Exception as e:
        # Print any errors that occur (e.g., network issues, quota errors)
        print(f"[HF LLM ERROR] {e}")
        return False
