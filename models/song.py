import sqlite3

class Song:
    @staticmethod
    def create(title, artist_id):
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO songs (title, artist_id) VALUES (?, ?)', (title, artist_id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(song_id):
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM songs WHERE id = ?', (song_id,))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all():
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM songs')
        songs = cursor.fetchall()
        connection.close()
        return songs

    @staticmethod
    def get_by_id(song_id):
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM songs WHERE id = ?', (song_id,))
        song = cursor.fetchone()
        connection.close()
        return song

    @staticmethod
    def search_by_title(title):
        connection = sqlite3.connect('music_manager.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM songs WHERE title LIKE ?', ('%' + title + '%',))
        songs = cursor.fetchall()
        connection.close()
        return songs
