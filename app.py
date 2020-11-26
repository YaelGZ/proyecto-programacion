import sqlite3, Funcion
from flask import Flask, jsonify, request, render_template
from pathlib import Path

emails = []

f = Path('DataBase')
if f.exists() != True :
    Funcion.LoadDataBase("DataBase")
else:
    conn=sqlite3.connect("DataBase")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Usuarios;")
    datos=cur.fetchall()
    for i in range(0,len(datos)):
        registro=datos[i][0]
        emails.append(registro)
    conn.commit()
    conn.close()

app = Flask(__name__)

@app.route("/principal")
def login():
    return render_template("login.html")

@app.route("/registrar")    
def registrar():
    return render_template("registrar.html")

@app.route("/registroNuevo",methods=['GET'])
def registroNuevo():
    if request.args.get("email") in emails:
        return "Ya existe este correo registrado"
    else:
        Funcion.save(request.args.get("email"),request.args.get("name"),request.args.get("password"))
        return "Usuario registrado"
    
@app.route("/inicio", methods=['GET'])
def inicio():
    if request.args.get("email") in emails:
        respuesta = Funcion.init(request.args.get("email"), request.args.get("password"))
        return respuesta
    else:
        return "Este correo no ha sido registrado. Favor de verificarlo"

@app.route("/mostrar")    
def mostrar():
    conn=sqlite3.connect("DataBase")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Usuarios;")
    datos=cur.fetchall()
    print(datos)
    conn.commit()
    conn.close()
    return "Checar usuarios en la consola de Python (Esta información no debería ser visible para los usuarios)"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000,
       threaded=True, debug=True)
       
