class User:
    def __init__ (self, username, password, xp):
        self.username = username
        self.password = password
        self.xp = xp

def add_user(username, password):
    temp = User(username, password, "0")
    with open("userdata.txt", "w") as f:
        f.write(f"{temp.username},{temp.password},{temp.xp}\n")

    return True

def login(username, password): #CHECK IF USERNAME/PASSWORD IS IN USERDATA.TXT, if it is return true/sign in
    None
    #TODO

