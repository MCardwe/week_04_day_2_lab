from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"

    values = [album.title, album.genre, album.artist.id]

    results = run_sql(sql, values)

    id = results[0]['id']

    album.id = id

    return album

# def select_all():
#     artists = []

#     sql = "SELECT * FROM artists"

#     results = run_sql(sql)

#     for row in results:
#         artist = Artist(row['name'], row['id'])
#         artists.append(artist)

#     return artists

# def select(id):
#     artist = None
#     sql = "SELECT * FROM artists WHERE id = %s"
#     values = [id]

#     results = run_sql(sql, values)[0]

#     if results is not None:
#         artist = Artist(results['name'], results['id'])
#     return artist

# def delete_all():

#     sql = "DELETE FROM artists"
#     run_sql(sql)

    