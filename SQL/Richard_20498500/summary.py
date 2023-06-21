#pylint: disable missing-docstring

import sqlite3

connector = sqlite3.connect('Project.db')
cursor = connector.cursor()
print("Connection successful!")

#1a. A total number of musicians
output = cursor.execute("""
SELECT COUNT(*)
FROM Musician""")
output = cursor.fetchall()
print(output)

#1b. A list of musicians
output = cursor.execute("""
SELECT name
FROM Musician""")
output = cursor.fetchall()
print(output)

#2a. A total number of albums
output = cursor.execute("""
SELECT COUNT(*)
FROM Album""")
output = cursor.fetchall()
print(output)

#2b.A list of albums
output = cursor.execute("""
SELECT name
FROM Album""")
output = cursor.fetchall()
print(output)

#3a. A total number of instruments
output = cursor.execute("""
SELECT COUNT(*)
FROM Instrument""")
output = cursor.fetchall()
print(output)

#3b.A list of instruments
output = cursor.execute("""
SELECT type
FROM Instrument""")
output = cursor.fetchall()
print(output)

#4. Table of names of musicians and total number of albums written by them
output = cursor.execute(""" 
SELECT Musician.name, COUNT(*) AS count FROM Musician, MusicianAlbum, Album
WHERE MusicianAlbum.album_id = Album.id AND Musician.ssn = MusicianAlbum.ssn 
GROUP BY Musician.ssn""")
output = cursor.fetchall()
print(output)
