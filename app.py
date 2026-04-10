# Flask App
# Author: John Crumlish

# Import Flask + JSON response
from flask import Flask, jsonify

# Create app
app = Flask(__name__)

# Sample data
players = [  
    {"id": 1, "name": "Lionel Messi", "goals": 800},
    {"id": 2, "name": "Cristiano Ronaldo", "goals": 850}
]

# Home route
@app.route('/')
def home():
    return "WSAA Project Running"

# API route to get all players
@app.route('/players', methods=['GET'])
def get_players():
    return jsonify(players)  # return data as JSON

# Run app
if __name__ == '__main__':
    app.run(debug=True)