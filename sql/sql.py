import sqlite3

from sql.customer import Customer


class Sql:
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    def create_table_customers(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Customers
                      (CustomerID INTEGER PRIMARY KEY AUTOINCREMENT, CustomerName TEXT, 
                      ContactName TEXT, Address TEXT, 
                      City TEXT, PostalCode TEXT, Country TEXT, 
                      UNIQUE (CustomerName, ContactName, City, Country))''')
        self.connection.commit()

    def create_table_products(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Products
                              (ProductID INTEGER PRIMARY KEY AUTOINCREMENT, 
                              ProductName TEXT, SupplierID INTEGER, 
                              CategoryID INTEGER, Unit TEXT, Price REAL, 
                              UNIQUE (ProductName, SupplierID, CategoryID))''')
        self.connection.commit()

    def close(self):
        self.connection.close()

    def add_customers(self, records: list):
        for record in records:
            self.add_customer(record)

    def add_customer(self, record: dict):
        self.cursor.execute(
            '''INSERT INTO Customers 
            (CustomerName, ContactName, Address, City, PostalCode, Country) 
            VALUES (?, ?, ?, ?, ?, ?)''',
            (*(record.values()),)
        )
        self.connection.commit()

    def add_products(self, records: list):
        for record in records:
            self.add_product(record)

    def add_product(self, record: dict):
        self.cursor.execute(
            '''INSERT INTO Products 
            (ProductName, SupplierID, CategoryID, Unit, Price) 
            VALUES (?, ?, ?, ?, ?)''',
            (*(record.values()),)
        )
        self.connection.commit()

    @staticmethod
    def __to_customer(cursor: sqlite3.Cursor) -> list:
        records = []
        for row in cursor:
            records.append(Customer(
                customer_id=row[0],
                customer_name=row[1],
                contact_name=row[2],
                address=row[3],
                city=row[4],
                postal_code=row[5],
                country=row[6]
            ))
        return records

    def get_customers_from_a_country(self, country: str) -> list:
        self.cursor.execute("SELECT * FROM Customers WHERE(Country = ?)", (country,))
        return self.__to_customer(self.cursor)

    def get_customers_from_a_city(self, city: str) -> list:
        self.cursor.execute("SELECT * FROM Customers WHERE(City LIKE '%" + city + "%')")
        return self.__to_customer(self.cursor)

    def get_average_price_of_all_products(self) -> float:
        self.cursor.execute("SELECT avg(Price) FROM Products")
        return self.cursor.fetchone()[0]

    def count_all_products_with_price(self, price: float) -> int:
        self.cursor.execute("SELECT count(*) FROM Products WHERE(Price == ?)", (price,))
        return self.cursor.fetchone()[0]

    def clear_tables(self):
        self.cursor.execute("DROP TABLE Customers")
        self.cursor.execute("DROP TABLE Products")
        self.connection.commit()
