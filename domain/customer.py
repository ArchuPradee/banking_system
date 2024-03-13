import sqlite3

class Customer:
    def __init__(self, name, email, phone_number):
        self.customer_id = None
        self.name = name
        self.email = email
        self.phone_number = phone_number

