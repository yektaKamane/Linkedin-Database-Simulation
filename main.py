
import sqlite3


class linkedin:
    def __init__(self):
        self.connection = sqlite3.connect("./myDB.db")
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
        self.connection.commit()

    def create_message_table(self):
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

    def add_new_message(self, text):
        try:
            self.create_message_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Message (text) VALUES ('{0}');".format(text)
        self.cursor.execute(command)
        self.connection.commit()

        command = "SELECT * FROM Message ORDER BY message_id DESC LIMIT 1;"

        self.cursor.execute(command)
        message_id = self.cursor.fetchall()
        return message_id[0][0]


    def add_new_conversation(self, sender, receiver, message_id):
        # AKA send a message
        try:
            self.create_conversation_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Conversation (sender_id, receiver_id, message_id, archived, unread, deleted) VALUES ('{0}', '{1}', '{2}', 0, 0, 0 );".format(sender, receiver, message_id)
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
        if len(res) == 1: # change this to == pls
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
        # returns mssg ids
        return res

    def get_my_contacts(self, user_id):
        command = "SELECT DISTINCT username, user_id FROM Conversation JOIN User ON Conversation.receiver_id = User.user_id WHERE sender_id = '{0}'".format(user_id)
        command += " UNION  "
        command += "SELECT DISTINCT username, user_id FROM Conversation JOIN User ON Conversation.sender_id = User.user_id WHERE receiver_id = '{0}';".format(user_id)
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def get_a_conversation(self, user_id1, user_id2):
        command = "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{0}' AND sender_id = '{1}'".format(user_id1, user_id2)
        command += " UNION "
        command += "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{1}' AND sender_id = '{0}'".format(user_id1, user_id2)
        command += " ORDER BY message_id"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def get_archived(self, user_id1, user_id2):
        command = "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{0}' AND sender_id = '{1}' AND archived = '1'".format(user_id1, user_id2)
        command += " UNION "
        command += "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{1}' AND sender_id = '{0}' AND archived = '1'".format(user_id1, user_id2)
        command += " ORDER BY message_id"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def get_unarchived(self, user_id1, user_id2):
        command = "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{0}' AND sender_id = '{1}' AND archived = '0'".format(user_id1, user_id2)
        command += " UNION "
        command += "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{1}' AND sender_id = '{0}' AND archived = '0'".format(user_id1, user_id2)
        command += " ORDER BY message_id"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def search_in_messages(self, user_id1, user_id2, message_subset):
        command = "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{0}' AND sender_id = '{1}' AND Message.text like '%{2}%'".format(user_id1, user_id2, message_subset)
        command += " UNION "
        command += "SELECT * FROM Conversation JOIN Message ON Conversation.message_id = Message.message_id WHERE receiver_id = '{1}' AND sender_id = '{0}' AND Message.text like '%{2}%'".format(user_id1, user_id2, message_subset)
        command += " ORDER BY message_id"
        self.cursor.execute(command)
        res = self.cursor.fetchall()
        return res

    def physical_delete_a_message(self, message_id):
        command = "DELETE FROM Conversation WHERE Conversation.message_id = '{0}';".format(message_id)
        self.cursor.execute(command)
        self.connection.commit()

    def print_user_table(self):
        self.cursor.execute("SELECT * FROM User")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

    def print_message_table(self):
        self.cursor.execute("SELECT * FROM Message")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

    def print_conversation_table(self):
        self.cursor.execute("SELECT * FROM Conversation")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

    #Negin start

    def create_post_table(self):
        self.cursor.execute("""CREATE TABLE Post (
                            post_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            image IMAGE,
                            caption TEXT,
                            releaseDate DATE,
                            releaseTime TIME,
                            author_id INTEGER,
                            share_id INTEGER
                            );""")


    # def create_likes_table(self):
    #     pass

    def create_comment_table(self):
        self.cursor.execute("""CREATE TABLE Comment (
                            comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            commentText VARCHAR(100),
                            releaseDate DATE,
                            releaseTime TIME
                            );""")


    def create_comment_detail_table(self):
        self.cursor.execute("""CREATE TABLE CommentDetail (
                            FOREIGN KEY (CommentPost) REFERENCES Comment(comment_id),
                            FOREIGN KEY (UserID) REFERENCES User(user_id),
                            FOREIGN KEY (PostID) REFERENCES Post(post_id)
                            );""")


    def create_reply_table(self):
        self.cursor.execute("""CREATE TABLE Reply (
                            FOREIGN KEY (CommentPost) REFERENCES Comment(comment_id),
                            text VARCHAR(150),
                            FOREIGN KEY (UserID) REFERENCES User(user_id)
                            );""")


    def create_likes_table(self):
        self.cursor.execute("""CREATE TABLE Likes (
                                    FOREIGN KEY (UserID) REFERENCES User(user_id),
                                    FOREIGN KEY (PostID) REFERENCES Post(post_id)
                                    );""")


    def show_likes(self, postid):
        command = "SELECT Likes.UserID FROM Likes WHERE Likes.PostID = postid;".format(postid)
        self.cursor.execute(command)
        # self.connection.commit()
        likes = self.cursor.fetchall()
        for record in likes:
            print(record)


    def show_comments(self):
        command = "SELECT Comment.commentText FROM Comment"
        self.cursor.execute(command)
        # self.connection.commit()
        comments = self.cursor.fetchall()
        for record in comments:
            print(record)


    def add_new_comment(self, text, postid, userid):
        command = "INSERT INTO Comment (text) VALUES ('{0}') WHERE EXISTS (SELECT * FROM CommentDetail WHERE CommentDetail.UserID = userid AND CommentDetail.PostID = postid);".format(text, userid, postid)
        self.cursor.execute(command)
        self.connection.commit()


    def share_post(self, post, user1, user2):
        pass


    def reply_comment(self, commentid, text):
        command = "INSERT INTO Reply (text) VALUES ({0}) WHERE EXISTS (SELECT Comment.comment_id from Comment WHERE Comment.comment_id = commentid);".format(text, commentid)
        self.cursor.execute(command)
        self.connection.commit()


    def add_new_post(self, image, caption, releaseDate, releaseTime, user_id):
        try:
            self.create_post_table()
        except:
            print("table already existed!")

        command = "INSERT INTO Post (image, caption, releaseDate, releaseTime, author_id) VALUES ('{0}', '{1}', '{2}', '{3}', {4});".format(image, caption, releaseDate, releaseTime, user_id)
        self.cursor.execute(command)
        self.connection.commit()

    def print_post_table(self):
        self.cursor.execute("SELECT * FROM Post")
        table = self.cursor.fetchall()
        for record in table:
            print(record)

if __name__ == "__main__":
    l = linkedin()
    #l.add_new_user("Y", "0000", "", "", "", "")
    # l.add_new_user("S", "0000", "", "", "", "")
    # l.invite()
    #l.add_new_post(None, "caption", None, None, 1)
    #l.print_post_table()
    #l.add_new_conversation("","","")
    #m1 = l.add_new_message("hi")
    #m2 = l.add_new_message("This is admin")
    #m3 = l.add_new_message("This is P")
    #l.print_message_table()
    #l.add_new_user("JaneJason100", "1111", "Jane", "Jason", "F", 32)
    #l.print_user_table()
    #print(l.login("SS97", "0000"))
    #l.signup("MBFD", "1245")
    #l.print_user_table()

    #l.add_new_conversation(2, 1, m1)
    #l.add_new_conversation(4, 1, m3)
    #l.add_new_conversation(2, 1, m2)
    #l.add_new_conversation("SS97", "Y", m3)
    #l.get_a_conversation(1,2)
    #print("---------")
    #l.print_conversation_table()
    #l.physical_delete_a_message(6)
    #l.print_conversation_table()
    #print("---------")
    #print(l.search_in_messages(1, 2, 'i'))
    #print(l.get_my_contacts(4))
    #print(l.get_a_conversation(1,4))
    #print(l.get_unarchived(1,4))
