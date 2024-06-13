# phase-3-music-manager

#Music Manager CLI Application

This CLI application allows users to manage artists, songs, and playlists in a music library. It provides functionalities such as adding and deleting artists, adding and deleting songs, creating and removing playlists, and more.

Features
Artist Management: Add new artists, delete existing artists, list all artists, view songs by a specific artist.
Song Management: Add new songs, delete existing songs, list all songs, search for songs by title.
Playlist Management: Create new playlists, delete existing playlists, add songs to playlists, remove songs from playlists, view songs in a playlist.
Interactive Menu: The application provides an interactive menu for easy navigation and usage.
Technologies Used
Python: The application is written in Python programming language.
SQLite: SQLite is used as the database to store information about artists, songs, playlists, and their relationships.
Object-Relational Mapping (ORM): ORM is utilized for interacting with the SQLite database.
Command-Line Interface (CLI): The application is accessed and operated through a command-line interface.
Setup Instructions
Clone the repository to your local machine.
Ensure you have Python and Pipenv installed.
Install the required dependencies using Pipenv.
pipenv install
Run the application using the following command:
pipenv run python main.py
Usage
Upon running the application, you will be presented with a menu listing various options.
Choose an option by entering the corresponding number.
Follow the prompts to perform actions such as adding artists, adding songs, creating playlists, etc.