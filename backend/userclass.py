import sqlite3
from flask import Flask

class User:
    def __init__ (self, username, password, xp, level):
        self.username = username
        self.password = password
        self.xp = xp
        self.level = level



