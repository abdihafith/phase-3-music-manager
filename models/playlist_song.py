import sqlite3

class PlaylistSong:
    @staticmethod
    def add_song_to_playlist(playlist_id, song_id):
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO playlist_songs (playlist_id, song_id) VALUES (?, ?)', (playlist_id, song_id))
        conn.commit()
        conn.close()

    @staticmethod
    def remove_song_from_playlist(playlist_id, song_id):
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM playlist_songs WHERE playlist_id = ? AND song_id = ?', (playlist_id, song_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_songs_in_playlist(playlist_id):
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute('SELECT song_id FROM playlist_songs WHERE playlist_id = ?', (playlist_id,))
        song_ids = cursor.fetchall()
        conn.close()
        return song_ids
