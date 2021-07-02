
import sqlite3


class linkedin:
    def __init__(self):
        self.connection = sqlite3.connect("myDB.db")
        self.cursor = self.connection.cursor()
        self.username = ""

    def set_myusername(self, username):
        self.username = username

    def create_user_table(self):
        self.cursor.execute("""CREATE TABLE User (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username VARCHAR(50),
                            password VARCHAR(50),
                            fname VARCHAR(50),
                            lname VARCHAR(50),
                            about VARCHAR(500),
                            gender CHAR(1),
                            bday int,
                            joining DATE
                            );""")

    def create_conversation_table(self):
        self.cursor.execute("""CREATE TABLE Conversation (
                            sender_id INTEGER,
                            receiver_id INTEGER,
                            message_id INTEGER,
                            archived VARCHAR(1),
                            unread VARCHAR(1),
                            deleted VARCHAR(1),
                            joining DATE
                            );""")

    def create_message(self):
        self.cursor.execute("""CREATE TABLE Message (
                            message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            text VARCHAR(500),
                            joining DATE
                            );""")

    def create_skill_table(self):
        self.cursor.execute("""CREATE TABLE Skill (
                            skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            skill_name VARCHAR(100),
                            joining DATE
                            );""")

    def create_endorse_table(self):
        self.cursor.execute("""CREATE TABLE Endorse (
                            skill_id INTEGER,
                            user_id INTEGER,
                            endorsement_id INTEGER,
                            joining DATE
                            );""")

    def create_endorsement_table(self):
        self.cursor.execute("""CREATE TABLE Endorsement (
                            endorsement_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            message VARCHAR(100),
                            joining DATE
                            );""")

    def add_new_user(self, username, password, first_name, last_name, gender, bday):
        try:
            self.create_user_table()
        except:
            print("table already existed!")

        command = "INSERT INTO User (username, password, fname, lname, gender, bday) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');".format(username, password, first_name, last_name, gender, bday)
        self.cursor.execute(command)
        self.connection.commit()

    def add_new_conversation(self, sender, receiver, message_id):
        # AKA send a message
        try:
            self.create_conversation_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Conversation (sender_id, receiver_id, message_id) VALUES ('{0}', '{1}', '{2}');".format(sender, receiver, message_id)
        self.cursor.execute(command)
        self.connection.commit()

    def add_new_skill(self, user_id, skill_name):
        try:
            self.create_skill_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Skill (user_id, skill_name) VALUES ('{0}', '{1}');".format(user_id, skill_name)
        self.cursor.execute(command)
        self.connection.commit()

    def add_new_endorse(self, skill_id, user_id, endorsement_id): #should create an Endorsement first then pass its  id to this function
        try:
            self.create_endorse_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Endorse (skill_id, user_id, endorsement_id) VALUES ('{0}', '{1}', '{2}');".format(skill_id, user_id, endorsement_id)
        self.cursor.execute(command)
        self.connection.commit()

    def add_new_endorsement(self, mssg):
        try:
            self.create_endorsement_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Endorsement (message) VALUES ('{0}');".format(mssg)
        self.cursor.execute(command)
        self.connection.commit()

    def login(self, username, password):
        command = "SELECT * FROM User WHERE username = '{0}' and password = '{1}';".format(username, password)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        if len(res) == 1:
            return True
        else:
            return False

    def signup(self, username, password):
        command = "SELECT * FROM User WHERE username = '{0}' and password = '{1}';".format(username, password)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        if len(res) == 0:
            # This username is available
            command = "INSERT INTO User (username, password) VALUES ('{0}', '{1}');".format(username, password)
            self.cursor.execute(command)
            self.connection.commit()
            return True
        else:
            #This username is taken
            return False

    def get_user_information(self, username):
        command = "SELECT * FROM User WHERE username = '{0}';".format(username)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        if len(res) == 1:
            return res

    def open_conversation(self, sender_id, receiver_id):
        command = "SELECT * FROM Conversation WHERE sender_id = '{0}' and receiver_id = '{1}';".format(sender_id, receiver_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def print_user_table(self):
        self.cursor.execute("SELECT * FROM User")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

    def print_conversation_table(self):
        self.cursor.execute("SELECT * FROM Conversation")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

if __name__ == "__main__":
    l = linkedin()
    l.add_new_user("SS97", "0000", "Sam", "Stone", "M", 24)
    #l.add_new_user("JaneJason100", "1111", "Jane", "Jason", "F", 32)
    #l.print_user_table()
    #print(l.login("SS97", "0000"))
    l.signup("MBFD", "1245")
    l.print_user_table()
