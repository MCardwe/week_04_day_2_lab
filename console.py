import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# artist_repository.delete_all() 

artist_1 = Artist("The Cranberries")

# artist_repository.save(artist_1)

# artist_2 = Artist("Adele")

# artist_repository.save(artist_2)

# artists = artist_repository.select_all()

# for artist in artists:
#     print(artist.__dict__)

# artist = artist_repository.select("7")

album_1 = Album("Wake Up", "rock", artist_1)

album_repository.save(album_1)



pdb.set_trace()