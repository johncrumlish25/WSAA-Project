# Flask App
# Author: John Crumlish

from flask import Flask, jsonify, request
from playerDAO import playerDAO

app = Flask(__name__)

@app.route('/')
def home():
    return "WSAA Project Running"

@app.route('/players')
def get_all():
    return jsonify(playerDAO.getAll())

@app.route('/players', methods=['POST'])
def create():
    data = request.get_json()
    player = {
        "name": data["name"],
        "goals": data["goals"]
    }
    return jsonify(playerDAO.create(player))

@app.route('/players/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    player = {
        "name": data["name"],
        "goals": data["goals"]
    }
    playerDAO.update(id, player)
    return jsonify({"message": "updated"})

@app.route('/players/<int:id>', methods=['DELETE'])
def delete(id):
    playerDAO.delete(id)
    return jsonify({"message": "deleted"})

if __name__ == '__main__':
    app.run(debug=True)