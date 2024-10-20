import sqlite3

price = {'лапша': 100, 'лаврол':200, 'картошка': 275 }



def session_order(list_order, time):
    conn = sqlite3.connect('cafe_db.sql')
    cur = conn.execute('CREATE TABLE IF NOT EXISTS sessions (dish varcher(50), time varcher(50)), people varcher(50)')
    conn.commit()
    for i in list_order:
        cur.execute('INSERT INTO sessions (dish, time) VALUES ("%s", "%s")' % (i, time ))
        cur.execute('INSERT INTO sessions (dish, time) VALUES ("%s", "%s")' % (i, time ))
    cur = conn.execute('SELECT * FROM sessions')
    g = cur.fetchall()
    print(g)
    conn.commit()
    cur.close()
    conn.close()
    

def session_table():
    list_time = []
    conn = sqlite3.connect('cafe_db.sql')
    cur = conn.execute('select * FROM sessions')
    g = cur.fetchall()
    for i in range(len(g)):
        list_time.append(int(g[i][1].split(':')[0] + g[i][1].split(':')[1]))
    while list_time != []:
        cur = conn.execute(f"""SELECT * FROM sessions WHERE time = '{list(str(min(list_time)))[0] + list(str(min(list_time)))[1] + ":" + list(str(min(list_time)))[2] + list(str(min(list_time)))[3]}'""")
        g = cur.fetchall()
        list_time.remove(min(list_time))
        print(g[0])
    cur.close()
    conn.close()




session_table()
