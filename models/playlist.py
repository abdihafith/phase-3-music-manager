import sqlite3

class Playlist:
    @staticmethod
    def create(name):
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO playlists (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(playlist_id):
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM playlists WHERE id = ?', (playlist_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM playlists')
        playlists = cursor.fetchall()
        conn.close()
        return playlists

    @staticmethod
    def get_by_id(playlist_id):
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM playlists WHERE id = ?', (playlist_id,))
        playlist = cursor.fetchone()
        conn.close()
        return playlist
