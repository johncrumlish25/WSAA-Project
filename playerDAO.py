import sqlite3
from os import path

ROOT = path.dirname(path.realpath(__file__))
DB_PATH = path.join(ROOT, "database.db")

class PlayerDAO:

    def getConnection(self):
        conn = sqlite3.connect(DB_PATH)
        return conn

    def getAll(self):
    conn = self.getConnection()
    cursor = conn.cursor()

    # CREATE TABLE FIRST
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            goals INTEGER NOT NULL
        )
    ''')

    conn.commit()   # 👈 THIS LINE IS CRITICAL

    cursor.execute("SELECT * FROM players")
    results = cursor.fetchall()

    players = []
    for row in results:
        players.append({
            "id": row[0],
            "name": row[1],
            "goals": row[2]
        })

    conn.close()
    return players

    def create(self, player):
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

        cursor.execute(
            "UPDATE players SET name = ?, goals = ? WHERE id = ?",
            (player["name"], player["goals"], id)
        )

        conn.commit()
        conn.close()

    def delete(self, id):
        conn = self.getConnection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM players WHERE id = ?", (id,))
        conn.commit()
        conn.close()


playerDAO = PlayerDAO()