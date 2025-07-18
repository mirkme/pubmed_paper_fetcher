**PubMed Paper Fetcher – Smart Literature Search for Science and Research**
PubMed Paper Fetcher is a command line tool designed to simplify and accelerate your literature review process. Instead of manually sifting through the enormous PubMed database, this tool allows you to search for papers by keyword, identify which ones have authors affiliated with companies or the pharmaceutical industry, and export your findings into a clean CSV format. Whether you’re a researcher trying to find relevant studies, a journalist probing the intersection of science and industry, or a data scientist preparing training data for a machine learning model, this tool can help you save time and focus your efforts.

Real-world scenarios where PubMed Paper Fetcher proves useful are numerous. Suppose you are researching COVID-19 vaccine development and want to understand how much of the work is driven by private companies. Or imagine you’re working on a study to detect KOA (Knee Osteoarthritis) using AI models and want to filter papers where companies contributed to imaging datasets or model design. You might even be exploring the ethics of pharmaceutical involvement in clinical trials. With this tool, you can quickly discover which papers have non-academic affiliations, flag relevant companies, and even enhance the detection accuracy using language models like OpenAI’s GPT, Hugging Face’s models, or local LLMs via Ollama.

PubMed Paper Fetcher brings speed, structure and intelligence to your biomedical literature search. It’s especially handy when working on data-driven projects, writing a grant proposal, or conducting a deep dive into industry involvement across medical research topics.


**Features**
    *Search PubMed with Ease: Just provide a keyword (like covid vaccine, cancer immunotherapy, or even KOA detection) and the tool fetches the latest, most relevant papers directly from PubMed.

    *Filters Non-Academic Authors: Automatically detects and highlights papers that include authors from industry—like pharma companies, biotech startups, or research labs—rather than purely academic institutions.

    *LLM-Powered Filtering (Optional): If you want smarter filtering, enable LLM support to classify affiliations more intelligently using OpenAI, Hugging Face models, or local models via Ollama.

    *Outputs Ready-to-Use CSV: The results are saved in a clean CSV file with PubMed ID, title, date, non-academic authors, company names, and corresponding emails—perfect for data science workflows, reporting, or review.

    *Flexible LLM Backends: Supports OpenAI API, Hugging Face inference endpoints, or fully offline models using Ollama so you can choose your preferred LLM provider.

    *Use Cases in the Real World: Whether you're tracking vaccine trial results, investigating pharma involvement in COVID-19 publications, or identifying company-linked research in KOA (Knee Osteoarthritis) detection, this tool gives you an edge.

**Installation**
Step 1: Clone the Repository

    git clone https://github.com/your-username/pubmed_paper_fetcher.git
    cd pubmed_paper_fetcher
Step 2: Set Up Poetry (if not already installed)

    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    Then add Poetry to your system path (PowerShell):

    [Environment]::SetEnvironmentVariable("Path", $Env:Path + ";C:\Users\<YourUser>\AppData\Roaming\Python\Scripts", "User")
    💡 Close and restart your terminal to apply the path changes.

Step 3: Install Dependencies

    poetry install

Step 4: Test the CLI

    poetry run get-papers-list --help


**structure of the project**
    pubmed_paper_fetcher/
    ├── src/
    │   └── pubmed_paper_fetcher/
    │       ├── __init__.py               # Marks this as a Python package
    │       ├── cli.py                    # Command-line interface built with Typer
    │       ├── fetcher.py                # Fetches papers using the PubMed API
    │       ├── filters.py                # Filters out academic authors and detects companies
    │       ├── llm_helper.py             # uses Hugging face API to determine affiliation type
    │       ├── llm_helper_openai.py      # Uses OpenAI API to determine affiliation type
    │       ├── llm_helper_ollama.py      # Uses Ollama (local LLM) for affiliation analysis
    │       ├── writer.py                 # Exports filtered results to CSV
    ├── papers_with_ollama.csv            # Example output CSV from a sample query
    ├── poetry.lock                       # Locked dependency versions managed by Poetry
    ├── pyproject.toml                    # Project configuration and dependencies
    └── README.md                         # Documentation and usage instructions


**Usage**
After installation, you can run the tool using the CLI:

    poetry run get-papers-list "your pubmed query" --file output.csv
    
    Options
    QUERY: The PubMed search term (required)

        --file / -f: Optional output CSV file path

        --debug / -d: Print debug information while running

        --help: Show help message and available options

    Example

        poetry run get-papers-list "knee osteoarthritis" --file koa_results.csv --debug
    This will fetch papers related to knee osteoarthritis, filter for non-academic authors (like researchers from pharmaceutical companies), and save the results in koa_results.csv.



**Development Journey**
* created new directory and initializing a git   repository to track the development process
    mkdir pubmed_paper_fetcher
    cd pubmed_paper_fetcher
    git init

* installed poetry 
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

    [Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Users\Asus\AppData\Roaming\Python\Scripts", "User")

    close terminal and restart a new terminal 

    C:\Users\Asus\AppData\Roaming\Python\Scripts\poetry --version

* scaffolded the project,enabling a clean structure with a src/ layout.
    C:\Users\Asus\AppData\Roaming\Python\Scripts\poetry new --src pubmed_paper_fetcher

* access the project folder
    cd C:\Users\Asus\Desktop\pubmed_paper_fetcher\pubmed_paper_fetcher

* created a virtual environment 
    C:\Users\Asus\AppData\Roaming\Python\Scripts\poetry env use python 
    Creating virtualenv pubmed-paper-fetcher-Ic4uL52_-py3.13 in C:\Users\Asus\AppData\Local\pypoetry\Cache\virtualenvs
    Using virtualenv: C:\Users\Asus\AppData\Local\pypoetry\Cache\virtualenvs\pubmed-paper-fetcher-Ic4uL52_-py3.13


    (base) PS C:\Users\Asus\Desktop\pubmed_paper_fetcher\pubmed_paper_fetcher> C:\Users\Asus\AppData\Roaming\Python\Scripts\poetry env info --path
    C:\Users\Asus\AppData\Local\pypoetry\Cache\virtualenvs\pubmed-paper-fetcher-Ic4uL52_-py3.13

* installing dependancies
    C:\Users\Asus\AppData\Roaming\Python\Scripts\poetry add requests

    C:\Users\Asus\AppData\Roaming\Python\Scripts\poetry add pandas

    C:\Users\Asus\AppData\Roaming\Python\Scripts\poetry add typer

    C:\Users\Asus\AppData\Roaming\Python\Scripts\poetry add --group dev mypy pytest

    C:\Users\Asus\AppData\Roaming\Python\Scripts\poetry add openai

    verify if all r there in pyproject.toml 

* make files
    src/
    └── pubmed_paper_fetcher/
        ├── __init__.py
        ├── cli.py                  ← Command-line interface using Typer
        ├── fetcher.py              ← Fetch papers from PubMed API
        ├── filters.py              ← Filter non-academic authors, company affiliations
        ├── writer.py               ← Write CSV file output
        └── llm_helper.py           ← (Optional) LLM-based heuristics for better filtering


                MODULES OVERVIEW
                File	Responsibility
                fetcher.py	Interact with the PubMed API
                filters.py	Identify non-academic authors and companies
                writer.py	Convert results to CSV
                llm_helper.py	Use OpenAI LLM (optional) to help spot pharma authors
                utils.py	Small helper functions, string cleanup etc


* setting up files

    * set up cli.py file code:
        This is the entry point for your tool. It will:
            Accept --query from command line
            Optionally --file to save output
            --debug flag for extra prints
            --help support (Typer does this automatically)
        put the following in pyproject.toml:
            [tool.poetry.scripts]
            get-papers-list = "pubmed_paper_fetcher.cli:app"
        to test if cli is working:
            in a new terminal 
                cd file name 
                poetry install
                poetry run get-papers-list --help

    * set up fetcher:
        We’ll now implement logic that:
            Uses your query to call PubMed’s API
            Retrieves relevant metadata (title, publication date, authors, etc.)
            Returns that data in a structured format (like a list of dicts)
        PubMed API (Entrez from NCBI) lets you:
        Search for paper IDs using a query (esearch)
        Fetch metadata for those papers (efetch or esummary)

    * setup filter 

    * setup writer


**For LLM-based classification, I experimented with different backends**
    OpenAI: using the OPENAI_API_KEY from the OpenAI platform
    Hugging Face: adding transformers, torch, and configuring the HF_API_TOKEN
    Ollama: setting up local inference with models like gemma3 after downloading and running the Ollama application

**for using LLMs**
    * to use openai LLM 
        $env:OPENAI_API_KEY = "your-real-api-key-here"
        go to the  https://platform.openai.com/account/api-keys and login 
        Click “Create new secret key”
        Give it a name like pubmed-script
        Copy the generated key immediately (it looks like: sk-...)
        Do not share this key publicly.

    * to use hugging face LLM
        Sign up: https://huggingface.co/join
        Go to: https://huggingface.co/settings/tokens → Click New token
        Copy the token.
        poetry add transformers torch requests
        $env:HF_API_TOKEN = "your-huggingface-token-here"

    * to use models by ollama
        Go to: https://ollama.com/download
        Click the “Download for Windows” button.
        After downloading:
        Run the .msi installer
        Complete the installation
        Restart your terminal (PowerShell)
        in new terminal :ollama run gemma3    #use any model
            /set            Set session variables
            /show           Show model information
            /load <model>   Load a session or model
            /save <model>   Save your current session
            /clear          Clear session context
            /bye            Exit
            /?, /help       Help for a command
            /? shortcuts    Help for keyboard shortcuts

**publish pubmed_paper_fetcher package to TestPyPI**
cd pubmed_paper_fetcher
poetry build
poetry add --group dev twine

