import sqlite3
from models.artist import Artist
from models.song import Song
from models.playlist import Playlist
from models.playlist_song import PlaylistSong
from database.setup import create_tables

def add_artist():
    name = input("Enter artist name: ")
    Artist.create(name)
    print(f"Artist '{name}' added.")

def delete_artist():
    while True:
        try:
            artist_id = int(input("Enter artist ID to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric artist ID.")
    Artist.delete(artist_id)
    print(f"Artist with ID '{artist_id}' deleted.")

def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        print(f"ID: {artist[0]}, Name: {artist[1]}")

def artist_songs():
    while True:
        try:
            artist_id = int(input("Enter artist ID to view songs: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric artist ID.")
    artist = Artist.get_by_id(artist_id)
    if artist:
        songs = Artist.get_songs(artist_id)
        for song in songs:
            print(f"ID: {song[0]}, Title: {song[1]}, Artist ID: {song[2]}")
    else:
        print(f"No artist found with ID '{artist_id}'.")

def add_song():
    title = input("Enter song title: ")
    artist_name = input("Enter artist name: ")
    artists = Artist.search_by_name(artist_name)
    if artists:
        if len(artists) == 1:
            artist_id = artists[0][0]
        else:
            print("Multiple artists found with that name:")
            for artist in artists:
                print(f"ID: {artist[0]}, Name: {artist[1]}")
            while True:
                try:
                    artist_id = int(input("Enter the artist ID: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric artist ID.")
        Song.create(title, artist_id)
        print(f"Song '{title}' added to artist with ID '{artist_id}'.")
    else:
        print(f"No artist found with name '{artist_name}'.")

def delete_song():
    while True:
        try:
            song_id = int(input("Enter song ID to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric song ID.")
    song = Song.get_by_id(song_id)
    if song:
        Song.delete(song_id)
        print(f"Song with ID '{song_id}' deleted.")
    else:
        print(f"No song found with ID '{song_id}'.")

def list_songs():
    songs = Song.get_all()
    for song in songs:
        print(f"ID: {song[0]}, Title: {song[1]}, Artist ID: {song[2]}")

def search_artist():
    name = input("Enter artist name to search: ")
    artists = Artist.search_by_name(name)
    if artists:
        for artist in artists:
            print(f"ID: {artist[0]}, Name: {artist[1]}")
    else:
        print(f"No artists found with name '{name}'.")

def search_song():
    title = input("Enter song title to search: ")
    songs = Song.search_by_title(title)
    if songs:
        for song in songs:
            print(f"ID: {song[0]}, Title: {song[1]}, Artist ID: {song[2]}")
    else:
        print(f"No songs found with title '{title}'.")

def add_playlist():
    name = input("Enter playlist name: ")
    Playlist.create(name)
    print(f"Playlist '{name}' added.")

def delete_playlist():
    while True:
        try:
            playlist_id = int(input("Enter playlist ID to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric playlist ID.")
    Playlist.delete(playlist_id)
    print(f"Playlist with ID '{playlist_id}' deleted.")

def list_playlists():
    playlists = Playlist.get_all()
    for playlist in playlists:
        print(f"ID: {playlist[0]}, Name: {playlist[1]}")

def add_song_to_playlist():
    while True:
        try:
            playlist_id = int(input("Enter playlist ID: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric playlist ID.")
    while True:
        try:
            song_id = int(input("Enter song ID: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric song ID.")
    PlaylistSong.add_song_to_playlist(playlist_id, song_id)
    print(f"Song ID '{song_id}' added to playlist ID '{playlist_id}'.")

def remove_song_from_playlist():
    while True:
        try:
            playlist_id = int(input("Enter playlist ID: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric playlist ID.")
    while True:
        try:
            song_id = int(input("Enter song ID to remove: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric song ID.")
    PlaylistSong.remove_song_from_playlist(playlist_id, song_id)
    print(f"Song ID '{song_id}' removed from playlist ID '{playlist_id}'.")

def view_playlist_songs():
    while True:
        try:
            playlist_id = int(input("Enter playlist ID to view songs: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric playlist ID.")
    song_ids = PlaylistSong.get_songs_in_playlist(playlist_id)
    if song_ids:
        print(f"Songs in Playlist ID '{playlist_id}':")
        for song_id in song_ids:
            song = Song.get_by_id(song_id[0])
            print(f"ID: {song[0]}, Title: {song[1]}")
    else:
        print(f"No songs found in Playlist ID '{playlist_id}'.")

def main():
    create_tables()
    while True:
        print("\nMenu:")
        print("1. Add Artist")
        print("2. Delete Artist")
        print("3. List Artists")
        print("4. View Artist's Songs")
        print("5. Add Song")
        print("6. Delete Song")
        print("7. List Songs")
        print("8. Search Artist")
        print("9. Search Song")
        print("10. Add Playlist")
        print("11. Delete Playlist")
        print("12. List Playlists")
        print("13. Add Song to Playlist")
        print("14. Remove Song from Playlist")
        print("15. View Playlist Songs")
        print("16. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_artist()
        elif choice == '2':
            delete_artist()
        elif choice == '3':
            list_artists()
        elif choice == '4':
            artist_songs()
        elif choice == '5':
            add_song()
        elif choice == '6':
            delete_song()
        elif choice == '7':
            list_songs()
        elif choice == '8':
            search_artist()
        elif choice == '9':
            search_song()
        elif choice == '10':
            add_playlist()
        elif choice == '11':
            delete_playlist()
        elif choice == '12':
            list_playlists()
        elif choice == '13':
            add_song_to_playlist()
        elif choice == '14':
            remove_song_from_playlist()
        elif choice == '15':
            view_playlist_songs()
        elif choice == '16':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
