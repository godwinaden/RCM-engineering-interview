import uvicorn

from sql.mock_record import mocked_customers, mocked_products
from tech_stock.stock_management import StockManager
from sql.sql import Sql


def app():
    stock_manager = StockManager()
    latest_prices = stock_manager.get_latest_prices()
    saved_csv = stock_manager.save_to_csv()
    print("Latest Stock Prices: ", latest_prices)
    print("Most Volatile Stock In csv: ", saved_csv)
    sql()


def sql():
    sql_object = Sql()
    sql_object.create_table_customers()
    sql_object.create_table_products()
    sql_object.add_customers(records=mocked_customers)
    sql_object.add_products(records=mocked_products)

    # find all customers in Berlin
    berlin_customers = sql_object.get_customers_from_a_city(city="Berlin")
    print("Customers In Berlin: ", berlin_customers)

    # find all customers in Mexico City (Country)
    mexican_customers = sql_object.get_customers_from_a_country(country="Mexico")
    print("Our Mexican Customers: ", mexican_customers)

    # find average price of all products
    average = sql_object.get_average_price_of_all_products()
    print("Average of all product prices: ", average)

    # find number of products that has price = 18
    number_of_products_priced_18 = sql_object.count_all_products_with_price(price=18)
    print("Total Number Of Products Priced At 18: ", number_of_products_priced_18)
    sql_object.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
