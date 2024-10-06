class user:
    def __init__ (self, username, password, xp):
        self.username = username
        self.password = password
        self.xp = xp

def add_user(username, password):
    temp = user(username, password, 0)
    with open("userdata.txt", "w") as f:
        f.write(temp)
def login(username, password):
    #TODO