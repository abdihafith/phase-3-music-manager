import sqlite3

class Artist:
    @staticmethod
    def create(name):
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO artists (name) VALUES (?)', (name,))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(artist_id):
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM artists WHERE id = ?', (artist_id,))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all():
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM artists')
        artists = cursor.fetchall()
        connection.close()
        return artists

    @staticmethod
    def get_by_id(artist_id):
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM artists WHERE id = ?', (artist_id,))
        artist = cursor.fetchone()
        connection.close()
        return artist

    @staticmethod
    def get_songs(artist_id):
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM songs WHERE artist_id = ?', (artist_id,))
        songs = cursor.fetchall()
        connection.close()
        return songs

    @staticmethod
    def search_by_name(name):
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM artists WHERE name LIKE ?', ('%' + name + '%',))
        artists = cursor.fetchall()
        connection.close()
        return artists
