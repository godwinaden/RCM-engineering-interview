import pytest
from tech_stock.stock import Stock
from timer.timer import method_timer

stocks = [
    {"o": 102.3847, "c": 3302.3847, "h": 302.3847, "dp": 602.3847, "pc": 1.3847, "d": 502.3847, "l": 602.3847,
     "t": 15637488383},
    {"o": 302.3847, "c": 4302.3847, "h": 402.3847, "dp": 702.3847, "pc": 3.3847, "d": 802.3847, "l": 702.3847,
     "t": 15637488383},
    {"o": 402.3847, "c": 5302.3847, "h": 502.3847, "dp": 602.3847, "pc": 2.3847, "d": 702.3847, "l": 802.3847,
     "t": 15637488383},
    {"o": 402.3847, "c": 6302.3847, "h": 202.3847, "dp": 902.3847, "pc": 1.1847, "d": 402.3847, "l": 702.3847,
     "t": 15637488383},
]


class TestStockObject:

    @staticmethod
    @pytest.fixture
    def mock_stock_dict_data():
        return {
            "stock_symbol": "GOOGL",
            "stock": stocks[0]
        }

    def test_method_from_dict(self, mock_stock_dict_data):
        google_stock = Stock()
        assert google_stock.change == 0.0
        google_stock.from_dict(mock_stock_dict_data["stock_symbol"], mock_stock_dict_data["stock"])
        assert hasattr(google_stock, "current_price")
        assert hasattr(google_stock, "change")
        assert hasattr(google_stock, "stock_symbol")
        assert hasattr(google_stock, "percentage_change")
        assert hasattr(google_stock, "last_close_price")
        assert hasattr(google_stock, "high_price")
        assert hasattr(google_stock, "low_price")
        assert hasattr(google_stock, "open_price")
        assert hasattr(google_stock, "date_of_transaction")
        assert isinstance(google_stock.date_of_transaction, str)

    @pytest.mark.parametrize("symbol,stock", [("GOOGL", stocks[0]), ("FB", stocks[1]),
                                              ("AAPL", stocks[2]), ("AMZN", stocks[3])])
    def test_method_to_dict(self, symbol, stock):
        google_stock = Stock()
        google_stock.from_dict(symbol, stock)
        stock_dict = google_stock.as_dict()
        print("Dict: ", stock_dict)
        assert isinstance(stock_dict, dict) and stock_dict["stock_symbol"] == symbol
        assert isinstance(stock_dict["percentage_change"], float) and stock_dict["percentage_change"] == google_stock.percentage_change
        assert isinstance(stock_dict["current_price"], float) and stock_dict["current_price"] == google_stock.current_price
