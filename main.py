
import sqlite3


class linkedin:
    def __init__(self):
        self.connection = sqlite3.connect("myDB.db")
        self.cursor = self.connection.cursor()

    def create_user_table(self):
        self.cursor.execute("""CREATE TABLE User (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            password VARCHAR(50),
                            fname VARCHAR(50),
                            lname VARCHAR(50),
                            about VARCHAR(500),
                            gender CHAR(1),
                            age int,
                            joining DATE
                            );""")

    def initial(self):
        try:
            self.create_user_table()
        except:
            print("table already existed!")

    def add_new_user(self, first_name, last_name, gender, age):
        command = "INSERT INTO User (fname, lname, gender, age) VALUES ('{0}', '{1}', '{2}', '{3}');".format(first_name, last_name, gender, age)
        self.cursor.execute(command)
        self.connection.commit() # to save changes

    def print_user_table(self):
        self.cursor.execute("SELECT * FROM User")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

if __name__ == "__main__":
    l = linkedin()
    l.initial()
    l.add_new_user('Sam', "Stone", "M", 24)
    l.add_new_user("Jane", "Jason", "F", 32)
    l.print_user_table()
