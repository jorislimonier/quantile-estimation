import os
import pandas as pd
import numpy as np

class DataPrep():
    # Get quantile of n zeros
    def quantile(k):
        return 1 - 10**(-k)

    @staticmethod
    def load_data():
        # getting data from excel file
        cwd = os.getcwd()
        data = pd.read_excel(cwd + "/20201030_data.xlsx", sheet_name=1).iloc[2:,1:4]
        data.columns = data.iloc[0]
        data = data.iloc[1:]
        data = data.reset_index(drop=True)
        data.columns.name = None
        data = data.convert_dtypes()
        DataPrep.data = data

    def get_stat():
        # getting statistics from excel file
        st = pd.read_excel("20201030_data.xlsx", sheet_name=1, header=3).iloc[:1, 12:19]
        return

    def get_width():
        # get bin width as variable since all bin width are the same
        width = data["Width"][0]
        data = data.drop(columns="Width")


# results = np.repeat(data["Value"], data["Count"])
# results = np.array(results)

