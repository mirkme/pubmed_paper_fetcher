import pandas as pd                    # Used for creating and writing DataFrames (CSV files)
from pathlib import Path               # For handling file system paths in a cross-platform way
from typing import List, Dict          # For type annotations (a list of dictionaries)

def save_to_csv(data: List[Dict], file_path: Path) -> None:
    # Convert the list of dictionaries into a Pandas DataFrame
    df = pd.DataFrame(data)

    # Ensure output directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the CSV
    df.to_csv(file_path, index=False) # index=False avoids writing row numbers in the CSV
