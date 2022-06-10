import os
ruta_main = os.path.dirname(__file__)
ruta = ruta_main + '/data/data.csv'
def regresa_estados(matriz):
    estados = []
    for i in range(len(matriz)):
        element = matriz[i]
        estados.append(element[2])
    return estados
def leer_archivo():
    with open(ruta, 'r') as op:
        lines = op.readlines()
    datos = []
    for line in lines:
        columnas = line.split(',')
        datos.append(columnas)
    return datos
def string_a_entero(lista):
    lista_enteros = []
    for i in range(len(lista)):
        if i == 0 or i == 2:
            element = lista[i]
            lista_enteros.append(element[1:-1])
        else: 
            lista_enteros.append(int(lista[i]))
    return lista_enteros
def matriz_a_entero(matriz):
    matriz_int = []
    for i in range(1,len(matriz)):
        elemento = string_a_entero(matriz[i])
        matriz_int.append(elemento)
    return matriz_int
def fecha_sin_dias(lista_fechas):
    sin_dias = []
    for i in range(len(lista_fechas)):
        if i < 3:
            sin_dias.append(lista_fechas[i]) 
        else:
            fecha = lista_fechas[i]
            sin_dias.append(fecha[3:])
    return sin_dias
def dia_con_mas_casos():
    print('Día con más casos')
def porcentaje_casos():
    print('Porcentaje de casos')
def series_tiempo():
    pass
def imprime_opciones():
    print('''
        ==================================================================================
        ==                                                                              ==
        ==  Elige una de las siguientes opciones:                                       ==
        ==      1. Día con más casos a nivel nacional                                   ==
        ==      2. Porcentaje de casos confirmados de acuerdo a la población            ==
        ==      3. Series de tiempo                                                     ==
        ==      4. Salir                                                                ==
        ==                                                                              ==
        ==================================================================================
        ''')
def menu():
    imprime_opciones()
    option = 0
    while option != 4:
        option = int(input("Opción: "))
        if option == 1:
            dia_con_mas_casos()
        elif option == 2:
            porcentaje_casos()
        elif option == 3:
            series_tiempo()
        elif option == 4:
            print("Saliendo...")
        else: 
            print("Opción inválida")
            imprime_opciones()    
def main():
    pass

if __name__ == '__main__':
    main()