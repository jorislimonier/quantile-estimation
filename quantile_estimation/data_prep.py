import os
import pandas as pd
import numpy as np


class DataPrep():
    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.data = self.load_data()
        self.width = self.get_width()
        self.results = self.get_results()

    def load_data(self):
        """getting data from excel file
        the data is supposed to be in the data folder"""
        cwd = os.getcwd()
        data = pd.read_excel(cwd + "/data/" + self.file_name, sheet_name=self.sheet_name, header=None)
        self.sim_time, self.priority, _ = data.iloc[0, 0].split(" ")
        self.protocol = data.iloc[1, 0]
        data.columns = data.iloc[2]
        data = data.iloc[3:]
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