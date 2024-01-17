import typer
from rich.console import Console
from preprocessing.text_cleaning import TextCleaning
import pandas as pd

console = Console()

app = typer.Typer()

@app.command(short_help='adds dataset')
def start():
    console.print("[bold red]Enter the dataset that should be present in the current directory[/bold red]!")
    dataset = input("")
    dataset = pd.read_csv(dataset)
    console.print(f"[bold blue]Added {dataset.head(5)}[/bold blue]")
    console.print("[bold red]Enter the column on which you want to perform preprocessing.[/bold red]")
    value = input("")
    console.print(f"")
    text_cleaning(dataset[value])

def text_cleaning(dataset: str):
    console.print(f"Text Cleaning")
    console.print("[bold yellow]Select cleaning options:[/bold yellow]")
    lowercasing = typer.confirm("Convert texts to lowercase?")
    remove_punctuation = typer.confirm("Remove punctuation from Data?")
    remove_numbers = typer.confirm("Remove numbers from Data?")
    remove_stopwords = typer.confirm("Remove stopwords from Data?")
    remove_special_chars = typer.confirm("Remove Special Character from Data?")
    remove_html_tags = typer.confirm("Remove HTML Tags from Data?")

    cleaned_text = dataset
    if lowercasing:
        cleaned_text = [TextCleaning(text).lowercasing() for text in cleaned_text]

    if remove_punctuation:
        cleaned_text = [TextCleaning(text).removing_punctuation() for text in cleaned_text]

    if remove_numbers:
        cleaned_text = [TextCleaning(text).removing_numbers() for text in cleaned_text]

    if remove_stopwords:
        cleaned_text = [TextCleaning(text).removing_stopwords() for text in cleaned_text]

    if remove_special_chars:
        cleaned_text = [TextCleaning(text).removing_special_chars() for text in cleaned_text]

    if remove_html_tags:
        cleaned_text = [TextCleaning(text).removing_html_tags() for text in cleaned_text]

    cleaned_dataset = pd.DataFrame({'text': cleaned_text})

    value = typer.confirm("Do you want to save your cleaned Dataset?")
    if value:
        file_name = input("Enter Name of File")
        cleaned_dataset.to_csv(file_name+".csv", header=False, index=False)
    else:
        return cleaned_dataset
        
if __name__ == "__main__":
    app()
