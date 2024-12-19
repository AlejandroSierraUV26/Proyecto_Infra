from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS personas (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)''')
    conn.commit()
    conn.close()

@app.route("/personas", methods=["GET"])
def get_personas():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM personas")
    personas = c.fetchall()
    conn.close()
    return jsonify(personas)

@app.route("/personas", methods=["POST"])
def add_persona():
    data = request.json
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO personas (nombre, email) VALUES (?, ?)", (data["nombre"], data["email"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Persona agregada"}), 201

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
