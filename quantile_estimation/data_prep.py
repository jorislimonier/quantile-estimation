import os
import pandas as pd
import numpy as np


class DataPrep():
    def __init__(self):
        self.data = self.load_data()
        self.stat = self.load()
        self.width = self.get_width()
        self.results = self.get_results()

    # Get quantile of n zeros
    def quantile(k):
        return 1 - 10**(-k)

    def load_data(self):
        # getting data from excel file
        cwd = os.getcwd()
        data = pd.read_excel(cwd + "/data/20201030_data.xlsx",
                             sheet_name=1).iloc[2:, 1:4]
        data.columns = data.iloc[0]
        data = data.iloc[1:]
        data = data.reset_index(drop=True)
        data.columns.name = None
        data = data.convert_dtypes()
        return data

    def load(self):
        # getting statistics from excel file
        return pd.read_excel("data/20201030_data.xlsx", sheet_name=1, header=3).iloc[:1, 12:19]

    def get_width(self):
        # get bin width as variable since all bin width are the same
        width = self.data["Width"][0]
        self.data = self.data.drop(columns="Width")
        return width

    def get_results(self):
        # generate results from data
        results = np.repeat(self.data["Value"], self.data["Count"])
        return np.array(results)


# results = np.repeat(data["Value"], data["Count"])
# results = np.array(results)
