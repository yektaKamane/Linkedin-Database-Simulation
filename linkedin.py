
import sqlite3

# connect withe the myTable database
# connection = sqlite3.connect("myTable.db")
# crsr = connection.cursor()
# crsr.execute("SELECT * FROM emp")
# ans = crsr.fetchall()
# print(ans)


class linkedin:
    def __init__(self):
        connection = sqlite3.connect("myDB.db")
        self.cursor = connection.cursor()

    def create_user_table(self):
        self.cursor.execute("""CREATE TABLE User (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            fname VARCHAR(50),
                            lname VARCHAR(50),
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

    def print_user_table(self):
        self.cursor.execute("SELECT * FROM User")
        table = self.cursor.fetchall()
        print(table)

if __name__ == "__main__":
    l = linkedin()
    l.initial()
    l.add_new_user('Sam', "Stone", "M", 24)
    l.add_new_user("Jane", "Jason", "F", 32)
    l.print_user_table()
