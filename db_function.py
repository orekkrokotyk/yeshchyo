import sqlite3
import atexit
import asyncio

connection = sqlite3.connect('more.db', check_same_thread=False)
cursor = connection.cursor()

async def menu_typs():
    g = await cursor.execute(f"""SELECT type FROM menu""").fetchall()
    return g

def element_menu(type):
    g = cursor.execute(f"""SELECT name FROM menu WHERE type = 'drink'""").fetchall()
    return g

def e(type):
    g = cursor.execute(f"""SELECT name FROM menu WHERE type = 'noodle'""").fetchall()
    return g

def exit_handler():
    connection.close()

atexit.register(exit_handler)

print(asyncio.run(menu_typs()))