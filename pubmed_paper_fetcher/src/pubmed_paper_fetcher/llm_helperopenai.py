import os                  # For accessing environment variables
import openai              # OpenAI SDK
from openai import OpenAI  # Explicit import for creating client instances

# Initialize the OpenAI client with your API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def is_industry_affiliation_llm(affiliation: str) -> bool:
    # Uses OpenAI's ChatCompletion API to classify an affiliation as academic or industry.Returns True if it's a company/industry affiliation.
    if not affiliation:
        return False # Skip empty or null input
    
    # Prompt for GPT model to classify affiliation
    prompt = (
        f"Classify this affiliation as either 'academic' or 'industry':\n\n"
        f"{affiliation}\n\n"
        "Answer with only one word: academic or industry."
    )

    try:
        # Call OpenAI's chat completion endpoint with the prompt
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can swap this with gpt-4 if needed
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0   # Deterministic response
        )
         # Extract the model's response (first choice only)
        classification = response.choices[0].message.content.strip().lower()
        return classification == "industry"  # Return True only if classified as industry
    except Exception as e:
        # Catch and print any API/network-related errors
        print(f"[LLM ERROR] Failed to classify using LLM: {e}")
        return False
