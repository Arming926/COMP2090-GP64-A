class Account:
    def init(self, username, password, nickname):
        self.username = username
        self.password = password
        self.nickname = nickname
        self.group = None

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_password(self, new_pwd):
        self.password = new_pwd
    
    def check_password(self, pwd):
        return self.password == pwd

    def get_nickname(self):
        return self.nickname

    def set_group(self, group):
        self.group = group

    def get_group(self):
        return self.group

    def show_status(self):
        if self.group is None:
            return f"{self.nickname}   Still Empty..."
        else:
            return f"{self.nickname}   {self.group.get_name()}   {self.group.get_current()}/{self.__group.get_limit()}"

class User:
    def __init__(self):
        self.accounts={}

    def create_account(self, username):
        if username in self.accounts:
            print("Username", username, "already exist!")
        else:
            password = input("Please enter your user password: ")
            new_acc = Account(username, password)
            self.accounts[username] = new_acc


