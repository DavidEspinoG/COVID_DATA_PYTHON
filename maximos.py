from operator import indexOf

from numpy import indices
import scripts as scr
from matplotlib import pyplot as plt
def regresa_max_contagios():
    max_contagios = 0
    lista_max_contagios = []
    
    for i in range(len(scr.INT_MATRIZ)):
        list_maximo = []
        elemento = scr.INT_MATRIZ[i][3:]
        maximo = max(elemento)
        lista_max_contagios.append(maximo)
        
    return  lista_max_contagios
    
def index_max_contagios(lista):
    fechas = scr.INT_MATRIZ[0][3:]
    lista_indices = []
    
    for i in range(len(scr.INT_MATRIZ)):
        index = scr.INT_MATRIZ[i].index(lista[i])
        lista_indices.append(index)
    return lista_indices

def fecha_max_contagio(lista_indices):
    lista_fechas = []
    for i in range(len(lista_indices)):
        elemento = scr.STRING_MATRIZ[0][lista_indices[i]]
        lista_fechas.append(elemento)       
    return lista_fechas 

def muestra_tabla_max_contagios(datos, nombre_columnas):   #datis =Matriz nombre_columna = Lista
    fig, ax = plt.subplots(figsize=(10,7))
    ax.table(cellText=datos, colLabels=nombre_columnas, loc="center")
    ax.axis('tight')
    ax.axis('off')
    plt.show()
def regresa_matriz_maximos(estados, fechas, maximos):
    matriz = []
    lista = []
    for i in range(33):
        lista = []
        lista.append(estados[i])
        lista.append(fechas[i])
        lista.append(maximos[i])
        matriz.append(lista)
    return matriz
def grafica_maximos_estado(estados, maximos):
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(estados, maximos)
    ax.grid(True)
    ax.set_title(f'Máximo de contagios por estado')
    ax.set_xlabel('Estados')
    ax.set_ylabel('Casos')
    plt.subplots_adjust(bottom=0.50)
    plt.xticks(estados, rotation= 80)
    plt.show()
