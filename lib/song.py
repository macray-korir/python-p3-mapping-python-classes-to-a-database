from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album
    
    def save(self):
        query = "INSERT INTO songs (name, album) VALUES (?, ?)"
        CURSOR.execute(query, (self.name, self.album))
        CONN.commit()
    
    @classmethod
    def create_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY, name TEXT, album TEXT)''')
        CONN.commit()
    
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()

        self.id = CURSOR.lastrowid 
