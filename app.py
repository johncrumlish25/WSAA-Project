# Flask App
# Author: John Crumlish

import os
from flask import Flask, jsonify, request, render_template
import sqlite3  # database

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def init_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute('''   
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            goals INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# create app
app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('index.html')

# get players from DB (READ)
@app.route('/players', methods=['GET'])  
def get_players():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)  # connect DB
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players")  # query table
    rows = cursor.fetchall() # fetch all results

    conn.close() # close connection

    players = []  # convert to JSON
    for row in rows:
        players.append({
            "id": row[0],
            "name": row[1],
            "goals": row[2]
        })

    return jsonify(players) # return JSON response

# add new player to DB (CREATE)
@app.route('/players', methods=['POST'])
def add_player():
    data = request.get_json()  # get JSON data

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)  # connect DB
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO players (name, goals) VALUES (?, ?)",  # insert player
        (data["name"], data["goals"])
    )

    conn.commit()  # save changes

    new_id = cursor.lastrowid  # get new ID

    conn.close()  # close DB

    return jsonify({
        "id": new_id,
        "name": data["name"],
        "goals": data["goals"]
    })

# update player in DB (UPDATE)
@app.route('/players/<int:id>', methods=['PUT'])
def update_player(id):
    data = request.get_json()  # get JSON data

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)  # connect DB
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE players SET name = ?, goals = ? WHERE id = ?",
        (data["name"], data["goals"], id)
    )

    conn.commit()  # save changes

    conn.close()  # close DB

    return jsonify({  # return updated player data
        "id": id,
        "name": data["name"],
        "goals": data["goals"]
    })

# delete player (DELETE)
@app.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)  # connect DB
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM players WHERE id = ?",  # delete row
        (id,)
    )

    conn.commit()  # save changes

    conn.close()  # close DB

    return jsonify({"message": "Player deleted"})  # confirmation

# run app
init_db()  # create database when app starts

if __name__ == '__main__':
    app.run(debug=True)