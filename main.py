import uvicorn

from tech_stock.stock_management import StockManager


def app():
    print("Cool things ")
    stock_manager = StockManager()
    latest_prices = stock_manager.get_latest_prices()
    saved_csv = stock_manager.save_to_csv()
    print("Latest Stock Prices: ", latest_prices)
    print("Most Volatile Stock In csv: ", saved_csv)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
