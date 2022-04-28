import csv
import os
import sys
import pandas as pd
from tech_stock.stock import Stock


class StockCSV(object):

    def __init__(self, file_name: str, field_names: list):
        self.file_name = file_name
        self.file_path = os.path.abspath("csv/" + self.file_name + '.csv')
        self.field_names = field_names
        self.writer = self.create(self.file_path, self.field_names)

    @staticmethod
    def create(file_path: str, field_names: list) -> csv.DictWriter:
        try:
            csv_file = open(file_path, "w", newline='')
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            return writer
        except csv.Error as e:
            sys.exit('file {}, Error {}'.format(file_path, e))

    def write_row(self, row_data: Stock):
        if isinstance(row_data, Stock):
            try:
                self.writer.writerow(row_data.as_dict())
            except csv.Error as e:
                sys.exit('Operation {}, Error {}'.format('write_row', e))

    @staticmethod
    def __use_pandas(data_to_save: Stock):
        stock_dict = data_to_save.as_dict()
        stock_dict["stock_symbol"] = [stock_dict["stock_symbol"]]
        stock_dict["percentage_change"] = [stock_dict["percentage_change"]]
        stock_dict["current_price"] = [stock_dict["current_price"]]
        stock_dict["last_close_price"] = [stock_dict["last_close_price"]]
        return pd.DataFrame(stock_dict)

    def save_as_csv_using_pandas(self, data_to_save: Stock):
        try:
            pandas_dataframe = self.__use_pandas(data_to_save)
            pandas_dataframe.to_csv(self.file_path)
        except csv.Error as e:
            sys.exit('Operation {}, Error {}'.format('close', e))

    def get_rows_columns_in_csv(self):
        data_frame = pd.read_csv(self.file_path)
        rows, cols = data_frame.shape
        return rows, cols
