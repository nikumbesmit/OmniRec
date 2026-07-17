from pathlib import Path

import pandas as pd

def load_csv(file_path : Path) -> pd.DataFrame :
    """
    Loads CSV file into Pandas Dataframe
    """

    return pd.read_csv(file_path)

