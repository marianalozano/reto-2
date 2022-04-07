def newArtist(name):
    
    artist = {'name': "",
              "albums": None,
              "tracks": 0,
              "artist_popularity": 0,
              "followers": 0,
              "genres": None}
    artist['name'] = name
    artist['books'] = lt.newList('ARRAY_LIST', compareArtistByName)
    return artist

def addTrack(catalog, track):

    lt.addLast(catalog['tracks'], track)
    mp.put(catalog['name'], track['spotify_track_name'], track)
    artists = track['artists'].split(",")  # Se obtienen los artistas
    for artist in artists:
        addTrackArtist(catalog, artist.strip(), track)
    

def addTrackArtist(catalog, artistname, track):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    artists = catalog['authors']
    existauthor = mp.contains(artists, artistname)
    if existauthor:
        entry = mp.get(artists, artistname)
        artist = me.getValue(entry)
    else:
        artist = newArtist(artistname)
        mp.put(artists, artistname, artist)
    lt.addLast(artists['tracks'], track)
    artist['average'] += float(track['popularity'])
    totaltracks = lt.size(artist['tracks'])
    if (totaltracks > 0):
        artist['popularity'] = artist['average'] / totaltracks















        #def printArtistData(artist):
    """
  #  Imprime la información del autor seleccionado
    """
   # if artist:
   #     print('Artista encontrado: ' + artist['name'])
   #     print('Popularidad: ' + str(artist['artist_popularity']))
   #     print('Total de Albumes: ' + str(lt.size(artist['albums'])))
  #      print("Total de Tracks: " + str())
  #  else:
  #      print('No se encontro el autor.\n')