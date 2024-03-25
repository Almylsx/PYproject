import pandas as pd
import numpy as np

class DataPrepKit:
    def __init__(self, file_path, file_format):
        self.file_path = file_path
        self.file_format = file_format
        self.df = self.read_data()

    def read_data(self):
        """
        Read data from a file and return a Pandas DataFrame.
        """
        if self.file_format == 'csv':
            return pd.read_csv(self.file_path)
        elif self.file_format == 'excel':
            return pd.read_excel(self.file_path)
        elif self.file_format == 'json':
            return pd.read_json(self.file_path)
        else:
            raise ValueError(f"Unsupported file format: {self.file_format}")

    def summarize_data(self):
        """
        Print key statistical summaries of the data.
        """
        print("Data Summary:")
        print(self.df.describe())

    def handle_missing_values(self, method='mean'):
        """
        Handle missing values in the DataFrame.
        """
        if method == 'mean':
            self.df = self.df.fillna(self.df.mean())
        elif method == 'median':
            self.df = self.df.fillna(self.df.median())
        elif method == 'mode':
            self.df = self.df.fillna(self.df.mode().iloc[0])
        elif method == 'ffill':
            self.df = self.df.fillna(method='ffill')
        elif method == 'bfill':
            self.df = self.df.fillna(method='bfill')
        else:
            raise ValueError(f"Unsupported method: {method}")

    def encode_categorical_data(self):
        """
        Encode categorical data in the DataFrame.
        """
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        self.df = pd.get_dummies(self.df, columns=categorical_cols)

    def export_data(self, export_format='csv'):
        """
        Export the DataFrame to a file.
        """
        if export_format == 'csv':
            self.df.to_csv('output.csv', index=False)
        elif export_format == 'excel':
            self.df.to_excel('output.xlsx', index=False)
        elif export_format == 'json':
            self.df.to_json('output.json', orient='records')
        else:
            raise ValueError(f"Unsupported export format: {export_format}")

# Example usage
file_path = 'data.csv'
file_format = 'csv'
prep_kit = DataPrepKit(file_path, file_format)
prep_kit.summarize_data()
prep_kit.handle_missing_values(method='mean')
prep_kit.encode_categorical_data()
prep_kit.export_data()
