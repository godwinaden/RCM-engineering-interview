import datetime


class Stock:

    def __init__(self,
                 stock_symbol: str = 0.0,
                 current_price: float = 0.0,
                 change: float = 0.0,
                 percentage_change: float = 0.0,
                 last_close_price: float = 0.0,
                 high_price: float = 0.0,
                 low_price: float = 0.0,
                 open_price: float = 0.0,
                 date_of_transaction: int = datetime.datetime.now().timestamp(),):
        self.current_price = current_price
        self.change = change
        self.stock_symbol = stock_symbol
        self.percentage_change = percentage_change
        self.last_close_price = last_close_price
        self.high_price = high_price
        self.low_price = low_price
        self.open_price = open_price
        self.date_of_transaction = self.__convert_timestamp_to_date(date_of_transaction)

    @staticmethod
    def __convert_timestamp_to_date(the_timestamp: int) -> datetime:
        if isinstance(the_timestamp, int):
            date = datetime.datetime.fromtimestamp(the_timestamp)
            return date.strftime("%c")
        else:
            return None

    def as_dict(self):
        return {
            "stock_symbol": self.stock_symbol,
            "percentage_change": self.percentage_change,
            "current_price": self.current_price,
            "last_close_price": self.last_close_price,
        }

    def from_dict(self, symbol: str, payload: dict):
        self.current_price = payload['c']
        self.change = payload['d']
        self.stock_symbol = symbol
        self.percentage_change = payload['dp']
        self.last_close_price = payload['pc']
        self.high_price = payload['h']
        self.low_price = payload['l']
        self.open_price = payload['o']
        self.date_of_transaction = self.__convert_timestamp_to_date(payload['t'])

    def get_stock_name(self):
        if self.stock_symbol == "AAPL":
            return "Apple"
        elif self.stock_symbol == "AMZN":
            return "Amazon"
        elif self.stock_symbol == "FB":
            return "Facebook"
        elif self.stock_symbol == "GOOGL":
            return "Google"
        else:
            return "Netflix"
