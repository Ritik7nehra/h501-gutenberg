# tt_gutenberg/utils.py
import pandas as pd

def load_authors_dataset(url=None):
    """
    Load the Gutenberg authors dataset from TidyTuesday.
    Default URL points to the 2025-06-03 dataset.
    """
    if url is None:
        url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/authors.csv"
    df = pd.read_csv(url)
    return df

def clean_alias_data(df):
    """
    Keep only rows with a valid alias and return cleaned DataFrame.
    """
    df = df[df['alias'].notna()].copy()
    df = df[df['alias'].str.strip() != ""]
    return df
