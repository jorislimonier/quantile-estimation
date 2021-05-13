import os
import pandas as pd
import numpy as np


class DataPrep():
    def __init__(self, file_name, sheet_name):
        self.data = self.load_data(file_name, sheet_name)
        self.width = self.get_width()
        self.results = self.get_results()

    def load_data(self, file_name, sheet_name):
        """getting data from excel file
        the data is supposed to be in the data folder"""
        cwd = os.getcwd()
        data = pd.read_excel(cwd + "/data/" + file_name,
                             sheet_name=sheet_name)
        data.columns = data.iloc[1]
        data = data.iloc[2:]
        data = data.reset_index(drop=True)
        data.columns.name = None
        data = data.convert_dtypes()
        return data

    def get_width(self):
        """get bin width as variable since all bin width are the same"""
        width = self.data["Width"][0]
        self.data = self.data.drop(columns="Width")
        return width

    def get_results(self):
        """generate repeated results from data"""
        results = np.repeat(self.data["Value"], self.data["Count"])
        return np.array(results) + (self.width / 2)
