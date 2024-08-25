import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV dataset from the specified path and return it as a pandas
    DataFrame.

    Parameters:
    path (str): The path to the CSV file to be loaded.

    Returns:
    pd.DataFrame or None: The loaded dataset as a pandas DataFrame, or
    None if there was an error.

    This function loads a CSV dataset from the given path using the
    pandas library.
    It prints the dimensions of the loaded dataset and returns the
    dataset as a DataFrame.
    If there is an error (e.g., bad path, bad format), None is returned.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("The file doesnt exist")
        if not path.lower().endswith('.csv'):
            raise ValueError("The file fromat is not .csv")
        dataframe = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataframe.shape}")
        return dataframe
    except (FileNotFoundError, ValueError) as error:
        print(__name__ + ":", error)
        return None