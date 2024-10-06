class User:
    def __init__ (self, username, password, xp):
        self.username = username
        self.password = password
        self.xp = xp

def add_user(username, password):
    temp = User(username, password, "0")
    with open("userdata.txt", "a") as f:
        f.write(f"{temp.username},{temp.password},{temp.xp}\n")

    return True

def login_to_acct(username, password): #CHECK IF USERNAME/PASSWORD IS IN USERDATA.TXT, if it is return true/sign in
    with open('userdata.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            user_details = line.split(",")

            if username == user_details[0]:
                if password == user_details[1]:
                    return True
                
        return False

