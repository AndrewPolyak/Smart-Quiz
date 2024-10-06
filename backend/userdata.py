class user:
    def __init__ (self, username, password, xp):
        self.username = username
        self.password = password
        self.xp = xp
temp = user('amogus', 'sussy', "0")
balls = temp.username + ' | ' + temp.password + ' | ' + temp.xp
def add_user(username, password):
    temp = user(username, password, "0")
    with open("userdata.txt", "w") as f:
        f.write(string)
def login(username, password): #CHECK IF USERNAME/PASSWORD IS IN USERDATA.TXT, if it is return true/sign in
    #TODO

print()