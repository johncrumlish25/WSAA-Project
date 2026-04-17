# Flask App
# Author: John Crumlish

from flask import Flask, jsonify, request
from playerDAO import playerDAO

# Create Flask application
app = Flask(__name__)

# Confirm the server is running
@app.route('/')
def home():
    return "WSAA Project Running"

# Retreive all players (GET)
@app.route('/players')
def get_all():
    return jsonify(playerDAO.getAll())

# Create new player (POST)
@app.route('/players', methods=['POST'])
def create():
    data = request.get_json()
    player = {
        "name": data["name"],
        "goals": data["goals"]
    }
    return jsonify(playerDAO.create(player))

# Update players (PUT)
@app.route('/players/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    player = {
        "name": data["name"],
        "goals": data["goals"]
    }
    playerDAO.update(id, player)
    return jsonify({"message": "updated"})

# Delete players (DELETE)
@app.route('/players/<int:id>', methods=['DELETE'])
def delete(id):
    playerDAO.delete(id)
    return jsonify({"message": "deleted"})

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)