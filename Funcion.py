import sqlite3

def LoadDataBase(name):
    conn=sqlite3.connect(name)
    cur=conn.cursor()
    cur.execute("CREATE TABLE Usuarios(email text primary key, name text, password text);")
    conn.commit()
    conn.close()

def save(email, name, password):
    conn=sqlite3.connect("DataBase")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Usuarios;")
    print("Se registra correctamente")
    cur.execute("INSERT INTO Usuarios(email, name, password) VALUES ('"+email+"','"+name+"','"+password+"');")
    conn.commit()
    conn.close()
    
def init(email, password):
    conn=sqlite3.connect("DataBase")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Usuarios WHERE email='"+email+"';")
    datos=cur.fetchall()
    
    print(datos)
    
    usuario = datos[0][1]
    
    if datos[0][2] == password:
        conn.commit()
        conn.close()
        return "Hola "+usuario+" :)"   
    else:
        conn.commit()
        conn.close()
        return "Contraseña incorrecta"

        
        