class user():
    def __int__(self,uname,mail,pw):
        self.username=uname
        self.email=mail
        self.password=pw

class volunteer(user):
    def __int__(self, uname, mail, pw,prof,pts):
        super().__int__()
        self.profile=prof
        self.points=pts

class consumer(user):
    def __int__(self, uname, mail, pw,prof,pts):
        super().__int__()
        self.profile=prof
        self.points=pts

class admin(user):
    def __int__(self, uname, mail, pw,prof,pts):
        super().__int__()
        self.profile=prof
        self.points=pts

