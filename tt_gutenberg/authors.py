# tt_gutenberg/utils.py
import pandas as pd
from pathlib import Path

def load_authors_dataset(local_path="data/authors.csv",
                         remote_url="https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-07-19/authors.csv"):
    """
    Load the authors dataset. Tries local CSV first, 
    then remote URL. Raises a clear error if both fail.
    """
    # First try local
    local_file = Path(local_path)
    if local_file.exists():
        return pd.read_csv(local_file)

    # Then try remote URL
    try:
        return pd.read_csv(remote_url)
    except Exception as e:
        raise RuntimeError(
            f"Could not load authors dataset from {local_path} or {remote_url}. "
            f"Error was: {e}"
        )

def clean_alias_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean alias / author fields if needed.
    """
    # Drop NaNs
    df = df.copy()
    if 'alias' in df.columns:
        df['alias'] = df['alias'].fillna('Unknown').str.strip()
    if 'author' in df.columns:
        df['author'] = df['author'].fillna('Unknown').str.strip()
    return df
