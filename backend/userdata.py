class user:
    def __init__ (self, username, password, xp):
        self.username = username
        self.password = password
        self.xp = xp
temp = user('amogus', 'sussy', "0")
balls = temp.username + ', ' + temp.password + ', ' + temp.xp
def add_user(username, password):
    temp = user(username, password, "0")
    with open("userdata.txt", "w") as f:
        f.write(string)
        
def login(user_input):
    '''
    Checks if username/password is in userdata.txt, if it is return true/sign in.
    '''
    # Split the input into username and password
    username, password = user_input.split(', ')
    
    try:
        # Open the userdata.txt file and read lines
        with open('userdata.txt', 'r') as file:
            for line in file:
                # Split each line into username and password
                stored_username, stored_password = line.strip().split(', ')
                
                # Check if the provided username and password match
                if username == stored_username and password == stored_password:
                    return True
        
    except FileNotFoundError:
        print("User data file not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    return False

# Example usage
user_input = "example_user, example_password"
if login(user_input):
    print("Login successful!")
else:
    print("Login failed.")


    #TODO

print()