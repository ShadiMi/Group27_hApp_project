class user():
    def __int__(self ,uname='', mail='', pw='',prof=''):
        self.username=uname
        self.email=mail
        self.password=pw

class volunteer(user):
    def __int__(self, uname='', mail='', pw='',prof='',pts=0,vServices=None):
        super().__int__()
        self.profile=prof
        self.points=pts
        self.servicesList=vServices

class consumer(user):
    def __int__(self, uname='', mail='', pw='',prof='',pts=0,cvServices=None):
        super().__int__()
        self.profile=prof
        self.points=pts
        self.servicesList=cvServices

class admin(user):
    def __int__(self, uname='', mail='', pw='',prof='',pts=0):
        super().__int__()
        self.profile=prof
        self.points=pts

