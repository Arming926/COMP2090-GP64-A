class User:
    def init(self, username, password, nickname):
        self.username = username
        self.password = password
        self.nickname = nickname
        self.group = None

    def get_username(self):
        return self.username

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

