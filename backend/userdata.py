from flask import Flask
import os


class user:
    def __init__ (self, username, password, xp):
        self.username = username
        self.password = password
        self.xp = xp
      
users = [] #

# def make_new_user(username, password, xp):
#     temp = user(username, password, 0)
#     users.append(temp)

amogus = user("amongus77", "sussybaka", "0")
users.append(amogus)


with open("userdata.txt", "w") as f:
    f.write("joner boner")
    f.write(amogus.username)
    f.write(amogus.password)
    f.write(amogus.xp)

    

print('check')

#need to 
    




