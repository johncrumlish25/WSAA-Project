# Flask App
# Author: John Crumlish

from flask import Flask, jsonify, request

# Create app
app = Flask(__name__)

# Sample data
players = [  
    {"id": 1, "name": "Lionel Messi", "goals": 900},
    {"id": 2, "name": "Cristiano Ronaldo", "goals": 950}
]

# Home route
@app.route('/')
def home():
    return "WSAA Project Running"

# API route to get all players (READ)
@app.route('/players', methods=['GET'])
def get_players():
    return jsonify(players)  # return data as JSON

# Add new player (CREATE)
@app.route('/players', methods=['POST']) 
def add_player():
    data = request.get_json()  # get data from request

    new_player = {             # player info
        "id": len(players) + 1,
        "name": data["name"],
        "goals": data["goals"]
    }

    players.append(new_player)  # add to list
    return jsonify(new_player)  # return new player

# Update players (UPDATE)
@app.route('/players/<int:id>', methods=['PUT'])  
def update_player(id):
    data = request.get_json()  # get JSON data

    for player in players:
        if player["id"] == id:
            player["name"] = data["name"]
            player["goals"] = data["goals"]
            return jsonify(player)  # return updated player

    return jsonify({"error": "Player not found"})  # if id not found

# Run app
if __name__ == '__main__':
    app.run(debug=True)