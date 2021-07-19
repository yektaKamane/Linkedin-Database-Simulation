from PyQt5 import QtCore, QtGui, QtWidgets
from main import linkedin

# The interface file

my_username = 5

class PageWindow(QtWidgets.QMainWindow): # Do not touch this
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)

class LoginPage(PageWindow):  # all the ui functions and widgets of login page sit in this class

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Login")

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(9)
        self.setFont(font)
        self.setStyleSheet("color: rgb(80, 80, 80);")
        self.commandLinkButton = QtWidgets.QCommandLinkButton("Don\'t have an account? Signup", self)
        self.commandLinkButton.setGeometry(QtCore.QRect(780, 670, 291, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("color: rgb(73, 73, 109);")
        icon = QtGui.QIcon.fromTheme("none")
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.login_button = QtWidgets.QPushButton("Login", self)
        self.login_button.setGeometry(QtCore.QRect(860, 580, 131, 41))
        self.login_button.setObjectName("login_button")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_username = QtWidgets.QLabel("Username", self)
        self.label_username.setGeometry(QtCore.QRect(810, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_username.setObjectName("label")
        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setGeometry(QtCore.QRect(800, 330, 251, 51))
        self.username_input.setObjectName("username_input")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_input.setFont(font)
        self.label_password = QtWidgets.QLabel("Password", self)
        self.label_password.setGeometry(QtCore.QRect(810, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_password.setObjectName("label_3")
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setGeometry(QtCore.QRect(800, 460, 251, 51))
        self.password_input.setObjectName("password_input")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_input.setFont(font)

        self.label_2 = QtWidgets.QLabel("Login to your account", self)
        self.label_2.setGeometry(QtCore.QRect(790, 80, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(117, 117, 176);")
        self.label_2.setObjectName("label_2")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(700, 170, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.line.setFont(font)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")


        self.commandLinkButton.clicked.connect(self.signup)
        self.login_button.clicked.connect(self.login)

    def signup(self):
        self.goto("signup")

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if linkedin_database.login(username, password):
            linkedin_database.username = username
            self.goto("main")
        else:
            # should show a message that says username or password incorrect
            pass

class SignupPage(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Signup")
        self.UiComponents()

    def UiComponents(self):

        self.signup_button = QtWidgets.QPushButton("Signup", self)
        self.signup_button.setGeometry(QtCore.QRect(860, 580, 131, 41))
        self.signup_button.setObjectName("login_button")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_username = QtWidgets.QLabel("Username", self)
        self.label_username.setGeometry(QtCore.QRect(810, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_username.setObjectName("label")
        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setGeometry(QtCore.QRect(800, 330, 251, 51))
        self.username_input.setObjectName("username_input")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_input.setFont(font)
        self.label_password = QtWidgets.QLabel("Password", self)
        self.label_password.setGeometry(QtCore.QRect(810, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_password.setObjectName("label_3")
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setGeometry(QtCore.QRect(800, 460, 251, 51))
        self.password_input.setObjectName("password_input")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_input.setFont(font)

        self.label_2 = QtWidgets.QLabel("Create an account", self)
        self.label_2.setGeometry(QtCore.QRect(810, 80, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(117, 117, 176);")
        self.label_2.setObjectName("label_2")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(700, 170, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.line.setFont(font)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.signup_button.clicked.connect(self.signup)

    def signup(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if linkedin_database.signup(username, password):
            self.goto("login")
        else:
            # should show a message that says this username is already taken
            pass


class MainPage(PageWindow):
    def __init__(self):
        super().__init__()
        self.user_id = ""
        self.username = ""
        self.password = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        self.birth_day = ""

        self.contacts = []
        self.conv = []
        self.result_of_search_mssg = []
        self.archived = []
        self.selected_contact = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Home")
        self.UiComponents()

    def get_info(self):
        info = linkedin_database.get_user_information(linkedin_database.username)
        print("info")
        print(info)
        print("-----")
        if info != None:
            self.user_id = info[0][0]
            self.username = info[0][1]
            if info[0][3] != None:
                self.first_name = info[0][3]
            if info[0][4] != None:
                self.last_name = info[0][4]

    def clearlayout(self, layout):
         if layout is not None:
             while layout.count():
                 item = layout.takeAt(0)
                 widget = item.widget()
                 if widget is not None:
                     widget.deleteLater()
                 else:
                     clearlayout(item.layout())

    def get_a_conv(self, contact_name):
        n = len(self.contacts)
        contact_id = ""
        for j in range(n):
            if self.verticalLayout_2m.itemAt(j).widget().text() == contact_name :
                contact_id = int(self.verticalLayout_2m.itemAt(j).widget().objectName())

        info = linkedin_database.get_a_conversation(self.user_id, contact_id)
        self.selected_contact = contact_id
        self.conv = info
        self.print_chat(self.conv)

    def delete_a_message(self, id):
        linkedin_database.physical_delete_a_message(int(id))
        self.conv = linkedin_database.get_a_conversation(self.user_id, self.selected_contact)
        self.print_chat(self.conv)

    def print_chat(self, chat_list):
        self.clearlayout(self.verticalLayout_2ch)
        num_of_chats = len(chat_list)
        #print(chat_list)
        for chat_index in range(num_of_chats):
            self.textBrowser_ch = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_ch)
            self.textBrowser_ch.setObjectName("textBrowser_2")
            self.del_chat_button = QtWidgets.QPushButton("Delete",self.textBrowser_ch)
            self.del_chat_button.setGeometry(QtCore.QRect(150, 0, 60, 30))
            self.del_chat_button.setObjectName(str(chat_list[chat_index][2]))
            ch_b_txt = self.del_chat_button.objectName()
            self.del_chat_button.clicked.connect(lambda ch, ch_b_txt=ch_b_txt : self.delete_a_message(ch_b_txt))
            if len(chat_list[chat_index]) >= 8:
                full_text = str(chat_list[chat_index][8])
                if chat_list[chat_index][3] == '1':
                    full_text += "\nArchived"
                else:
                    full_text += "\nUn-archived"
                if chat_list[chat_index][4] == '1':
                    full_text += "\nUnread"
                else:
                    full_text += "\nRead"
                self.textBrowser_ch.setText(full_text)
            self.verticalLayout_2ch.addWidget(self.textBrowser_ch)
            #self.verticalLayout_2ch.addWidget(self.del_chat_button)

        self.scrollArea_ch.setWidget(self.scrollAreaWidgetContents_ch)

    def send_mssg(self):
        mssg_text = self.textEdit.toPlainText()
        m = linkedin_database.add_new_message(mssg_text)
        linkedin_database.add_new_conversation(int(self.user_id), int(self.selected_contact), m)

        self.conv = linkedin_database.get_a_conversation(self.user_id, self.selected_contact)
        self.print_chat(self.conv)

    def search_mssg(self):
        if self.selected_contact != "":
            self.result_of_search_mssg = linkedin_database.search_in_messages(int(self.user_id), int(self.selected_contact), self.chat_search.text())
            self.print_chat(self.result_of_search_mssg)

    def get_contacts(self):
        info = linkedin_database.get_my_contacts(self.user_id)
        self.contacts = info

    def onChanged(self):
        filter_choice = self.comboBox.currentText()
        if filter_choice == "Archived":
            self.archived = linkedin_database.get_archived(self.user_id, self.selected_contact)
            self.print_chat(self.archived)
        elif filter_choice == "Not Archived":
            self.archived = linkedin_database.get_unarchived(self.user_id, self.selected_contact)
            self.print_chat(self.archived)
        elif filter_choice == "Read":
            pass
        elif filter_choice == "Unread":
            pass

    def make_a_post(self):
        linkedin_database.add_new_post(None, self.post_maker_input.toPlainText(), None, None, int(self.user_id))
        linkedin_database.print_post_table()
        self.post_maker_input.clear()

    def goToMain(self):
        self.goto("login")

    def UiComponents(self):
        self.backButton = QtWidgets.QPushButton("BackButton", self)
        self.backButton.setGeometry(QtCore.QRect(450, 5, 100, 20))
        self.backButton.clicked.connect(self.goToMain)

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 1780, 900))
        self.tabWidget.setObjectName("tabWidget")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(71, 71, 71);")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.tabWidget.addTab(self.home, "Home")

        self.post_holder = QtWidgets.QTextBrowser(self.home)
        self.post_holder.setGeometry(QtCore.QRect(500, 80, 600, 720))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.post_holder)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.home)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 651, 508))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        num_of_home_posts = 50
        for i in range(num_of_home_posts):
            self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
            self.textBrowser.setObjectName("textBrowser")
            self.verticalLayout_2.addWidget(self.textBrowser)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.people_you_may_know = QtWidgets.QTextBrowser(self.home)
        self.people_you_may_know.setGeometry(QtCore.QRect(1240, 80, 400, 720))
        self.verticalLayout_people = QtWidgets.QVBoxLayout(self.people_you_may_know)
        self.verticalLayout_people.setObjectName("verticalLayout")
        self.scrollArea_people = QtWidgets.QScrollArea(self.home)
        self.scrollArea_people.setWidgetResizable(True)
        self.scrollArea_people.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_people = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_people.setGeometry(QtCore.QRect(0, 0, 651, 508))
        self.scrollAreaWidgetContents_people.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2people = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_people)
        self.verticalLayout_2people.setObjectName("verticalLayout_2")

        num_of_people_you_may_know = 10
        for i in range(num_of_home_posts):
            self.textBrowser_people = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_people)
            self.textBrowser_people.setObjectName("textBrowser")
            self.verticalLayout_2people.addWidget(self.textBrowser_people)

        self.scrollArea_people.setWidget(self.scrollAreaWidgetContents_people)
        self.verticalLayout_people.addWidget(self.scrollArea_people)


        self.post_maker_input = QtWidgets.QTextEdit(self.home)
        self.post_maker_input.setGeometry(QtCore.QRect(50, 250, 331, 131))
        self.post_maker_input.setObjectName("post_maker_input")
        self.post_maker_button = QtWidgets.QPushButton("Post", self.home)
        self.post_maker_button.setGeometry(QtCore.QRect(160, 400, 93, 28))
        self.post_maker_button.setObjectName("post_maker_button")
        self.post_maker_button.setStyleSheet("color: rgb(30, 30, 30);")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.post_maker_button.setFont(font)
        self.post_maker_button.clicked.connect(self.make_a_post)

        # My network Tab
        self.my_network = QtWidgets.QWidget()
        self.my_network.setObjectName("my_network")
        self.tabWidget.addTab(self.my_network, "My Network")

        self.network_holder = QtWidgets.QTextBrowser(self.my_network)
        self.network_holder.setGeometry(QtCore.QRect(600, 80, 600, 720))
        self.verticalLayout_net = QtWidgets.QVBoxLayout(self.network_holder)
        self.verticalLayout_net.setObjectName("verticalLayout")
        self.scrollArea_net = QtWidgets.QScrollArea(self.my_network)
        self.scrollArea_net.setWidgetResizable(True)
        self.scrollArea_net.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_net = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_net.setGeometry(QtCore.QRect(0, 0, 651, 508))
        self.scrollAreaWidgetContents_net.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2net = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_net)
        self.verticalLayout_2net.setObjectName("verticalLayout_2")

        num_of_network = 10
        # All the people in my connection sit here
        for i in range(num_of_network):
            self.textBrowser_net = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_net)
            self.textBrowser_net.setObjectName("textBrowser")
            self.verticalLayout_2net.addWidget(self.textBrowser_net)

        self.scrollArea_net.setWidget(self.scrollAreaWidgetContents_net)
        self.verticalLayout_net.addWidget(self.scrollArea_net)

        self.lineEdit_search_net = QtWidgets.QLineEdit(self.my_network)
        self.lineEdit_search_net.setGeometry(QtCore.QRect(100, 231, 260, 41))
        self.lineEdit_search_net.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_search_net.setFont(font)
        self.pushButton_search_net = QtWidgets.QPushButton("Search", self.my_network)
        self.pushButton_search_net.setGeometry(QtCore.QRect(400, 230, 101, 41))
        self.pushButton_search_net.setStyleSheet("color: rgb(30, 30, 30);")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_net.setFont(font)
        self.pushButton_search_net.setObjectName("pushButton")

        self.network_holder_search = QtWidgets.QTextBrowser(self.my_network)
        self.network_holder_search.setGeometry(QtCore.QRect(100, 300, 400, 500))
        self.verticalLayout_net_search = QtWidgets.QVBoxLayout(self.network_holder_search)
        self.verticalLayout_net_search.setObjectName("verticalLayout")
        self.scrollArea_net_search = QtWidgets.QScrollArea(self.my_network)
        self.scrollArea_net_search.setWidgetResizable(True)
        self.scrollArea_net_search.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_net_search = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_net_search.setGeometry(QtCore.QRect(0, 0, 651, 508))
        self.scrollAreaWidgetContents_net_search.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2net_search = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_net_search)
        self.verticalLayout_2net_search.setObjectName("verticalLayout_2")

        num_of_network_searched = 0
        # All the people in my connection sit here
        for i in range(num_of_network_searched):
            self.textBrowser_net_search = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_net_search)
            self.textBrowser_net_search.setObjectName("textBrowser")
            self.verticalLayout_2net.addWidget(self.textBrowser_net_search)

        self.scrollArea_net_search.setWidget(self.scrollAreaWidgetContents_net_search)
        self.verticalLayout_net_search.addWidget(self.scrollArea_net_search)


        # mssging tab
        self.messaging = QtWidgets.QWidget()
        self.messaging.setObjectName("messaging")
        self.tabWidget.addTab(self.messaging, "Messaging")

        self.temp =  QtWidgets.QWidget(self.messaging)
        self.temp.setGeometry(QtCore.QRect(140, 200, 350, 400))
        self.verticalLayout_m = QtWidgets.QVBoxLayout(self.temp)
        self.verticalLayout_m.setObjectName("verticalLayout_m")
        self.verticalLayout_m.setSpacing(5)
        self.verticalLayout_m.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea_m = QtWidgets.QScrollArea(self.temp)
        self.scrollArea_m.setWidgetResizable(True)
        self.scrollArea_m.setObjectName("scrollArea_m")
        self.scrollAreaWidgetContents_m = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_m.setGeometry(QtCore.QRect(100, 100, 50, 50))
        self.scrollAreaWidgetContents_m.setObjectName("scrollAreaWidgetContents_m")
        self.verticalLayout_2m = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_m)
        self.verticalLayout_2m.setObjectName("verticalLayout_2m")
        self.verticalLayout_2m.setSpacing(5)
        self.verticalLayout_2m.setAlignment(QtCore.Qt.AlignTop)
        self.verticalLayout_2m.setContentsMargins(20, 20, 20, 20)

        num_of_contacts = len(self.contacts)
        for i in range(num_of_contacts):
            self.textBrowser_m = QtWidgets.QPushButton(self.contacts[i][0], self.scrollAreaWidgetContents_m)
            self.textBrowser_m.setObjectName(str(self.contacts[i][1]))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.textBrowser_m.setFont(font)
            text = self.textBrowser_m.text()
            self.textBrowser_m.clicked.connect(lambda ch, text=text : self.get_a_conv(text))
            self.verticalLayout_2m.addWidget(self.textBrowser_m)

        self.scrollArea_m.setWidget(self.scrollAreaWidgetContents_m)
        self.verticalLayout_m.addWidget(self.scrollArea_m)

        self.textEdit = QtWidgets.QTextEdit(self.messaging)
        self.textEdit.setGeometry(QtCore.QRect(770, 610, 421, 100))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton("Send",self.messaging)
        self.pushButton_4.setGeometry(QtCore.QRect(920, 750, 121, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.send_mssg)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(30, 30, 30);")

        self.scrollArea_ch = QtWidgets.QScrollArea(self.messaging)
        self.scrollArea_ch.setGeometry(QtCore.QRect(770, 200, 421, 400))
        self.scrollArea_ch.setWidgetResizable(True)
        self.scrollArea_ch.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_ch = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_ch.setGeometry(QtCore.QRect(0, 0, 278, 50))
        self.scrollAreaWidgetContents_ch.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2ch = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_ch)
        self.verticalLayout_2ch.setObjectName("verticalLayout_2")

        self.chat_search = QtWidgets.QLineEdit(self.messaging)
        self.chat_search.setGeometry(QtCore.QRect(780, 80, 281, 41))

        self.search_chat_button = QtWidgets.QPushButton("Search",self.messaging)
        self.search_chat_button.setGeometry(QtCore.QRect(1080, 80, 101, 41))
        self.search_chat_button.clicked.connect(self.search_mssg)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_chat_button.setFont(font)
        self.search_chat_button.setStyleSheet("color: rgb(30, 30, 30);")

        #Filtering chats
        self.label_filter = QtWidgets.QLabel("Filter your chats by : ", self.messaging)
        self.label_filter.setGeometry(QtCore.QRect(825, 154, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_filter.setFont(font)
        self.label_filter.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.messaging)
        self.comboBox.setGeometry(QtCore.QRect(1010, 150, 141, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("All")
        self.comboBox.addItem("Archived")
        self.comboBox.addItem("Not Archived")
        self.comboBox.addItem("Read")
        self.comboBox.addItem("Unread")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)

        self.comboBox.activated.connect(self.onChanged)

        # Notifications Tab
        self.notifications = QtWidgets.QWidget()
        self.notifications.setObjectName("notifications")
        self.tabWidget.addTab(self.notifications, "Notifications")

        self.editprof = QtWidgets.QWidget()
        self.editprof.setObjectName("editprof")
        self.tabWidget.addTab(self.editprof, "Profile")



        #self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)


class Window(QtWidgets.QMainWindow): # Just add the new pages to this, don't delete anything
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Modified
        self.resize(1800, 950)
        self.m_pages = {}

        # Register all the pages of app
        self.register(LoginPage(), "login")
        self.register(MainPage(), "main")
        self.register(SignupPage(), "signup")

        # Fisrt page to be
        self.goto("login")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            if name == 'main':
                # refreshing
                widget.get_info()
                widget.get_contacts()
            widget.UiComponents()
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    import sys

    linkedin_database = linkedin()
    #linkedin_database.signup("admin","admin")

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
