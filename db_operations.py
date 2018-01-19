import sqlite3


class MovieDatabase():

    def __init__(self, database):
        self.db = database
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title TEXT, director TEXT, year INTEGER, rating REAL)")
        self.connection.commit()


    def __del__(self):
        self.connection.close()

    def insert(self, title, director, year, rating):
        self.cursor.execute("INSERT INTO movies VALUES (NULL,?,?,?,?)", (title, director, year, rating))
        self.connection.commit()


    def view_all(self):
        self.cursor.execute("SELECT * FROM movies")
        rows = self.cursor.fetchall()
        return rows

    def search(self, title="", director="", year="", rating=""):
        self.cursor.execute("SELECT * FROM movies WHERE title=? OR director=? OR year=? OR rating=?", (title, director, year, rating))
        rows = self.cursor.fetchall()
        return rows

    def delete(self, id):
        self.cursor.execute("DELETE FROM movies WHERE id=?", (id))
        self.connection.commit()


    def update(self, id, title, director, year, rating):
        self.cursor.execute("UPDATE movies SET title=?, director=?, year=?, rating=? WHERE id=?", (title, director, year, rating, id))
        self.connection.commit()

