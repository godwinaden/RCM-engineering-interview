from tech_stock.create_csv import StockCSV
from tech_stock.stock import Stock
from test.test_stock_object import stocks
from timer.timer import method_timer


class TestStockCSVObject:
    stock_csv = StockCSV(
        file_name="volatile_stock",
        field_names=["stock_symbol", "percentage_change", "current_price", "last_close_price"]
    )
    stock = Stock()
    stock.from_dict("GOOGL", stocks[0])

    @method_timer
    def test_method_save_as_csv_using_pandas(self):

        self.stock_csv.save_as_csv_using_pandas(data_to_save=self.stock)

        rows, cols = self.stock_csv.get_rows_columns_in_csv()
        assert rows == 1
        # The dataframe df has all 4 of the cols in the original dataset plus
        # the goal_difference col added in read_data().
        assert cols == 5

    @method_timer
    def test_method_write_row(self):
        rows, cols = self.stock_csv.get_rows_columns_in_csv()
        self.stock_csv.write_row(self.stock)
        new_rows, new_cols = self.stock_csv.get_rows_columns_in_csv()
        assert new_rows != (rows + 1)
