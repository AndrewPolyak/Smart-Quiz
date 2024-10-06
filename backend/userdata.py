from flask import Flask

class user:
    def __init__ (self, username, password, xp, level):
        self.username = username
        self.password = password
        self.xp = xp
      
users = [] #

def make_new_user(username, password, xp):
    temp = user()
    temp.username = username
    temp.password = password
    temp.xp = 0

users.append(temp)

f = open("userdata.txt", "a")
#f.write("")

#need to 
    




