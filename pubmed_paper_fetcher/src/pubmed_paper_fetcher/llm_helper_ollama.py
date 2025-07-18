import requests

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"  # Local API endpoint for Ollama model generation
MODEL_NAME = "gemma3"   # Specify the model to use; can be changed to llama3, mistral, etc.

def is_industry_affiliation_llm(affiliation: str) -> bool:
    # Define the prompt that will be sent to the model
    prompt = (
        f"Classify this affiliation as 'academic' or 'industry':\n\n"
        f"{affiliation}\n\n"
        f"Answer only 'academic' or 'industry'."
    )

    try:
         # Send a POST request to the Ollama API with the model and prompt
        response = requests.post(
            OLLAMA_ENDPOINT,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=30   # Optional: wait max 30 seconds
        )
        response.raise_for_status()   # Raise exception if the HTTP request failed
        result = response.json()  # Parse the returned JSON
        answer = result.get("response", "").strip().lower() # Extract the model's response and clean it
         # Print the response from the model (for debugging)
        print(f"[OLLAMA] Model response: {answer}")
        # Return True if model said "industry", else False
        return "industry" in answer
    except Exception as e:
        print(f"[OLLAMA ERROR] {e}")
        return False
