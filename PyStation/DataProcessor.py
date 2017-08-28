import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DataProcessor(object):
    def __init__(self):
        self.pddata = None
        self.npdata = None
        self.data = None
        self.parameter_list = None
        pass

    def __str__(self):
        if(self.data == None):
            return "This data processor is empty."
        else:
            return self.data

    def __len__(self):
        if self.parameter_list == None:
            return 0
        else:
            return len(self.parameter(list))

    def load_data(self, file_path):
        pass

    def load_csv(self, file_path):
        self.pddata = pd.read_csv(file_path)
        self.npdata = self.pddata.as_matrix()
        self.data = self.npdata.tolist()
        self.parameter_list = list(self.pddata.columns.values)

    def get_parameter_list(self):
        return self.parameter_list

    def get_column_np(self, header=None, index=None):
        assert header != None or index != None, "Please supply either a header parameter or index"
        if index != None:
            assert type(index) == type(3), "index is not an integer"
            assert index >= 0, "index is less than 0"
            assert index < len(self.parameter_list), "index is greater than parameter size"
            return self.npdata[:,index]
        if header != None:
            assert type(header) == type(""), "header must be a string"
            assert header in self.parameter_list, "header not found in parameter list.  Please review parameters"
            index = self.parameter_list.index(header)
            return self.npdata[:,index]

       
    def plot_2d(self, x, y):
        assert type(x) == type("3") or type(x) == type(3), "Please supply an integer or header string matching a parameter within the dataset for your x-axis"
        assert type(y) == type("3") or type(y) == type(3), "Please supply an integer or header string matching a parameter within the dataset for your y-axis"
        if type(x) == type("3"):
            assert x in self.parameter_list
            x = self.parameter_list.index(x)
        if type(y) == type("3"):
            assert y in self.parameter_list
            y = self.parameter_list.index(y)

        plt.plot(self.get_column_np(index=x), self.get_column_np(index=y))
        plt.show()


    def main(self):
        processor = DataProcessor()
        processor.load_csv("C:/Users/JakeT/onedrive/documents/visual studio 2017/Projects/PyStation/PyStation/static/flights/trimmed-phased-formatted.csv")
        processor.plot_2d("Time", "Altitude")

if __name__ == '__main__':
    main()