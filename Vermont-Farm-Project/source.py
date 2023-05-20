import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression


class Vermont_Farm():
    def __init__(self) -> None:
        self.w = None

    
    def process(self, cols):
        log_cols = []
        for col in cols:
            col = f"log_{col}"
            log_cols.append(col)
        return log_cols 

