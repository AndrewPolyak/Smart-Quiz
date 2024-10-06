# 1
# 2
# 3
# 4
# 5

def make_new_user(username, password, exp) -> dict:
    user = {
        "username": username,
        "password": password,
        "exp": exp
    }
    return user

def main() -> None:
    a = "poopyhead"
    b = "test123"
    c = 21
    make_new_user(a, b, c)