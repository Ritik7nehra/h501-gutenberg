# tt_gutenberg/authors.py
import pandas as pd
from .utils import load_authors_dataset, clean_alias_data

def list_authors(by_languages=True, alias=True):
    """
    Return a list of author aliases ordered by translation count (descending).
    by_languages=True: use translation count column.
    alias=True: return alias column rather than main author name.
    """

    # Load and clean
    df = load_authors_dataset()
    df = clean_alias_data(df)

    # Pick which column to count. 
    count_col = 'translations' if by_languages else 'books'

    if count_col not in df.columns:
        # fallback if column name differs
        count_col = [c for c in df.columns if 'trans' in c.lower()][0]

    # Group by alias or author
    group_field = 'alias' if alias else 'author'

    counts = (
        df.groupby(group_field)[count_col]
        .sum()
        .sort_values(ascending=False)
    )

    return counts.index.tolist()
