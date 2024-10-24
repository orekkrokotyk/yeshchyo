import sqlite3

price = {'лапша': 100, 'лаврол':200, 'картошка': 275 }



def session_order(list_order, time, id):
    conn = sqlite3.connect('cafe_db.sql')
    cur = conn.execute('CREATE TABLE IF NOT EXISTS sessions (dish varcher(50), time varcher(50), id varcher(50))')
    conn.commit()
    for i in list_order:
        cur.execute(f'INSERT INTO sessions (dish, time, id) VALUES ("{i}", "{time}", "{id}")')
    cur = conn.execute('SELECT * FROM sessions')
    g = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return g
    
    

def session_serch(dish, time_1, time_2):
    c = 1
    list_time = []
    help = ''
    conn = sqlite3.connect('cafe_db.sql')
    cur = conn.execute('select * FROM sessions')
    g = cur.fetchall()
    for i in range(len(g)):
        if int(g[i][1].split(':')[0] + g[i][1].split(':')[1]) >= int(time_1.split(':')[0] + time_1.split(':')[1]) and int(g[i][1].split(':')[0] + g[i][1].split(':')[1]) <= int(time_2.split(':')[0] + time_2.split(':')[1]):
            list_time.append(int(g[i][1].split(':')[0] + g[i][1].split(':')[1]))
    while list_time != []:
        cur = conn.execute(f"""SELECT * FROM sessions WHERE (time, dish) = ('{list(str(min(list_time)))[0] + list(str(min(list_time)))[1] + ":" + list(str(min(list_time)))[2] + list(str(min(list_time)))[3]}', '{dish}' )""")
        g = cur.fetchall()
        list_time.remove(min(list_time))
        help += " " + str(c) + str(g[0]) + str(len(g)- 2) + '\n' 
        c += 1
    cur.close()
    conn.close() 
    return help
    

def session_add(dish, time, id):
    conn = sqlite3.connect('cafe_db.sql')
    cur = conn.execute(f"""INSERT INTO sessions (people) VALUES ('{id}') WHERE (dish, time) = ('{dish}', '{time}')""")
    g = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    

#session_order(['лапша', 'лаврол'], '19:35', 123456789)
print(session_serch('лаврол', '17:45', '18:00'))
