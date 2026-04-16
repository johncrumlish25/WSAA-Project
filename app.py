# Flask App
# Author: John Crumlish

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Temporary in-memory storage
players = []

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# GET all players
@app.route('/players', methods=['GET'])
def get_players():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # create table every time (guaranteed fix)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            goals INTEGER NOT NULL
        )
    ''')

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

    # ensure table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            goals INTEGER NOT NULL
        )
    ''')

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

    for player in players:
        if player["id"] == id:
            player["name"] = data["name"]
            player["goals"] = data["goals"]
            return jsonify(player)

    return jsonify({"error": "Player not found"})

# DELETE player
@app.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    for player in players:
        if player["id"] == id:
            players.remove(player)
            return jsonify({"message": "Player deleted"})

    return jsonify({"error": "Player not found"})

if __name__ == '__main__':
    app.run(debug=True)