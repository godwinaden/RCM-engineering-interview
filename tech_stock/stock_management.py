import requests
from requests import HTTPError

from tech_stock.create_csv import StockCSV
from tech_stock.stock import Stock


class StockManager:
    api_key = "c9iarriad3i9bpe2e7sg"
    api_url = "https://finnhub.io/api/v1"

    def __init__(self):
        try:
            self.apple = self.__get_stock('AAPL')
            self.amazon = self.__get_stock('AMZN')
            self.netflix = self.__get_stock('NFLX')
            self.facebook = self.__get_stock('FB')
            self.google = self.__get_stock('GOOGL')
        except Exception as err:
            print("An Error Occurred: ", err)

    def __get_stock(self, stock_symbol: str) -> Stock:
        try:
            url = self.api_url + "/quote"
            response = requests.get(url,
                                    params={"symbol": stock_symbol, "token": self.api_key},
                                    headers={"X-Finnhub-Token": self.api_key})
            response.raise_for_status()
        except HTTPError as http_err:
            print("HTTP error occurred: ", http_err)
        except Exception as er:
            print("Error: ", er)
        else:
            stock = Stock()
            stock.from_dict(symbol=stock_symbol, payload=response.json())
            return stock

    def get_latest_prices(self):
        return {
            "Apple": self.apple.current_price,
            "Amazon": self.amazon.current_price,
            "Facebook": self.facebook.current_price,
            "Google": self.google.current_price,
            "Netflix": self.netflix.current_price,
        }

    def get_percent_changes(self):
        return {
            "Apple": self.apple.percentage_change,
            "Amazon": self.amazon.percentage_change,
            "Facebook": self.facebook.percentage_change,
            "Google": self.google.percentage_change,
            "Netflix": self.netflix.percentage_change,
        }

    def get_stock(self, stock_name: str) -> Stock:
        if stock_name == "Apple":
            return self.apple
        elif stock_name == "Amazon":
            return self.amazon
        elif stock_name == "Facebook":
            return self.facebook
        elif stock_name == "Google":
            return self.google
        else:
            return self.netflix

    def get_most_volatile_stock(self) -> Stock:
        most_volatile_stock = Stock()
        percentage_changes = self.get_percent_changes()
        highest_percent = list(percentage_changes.values())[0]
        for key in percentage_changes:
            if percentage_changes[key] > highest_percent:
                highest_percent = percentage_changes[key]
                most_volatile_stock = self.get_stock(key)
        return most_volatile_stock

    def save_to_csv(self):
        try:
            most_volatile_stock = self.get_most_volatile_stock()
            stock_csv = StockCSV(file_name="most_volatile_stock",
                                 field_names=["stock_symbol", "percentage_change", "current_price", "last_close_price"])
            stock_csv.write_row(row_data=most_volatile_stock)
            print("CSV: ", stock_csv)
            return {
                "stock_name": most_volatile_stock.get_stock_name(),
                "percentage_change": most_volatile_stock.percentage_change,
                "csv_file_path": stock_csv.file_path
            }
        except Exception as err:
            print("Could not write row to csv: ", err)
