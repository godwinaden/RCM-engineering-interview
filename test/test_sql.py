from sql.mock_record import mocked_customers, mocked_products
from sql.sql import Sql
from timer.timer import method_timer


class TestSql:
    sql_instance = Sql()

    @method_timer
    def test_customers_connections(self):
        self.sql_instance.create_table_customers()
        self.sql_instance.add_customers()
        self.sql_instance.cursor.execute("SELECT * FROM Customers")
        records = self.sql_instance.cursor.fetchall()
        assert len(records) == len(mocked_customers)

    @method_timer
    def test_products_connections(self):
        self.sql_instance.create_table_products()
        self.sql_instance.add_products()
        self.sql_instance.cursor.execute("SELECT * FROM Products")
        records = self.sql_instance.cursor.fetchall()
        assert len(records) == len(mocked_products)
