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
        self.login_button = QtWidgets.QPushButton("Login", self)
        self.login_button.setGeometry(QtCore.QRect(350, 320, 93, 28))
        self.login_button.setObjectName("login_button")
        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setGeometry(QtCore.QRect(340, 220, 113, 22))
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setGeometry(QtCore.QRect(340, 260, 113, 22))
        self.password_input.setObjectName("password_input")
        self.signup_button = QtWidgets.QPushButton("Don't have an account? Signup", self)
        self.signup_button.setGeometry(QtCore.QRect(280, 370, 230, 28))


        self.signup_button.clicked.connect(self.signup)
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
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.signup_button = QtWidgets.QPushButton("Sign Up", self)
        self.signup_button.setGeometry(QtCore.QRect(350, 320, 93, 28))
        self.signup_button.setObjectName("signup_button")
        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setGeometry(QtCore.QRect(340, 220, 113, 22))
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setGeometry(QtCore.QRect(340, 260, 113, 22))
        self.password_input.setObjectName("password_input")

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
        self.username = ""
        self.password = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        self.birth_day = ""
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
            self.username = info[0][1]
            if info[0][3] != None:
                self.first_name = info[0][3]
            if info[0][4] != None:
                self.last_name = info[0][4]

    def goToMain(self):
        self.goto("login")

    def UiComponents(self):
        self.backButton = QtWidgets.QPushButton("BackButton", self)
        self.backButton.setGeometry(QtCore.QRect(450, 5, 100, 20))
        self.backButton.clicked.connect(self.goToMain)

        #Form.setObjectName("Form")
        #Form.resize(692, 572)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.tabWidget.addTab(self.home, "Home")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.home)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 651, 508))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        n = 50
        for i in range(n):
            self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
            self.textBrowser.setObjectName("textBrowser")
            self.verticalLayout_2.addWidget(self.textBrowser)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        # self.label = QtWidgets.QLabel(self.home)
        # self.label.setGeometry(QtCore.QRect(50, 80, 55, 50))
        # self.label.setObjectName("label")
        # self.label.setText("Welcome \n" + self.first_name)

        self.my_network = QtWidgets.QWidget()
        self.my_network.setObjectName("my_network")
        self.tabWidget.addTab(self.my_network, "My Network")


        self.messaging = QtWidgets.QWidget()
        self.messaging.setObjectName("messaging")
        self.tabWidget.addTab(self.messaging, "Messaging")

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
        self.resize(800, 600)
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
                widget.get_info()
            widget.UiComponents()
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    import sys

    linkedin_database = linkedin()
    linkedin_database.add_new_user("","","","","","")

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
