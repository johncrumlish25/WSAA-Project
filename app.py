# Flask App
# Author: John Crumlish

from flask import Flask, jsonify, request
import sqlite3  # database

def init_db():
    conn = sqlite3.connect('database.db')  # create/connect DB
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

# sample data
players = [  
    {"id": 1, "name": "Lionel Messi", "goals": 900},
    {"id": 2, "name": "Cristiano Ronaldo", "goals": 950}
]

# home route
@app.route('/')
def home():
    return "Project Running"

# API route to get all players (READ)
@app.route('/players', methods=['GET'])
def get_players():
    return jsonify(players)  # return data as JSON

# add new player (CREATE)
@app.route('/players', methods=['POST']) 
def add_player():
    data = request.get_json()  # get data from request

    new_player = {             # new player data
        "id": len(players) + 1,
        "name": data["name"],
        "goals": data["goals"]
    }

    players.append(new_player)  # add to list
    return jsonify(new_player)  # return new player

# update player (UPDATE)
@app.route('/players/<int:id>', methods=['PUT'])  
def update_player(id):
    data = request.get_json()  # get JSON data

    for player in players:
        if player["id"] == id:
            player["name"] = data["name"]
            player["goals"] = data["goals"]
            return jsonify(player)  # return updated player

    return jsonify({"error": "Player not found"})  # if ID not found

# delete player (DELETE)
@app.route('/players/<int:id>', methods=['DELETE']) 
def delete_player(id):
    for player in players:
        if player["id"] == id:
            players.remove(player)  # remove player
            return jsonify({"message": "Player deleted"})

    return jsonify({"error": "Player not found"}) # if ID not found

# run app
if __name__ == '__main__':
    init_db()  # create table if not exists
    app.run(debug=True)