import sqlite3
import atexit

connection = sqlite3.connect('more.db', check_same_thread=False)
cursor = connection.cursor()

def menu_typs():
    g = cursor.execute(f"""SELECT type FROM menu""").fetchall()
    return g

def exit_handler():
    connection.close()

atexit.register(exit_handler)