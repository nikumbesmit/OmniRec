import pandas as pd

def validate_columns (
        dataframe : pd.DataFrame,
        required_columns : list[str],
) -> None :
    
    """
    Validate all required columns
    """

    missing = set(required_columns) - set(dataframe.columns)

    if missing :
        raise ValueError(
            f'Missing required columns : {missing}'
        )