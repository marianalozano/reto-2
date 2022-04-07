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
 """

import time
import tracemalloc
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control


# Funciones para la carga de datos


def loadData(ctrlr):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
   
    tracemalloc.start()

    start_time = getTime()
    start_memory = getMemory()
    loadArtists(ctrlr)
    loadAlbums(ctrlr)
    loadTracks(ctrlr)
    
   
    stop_memory = getMemory()
    stop_time = getTime()
    
    tracemalloc.stop()

    
    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)

    return delta_time, delta_memory


def loadArtists(ctrlr):
    
    spoyifyfile = cf.data_dir + 'spotify-artists-utf8-small.csv'
    input_file = csv.DictReader(open(spoyifyfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(ctrlr['model'], artist)


def loadAlbums(ctrlr):

    spoyifyfile = cf.data_dir + 'spotify-albums-utf8-small.csv'
    input_file = csv.DictReader(open(spoyifyfile, encoding='utf-8'))
    for album in input_file:
        model.addAlbum(ctrlr['model'], album)


def loadTracks(ctrlr):

    spoyifyfile = cf.data_dir + 'spotify-tracks-utf8-small.csv'
    input_file = csv.DictReader(open(spoyifyfile, encoding='utf-8'))
    for track in input_file:
        model.addTrack(ctrlr['model'], track)

def artistsSize(ctrlr):
    """
    Numero de autores cargados al catalogo
    """
    return model.artistsSize(ctrlr['model'])

def albumsSize(ctrlr):
    """
    Numero de autores cargados al catalogo
    """
    return model.albumsSize(ctrlr['model'])

def tracksSize(ctrlr):
    """
    Numero de autores cargados al catalogo
    """
    return model.tracksSize(ctrlr['model'])













def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Funciones para medir la memoria utilizada


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
