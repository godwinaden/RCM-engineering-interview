import sqlite3

from sql.customer import Customer
from sql.mock_record import mock_records


class Sql:

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    def create_table_customers(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Customers
                      (CustomerID INTEGER PRIMARY KEY AUTOINCREMENT, CustomerName TEXT, ContactName TEXT, Address TEXT, 
                      City TEXT, PostalCode TEXT, Country TEXT)''')
        self.connection.commit()
        self.connection.close()

    def add_records(self, records: list):
        for record in records:
            self.add_record(record)

    def add_record(self, record: dict):
        self.cursor.execute(
            '''INSERT INTO Customers 
            (CustomerName, ContactName, Address, City, PostalCode, Country) 
            VALUES (?, ?, ?, ?, ?, ?)''',
            (record.values())
        )
        self.connection.commit()

    @staticmethod
    def __to_customer(cursor: sqlite3.Cursor):
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

    def get_customers_from_a_country(self, country: str) -> list<Customer>:
        self.cursor.close()
        self.cursor.execute("SELECT * FROM Customers WHERE(Country = ?)", country)
        return self.__to_customer(self.cursor)

    def get_customers_from_a_city(self, city: str) -> list<Customer>:
        self.cursor.close()
        self.cursor.execute("SELECT * FROM Customers WHERE(City LIKE '%?%'")", city)
        return self.__to_customer(self.cursor)