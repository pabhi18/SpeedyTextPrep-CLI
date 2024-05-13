import typer
from rich.console import Console
from preprocessing.text_cleaning import TextCleaning
from preprocessing.tokenize_stem_lemma import Tokenize
import pandas as pd

console = Console()

app = typer.Typer()

@app.command(short_help='adds dataset')
def start():
    console.print("[bold red]Enter the dataset![/bold red]")
    dataset = input("")
    dataset = pd.read_csv('../' + dataset)
    console.print(f"[bold blue]Added {dataset.head(5)}[/bold blue]")
    console.print("[bold red]Enter the column on which you want to perform preprocessing.[/bold red]")
    value = input("")
    console.print(f"")
    text_cleaning(dataset[value], dataset)

def text_cleaning(dataset_texts: str, dataset):
    console.print(f"Text Cleaning")
    console.print("[bold yellow]Select cleaning options:[/bold yellow]")
    lowercasing = typer.confirm("Convert texts to lowercase?")
    remove_punctuation = typer.confirm("Remove punctuation from Data?")
    remove_numbers = typer.confirm("Remove numbers from Data?")
    remove_stopwords = typer.confirm("Remove stopwords from Data?")
    remove_special_chars = typer.confirm("Remove Special Character from Data?")
    remove_html_tags = typer.confirm("Remove HTML Tags from Data?")

    cleaned_text = dataset_texts
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
    console.print("[bold green]Do you want to proceed with further steps?[/bold green]")
    value = typer.confirm("")
    if value:
        return tokenize_stem_lemma(cleaned_dataset, 'text', dataset)
    else:
        dataset['processed_texts'] = cleaned_dataset
        file_name = input("Enter Name of File (don't need to add .csv): ")
        dataset.to_csv('../'+file_name+'.csv', index=False)
        

def tokenize_stem_lemma(dataset_texts: pd.DataFrame, column_name: str, dataset):
    console.print("[bold yellow]Select steps that you want to perform further:[/bold yellow]")
    tokenization = typer.confirm("Do you want to tokenize your data?")
    stemming = typer.confirm("Do you want to Stem your data?")
    lemmatization = typer.confirm("Do you want to Lemmatize your data?")

    cleaned_text = dataset_texts[column_name].astype(str)
    if stemming:
        cleaned_text = [Tokenize(text).stemming() for text in cleaned_text]

    if lemmatization:
        cleaned_text = [Tokenize(text).lemmatization() for text in cleaned_text]

    if tokenization:
        cleaned_text = [Tokenize(text).tokenization() for text in cleaned_text]

    cleaned_dataset = pd.DataFrame(cleaned_text)

    console.print("[bold red]Completed...[/bold red]!")
    cleaned_dataset['combined'] = cleaned_dataset.apply(lambda row: row.dropna().tolist(), axis=1)
    cleaned_dataset= cleaned_dataset.drop(columns=cleaned_dataset.columns[:-1])

    dataset['processed_texts'] = cleaned_dataset
    file_name = input("Enter Name of File (don't need to add .csv): ")
    dataset.to_csv('../'+file_name+'.csv', index=False)
        
if __name__ == "__main__":
    app()
