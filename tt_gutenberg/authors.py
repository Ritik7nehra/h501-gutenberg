# tt_gutenberg/authors.py
from typing import List

def _get_df():
    # import inside helper so imports are local and don't trigger cycles
    from .utils import load_authors_dataset, clean_alias_data
    df = load_authors_dataset()
    return clean_alias_data(df)

def list_authors(by_languages: bool = True, alias: bool = True) -> List[str]:
    df = _get_df()
    count_col = 'translations' if by_languages else 'books'
    if count_col not in df.columns:
        trans_cols = [c for c in df.columns if 'trans' in c.lower()]
        if not trans_cols:
            raise ValueError("No translation count column found.")
        count_col = trans_cols[0]

    group_field = 'alias' if alias else 'author'
    if group_field not in df.columns:
        raise ValueError(f"No column '{group_field}' in dataset.")

    counts = df.groupby(group_field)[count_col].sum().sort_values(ascending=False)
    return counts.index.tolist()
