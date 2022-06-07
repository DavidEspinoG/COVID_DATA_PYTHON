import os
ruta_main = os.path.dirname(__file__)
ruta = ruta_main + '/data/data.csv'
def leer_archivo():
    with open(ruta, 'r') as op:
        lines = op.readlines()
    datos = []
    for line in lines:
        columnas = line.split(',')
        datos.append(columnas)
    print(datos)
def string_a_entero(lista):
    lista_enteros = []
    for i in len(lista):
        if i == 0 or i == 2:
            lista_enteros.append(lista[i])
        else: 
            lista_enteros.append(int(lista[i]))
    return lista_enteros
def dia_con_mas_casos():
    print('Día con más casos')
def porcentaje_casos():
    print('Porcentaje de casos')
def series_tiempo():
    print('Series de tiempo')
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
    # menu()
    leer_archivo()
if __name__ == '__main__':
    main()