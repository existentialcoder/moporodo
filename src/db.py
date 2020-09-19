import sqlite3
from sqlite3 import Error

class Database:

    __connection = None

    def __create_connection(db_file):
        if db_file is not None:
            try:
                Database.__connection = sqlite3.connect(db_file)
            except Error as e:
                print(e)

    def __close_connection():
        if Database.__connection is not None:
            Database.__connection.close()

    def connect():
        Database.__create_connection(r'pomodoro.db')

    def close():
        Database.__close_connection()

    def execute(command):
        cursor = Database.__connection.cursor()
        cursor.execute(command)
        Database.__connection.commit()

class User:

    def initialize():
        create_table_command = """
                           CREATE TABLE IF NOT EXISTS Users (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name VARCHAR NOT NULL
                           );
                           """
        Database.execute(create_table_command)

class Pomodoro:

    def initialize():
        create_table_command = """
                           CREATE TABLE IF NOT EXISTS Pomodoros (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           user_id INTEGER NOT NULL,
                           start DATE NOT NULL,
                           end DATE,
                           pauses INTEGER,
                           completed INTEGER,
                           FOREIGN KEY(user_id) REFERENCES Users(id)
                           );
                           """
        Database.execute(create_table_command)

#Usage:
#Database.connect()
#User.initialize()
#Pomodoro.initialize()
