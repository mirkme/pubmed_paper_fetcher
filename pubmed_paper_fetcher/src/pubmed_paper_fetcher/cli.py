#Typer library to easily create CLI applications
import typer

#Path for handling file paths
from pathlib import Path

#typing support for optional parameters
from typing import Optional

#custom modules: fetching, filtering, and writing logic
from pubmed_paper_fetcher import fetcher, filters, writer


"""instantiates a Typer application object
the core engine behind your command line interface and assigns it a concise help message. 
This single sentence is what users will read first when they run --help, 
so it immediately tells them the tool's purpose (“fetch and filter PubMed papers for pharma/biotech authors”). 
In other words, you're both launching the CLI framework (so Typer can register and run commands) 
and giving your program a clear one line bio that appears in the auto generated help screen, 
making the utility self explanatory and user friendly."""
app = typer.Typer(help="Filter's and fetches PubMed papers for pharma/biotech authors.")

# Define a command `get-papers-list` that users can run from the command line
@app.command("get-papers-list")
def get_papers_list(
    query: str = typer.Argument(..., help="PubMed search query"),
    file: Optional[Path] = typer.Option(None, "--file", "-f", help="Output CSV file path"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode")
):
    # Debug info if flag is enabled.
    if debug:
        typer.echo(f"[DEBUG] Query: {query}")
        if file:
            typer.echo(f"[DEBUG] Output file: {file}")

    #Fetch papers using query string
    papers = fetcher.fetch_papers(query, debug=debug)

    #Filter non-academic authors
    filtered = filters.filter_non_academic_authors(papers, debug=debug)

    #Write to CSV or print
    if file:
        writer.save_to_csv(filtered, file)
        typer.echo(f"✅ Results saved to: {file}")
    else:
        for row in filtered:
            typer.echo(row) #Print each result to the console

# If this file is run directly (not imported), run the Typer app
if __name__ == "__main__":
    app()
