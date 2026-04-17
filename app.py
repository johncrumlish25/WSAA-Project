# Flask App
# Author: John Crumlish

from os import path
from flask import Flask, jsonify, request, render_template
import sqlite3  # database

ROOT = path.dirname(path.realpath(__file__))
DB_PATH = path.join(ROOT, "database.db")

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# GET all players
@app.route('/players', methods=['GET'])
def get_players():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            goals INTEGER NOT NULL
        )
    ''')

    conn.commit() 

    cursor.execute("SELECT * FROM players")
    rows = cursor.fetchall()

    conn.close()

    players = []
    for row in rows:
        players.append({
            "id": row[0],
            "name": row[1],
            "goals": row[2]
        })

    return jsonify(players)

# ADD player
@app.route('/players', methods=['POST'])
def add_player():
    data = request.get_json(force=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # CREATE TABLE FIRST
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            goals INTEGER NOT NULL
        )
    ''')

    conn.commit() 

    cursor.execute(
        "INSERT INTO players (name, goals) VALUES (?, ?)",
        (data["name"], data["goals"])
    )

    conn.commit()

    new_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "id": new_id,
        "name": data["name"],
        "goals": data["goals"]
    })

# UPDATE player
@app.route('/players/<int:id>', methods=['PUT'])
def update_player(id):
    data = request.get_json(force=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE players SET name = ?, goals = ? WHERE id = ?",
        (data["name"], data["goals"], id)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "id": id,
        "name": data["name"],
        "goals": data["goals"]
    })

# DELETE player
@app.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM players WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Player deleted"})

if __name__ == '__main__':
    app.run(debug=True)