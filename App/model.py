"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

def newCatalog():

    catalog = {'artists': None,
               'albums': None,
               'tracks': None}
    

    catalog['artists'] = lt.newList('ARRAY_LIST', compareArtistsByName)

    catalog['albums'] = mp.newMap(comparefunction=compareAlbumsByName)

    catalog['tracks'] = mp.newMap(comparefunction=compareTracksByName)



def compareArtistsByName(keyname, artist):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    artistentry = me.getKey(artist)
    if (keyname == artistentry):
        return 0
    elif (keyname > artistentry):
        return 1
    else:
        return -1

def compareTracksByName (keyname, track):
    trackentry = me.getKey(track)
    if (keyname == trackentry):
        return 0
    elif (keyname > trackentry):
        return 1
    else:
        return -1

def compareAlbumsByName (keyname, album):
    albumentry = me.getKey(album)
    if (keyname == albumentry):
        return 0
    elif (keyname > albumentry):
        return 1
    else:
        return -1

def addArtist(catalog, artist):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['artists'], artist)
    mp.put(catalog['artist'], artist['spotify_artist_id'], artist)
    artists = artist['artists'].split(",")  # Se obtienen los autores
    for artist in artists:
        addArtist(catalog, artist.strip(), artist)

def addAlbum(catalog, album):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['albums'], album)
    mp.put(catalog['album'], album['spotify_album_id'], album)
    albums = album['albums'].split(",")  # Se obtienen los autores
    for album in albums:
        addAlbum(catalog, album.strip(), album)

def addTrack(catalog, track):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['albums'], track)
    mp.put(catalog['album'], track['spotify_track_id'], track)
    tracks = track['albums'].split(",")  # Se obtienen los autores
    for track in tracks:
        addTrack(catalog, track.strip(), track)

def artistsSize(catalog):

    return mp.size(catalog['artists'])

def albumsSize(catalog):

    return mp.size(catalog['albums'])

def tracksSize(catalog):

    return mp.size(catalog['tracks'])