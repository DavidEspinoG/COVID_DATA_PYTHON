from matplotlib import pyplot as plt
import scripts as scr
def total_casos_estados(matriz):
    suma_estados = []
    for i in range(len(matriz)):
        estado = []
        estadosuma = []

        nombre = matriz [i][2]
        nombresincomilla = nombre.strip('"')
        estadosuma.append(nombresincomilla)

        poblacion = matriz [i][1]
        estadosuma.append(poblacion)

        elemento = matriz[i][3:-1]
        estado.append(elemento)
        listSum = sum(estado[0])
        estadosuma.append(listSum)

        porcentajeInd = round(((listSum*100) / poblacion),2)
        estadosuma.append(porcentajeInd)
        suma_estados.append(estadosuma)
    return suma_estados


        
def muestra_tabla(datos, nombre_columnas):   #datis =Matriz nombre_columna = Lista
    fig, ax = plt.subplots(figsize=(10,7))
    ax.table(cellText=datos, colLabels=nombre_columnas, loc="center")
    ax.axis('tight')
    ax.axis('off')
    ax.set_title(f'Porcentaje de contagios por población')
    plt.show()

def datos_tabla(matriz):
    columnas = ['Estado', 'Poblacion','Suma', 'Porcentaje']
    muestra_tabla(matriz, columnas)

def grafica2(x,y):
    fig, ax2 = plt.subplots(figsize=(10,7))#ancho por alto
    ax2.bar(x,y)
    plt.title('Contagios respecto a la población')
    plt.ylabel('Porcentajes')
    plt.subplots_adjust(bottom=0.25)
    plt.xticks(x,rotation=90)
    plt.show()

def datos_grafica_barras(matriz):
    estados = []
    porcentajes = []
    for i in range(len(matriz)):
        x = matriz[i][0]
        estados.append(x)
        y = matriz[i][3]
        porcentajes.append(y)

    return estados, porcentajes
