import db_function as dbf

def menu_show():
    s = [x[0] for x in dbf.menu_typs()]
    m = []
    for x in s:
        if x not in m:
            m.append(x)
    return m
    

menu_show() 