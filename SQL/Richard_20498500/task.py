# pylint: disable missing-docstring

import sqlite3
import csv

connector = sqlite3.connect('Project.db')

cursor = connector.cursor()

#Creating the tables and then committing them to the database. Note that the Musician and Instrument tables don't have a relation table.
#This is because Musician and Instrument share no information, so I saw no need to make a relation table for them. 
musician_Table ="""CREATE TABLE Musician (
    num INTEGER,
    street TEXT,
    str_type TEXT,
    name TEXT, 
    ssn INTEGER);"""

instrument_Table = """CREATE TABLE Instrument (
    instrument_id INTEGER,
    type TEXT,
    key TEXT);"""

album_Table = """CREATE TABLE Album (
    name TEXT,
    id INTEGER,
    date INTEGER,
    type CHAR(2));
    """

instrument_album_Table = """CREATE TABLE AlbumInstrument (
    album_id INTEGER,
    instrument_id INTEGER);"""

musician_album_Table = """CREATE TABLE MusicianAlbum (
    ssn TEXT,
    album_id INTEGER);"""

cursor.execute(musician_Table)
print("Successfully created Musician table!")
cursor.execute(instrument_Table)
print("Successfully created Instrument table!")
cursor.execute(album_Table)
print("Successfully created Album table")
cursor.execute(instrument_album_Table)
print("Successfully created AlbumInstrument table!")
cursor.execute(musician_album_Table)
print("Successfully created MusicianAlbum table!")


connector.commit()


#Importing the data from the excel sheets into the database

#Starting with the Instruments table because it's easiest
file = open('instrument.csv')
contents = csv.reader(file)
insert_records = "INSERT INTO Instrument (instrument_id, type, key) VALUES(?,?,?)"
cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM Instrument"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

connector.commit()
file.close()

#Next is the Musician table
file = open('musician.csv')
contents = csv.reader(file)
insert_records = "INSERT INTO Musician (num, street, str_type, name, ssn) VALUES(?,?,?,?,?)"
cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM Musician"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

connector.commit()
file.close()

#Next is the Album table
file = open('album.csv')
contents = csv.reader(file)
insert_records = "INSERT INTO Album (name, id, date, type) VALUES(?,?,?,?)"
cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM Album"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

connector.commit()
file.close()

#Next is the AlbumInstrument table
file = open('album-instrument.csv')
contents = csv.reader(file)
insert_records = "INSERT INTO AlbumInstrument (album_id, instrument_id) VALUES(?,?)"
cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM AlbumInstrument"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

connector.commit()
file.close()

#Finally, the MusicianAlbum table
file = open('musician-album.csv')
contents = csv.reader(file)
insert_records = "INSERT INTO MusicianAlbum (ssn, album_id) VALUES(?,?)"
cursor.executemany(insert_records, contents)
select_all = "SELECT * FROM MusicianAlbum"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

connector.commit()
connector.close()
file.close()
