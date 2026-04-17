import sqlite3
from os import path

# Get the directory where this file is located
ROOT = path.dirname(path.realpath(__file__))

# Create full path to the SQLite database file
DB_PATH = path.join(ROOT, "database.db")

class PlayerDAO:

    def getConnection(self):              # Connection to DB
        conn = sqlite3.connect(DB_PATH)
        return conn

    def getAll(self):                     # Retrieve all players from DB
    conn = self.getConnection()
    cursor = conn.cursor()

    # Ensure the players table exists before querying
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            goals INTEGER NOT NULL
        )
    ''')

    conn.commit()  

    cursor.execute("SELECT * FROM players")
    results = cursor.fetchall()

    players = []    # Convert rows into a list of dictionaries
    for row in results:
        players.append({
            "id": row[0],
            "name": row[1],
            "goals": row[2]
        })

    conn.close()
    return players

    def create(self, player):              # Insert a new player
        conn = self.getConnection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                goals INTEGER NOT NULL
            )
        ''')

        cursor.execute(
            "INSERT INTO players (name, goals) VALUES (?, ?)",
            (player["name"], player["goals"])
        )

        conn.commit()
        player["id"] = cursor.lastrowid
        conn.close()
        return player

    def update(self, id, player):
        conn = self.getConnection()
        cursor = conn.cursor()

        # Update player details
        cursor.execute(
            "UPDATE players SET name = ?, goals = ? WHERE id = ?",
            (player["name"], player["goals"], id)
        )

        conn.commit()
        conn.close()

    # Delete a player by ID
    def delete(self, id):
        conn = self.getConnection()
        cursor = conn.cursor()

    # Remove player
        cursor.execute("DELETE FROM players WHERE id = ?", (id,))
        conn.commit()
        conn.close()


playerDAO = PlayerDAO()