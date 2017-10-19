# correlation.py    Afnan Enayet
# Trying to predict a college's exclusitivity based on factors we know

import pandas as pd
import scikit-learn as sk
import numpy as np

def extract_data(filepath: str):
    """
    extracts data at filepath into a string. Expecting a filepath to a 
    CSV file
    """
    df = pd.read_csv(filepath)
    return df


def main():
    df = extract_data(DATA_FP) 


if __name__ == "__main__":
    # constants
    DATA_FP = "/data/college_data.csv"
    main()
    
