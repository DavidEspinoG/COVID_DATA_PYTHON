import os
import series as ser
RUTA_MAIN = os.path.dirname(__file__)
RUTA = RUTA_MAIN + '/data/data.csv'
def leer_archivo():
    with open(RUTA, 'r') as op:
        lines = op.readlines()
    datos = []
    for line in lines:
        columnas = line.split(',')
        datos.append(columnas)
    return datos
STRING_MATRIZ = leer_archivo()
def quita_enter(lista):
    resultado = []
    for e in lista:
        element = e.strip('\n')
        resultado.append(element)
    return resultado
def regresa_estados(matriz):
    estados = []
    for i in range(len(matriz)):
        element = matriz[i]
        estados.append(element[2])
    return estados
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
INT_MATRIZ = matriz_a_entero(STRING_MATRIZ)
def dia_con_mas_casos():
    print('Día con más casos')
def porcentaje_casos():
    print('Porcentaje de casos')
def series_tiempo():
    estado_user_input = input('''
        ==================================================================================
        ==                                                                              ==
        ==  Teclea el nombre de algún estado de la república o la opción "Nacional"     ==
        ==                                                                              ==    
        ==================================================================================
        Lugar -> ''')
    lista_casos_estado = ser.busca_estado(estado_user_input)
    lista_fechas_sin_dias = quita_enter(ser.quita_dias(STRING_MATRIZ[0]))
    # estados = regresa_estados(INT_MATRIZ)
    casos_por_mes_estado = ser.suma_casos_mes(lista_fechas_sin_dias, lista_casos_estado)
    meses = ser.regresa_meses(lista_fechas_sin_dias)
    ser.grafica_historico_estado(meses, casos_por_mes_estado, lista_casos_estado[2])
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

def main_menu():
    option = 0
    while option != 4:
        imprime_opciones()
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
def main():
    main_menu()
   
if __name__ == '__main__':
    main()