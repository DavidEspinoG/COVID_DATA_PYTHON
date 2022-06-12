from matplotlib import pyplot as plt
import scripts as scr
def total_casos_estados(matriz):
    suma_estados = []
    for i in range(len(matriz)):
        estado = []
        estado_suma = []

        nombre = matriz [i][2]
        nombres_sin_comilla = nombre.strip('"')
        estado_suma.append(nombres_sin_comilla)

        poblacion = matriz [i][1]
        estado_suma.append(poblacion)

        elemento = matriz[i][3:-1]
        estado.append(elemento)
        list_sum = sum(estado[0])
        estado_suma.append(list_sum)

        porcentaje_ind = round(((list_sum*100) / poblacion),2)
        estado_suma.append(porcentaje_ind)
        suma_estados.append(estado_suma)
    return suma_estados


        
def muestra_tabla(datos, nombre_columnas):   #datis =Matriz nombre_columna = Lista
    fig, ax = plt.subplots(figsize=(10,7))
    ax.table(cellText=datos, colLabels=nombre_columnas, loc="center")
    ax.axis('tight')
    ax.axis('off')
    plt.show()

def datos_tabla(matriz):
    columnas = ['Estado', 'Poblacion','Num. Contagiados', 'Porcentaje']
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
