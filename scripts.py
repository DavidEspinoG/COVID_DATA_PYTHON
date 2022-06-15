import os
import series as ser
import porcentaje as por
import maximos as maxi
RUTA_MAIN = os.path.dirname(__file__)
RUTA = RUTA_MAIN + '/data/defunciones.csv'
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
    maximos = maxi.regresa_max_contagios()
    indices = maxi.index_max_contagios(maximos)
    estados = regresa_estados(INT_MATRIZ)
    fechas = maxi.fecha_max_contagio(indices)
    matriz_final = maxi.regresa_matriz_maximos(estados, fechas, maximos)
    columnas = ['Estado', 'Fecha', 'Máximo']
    maxi.muestra_tabla_max_contagios(matriz_final, columnas)
    maxi.grafica_maximos_estado(estados[:-1], maximos[:-1])
def porcentaje_casos():
    datos_tabla_porcentajes = por.total_casos_estados(INT_MATRIZ)
    por.datos_tabla(datos_tabla_porcentajes)

    datos1, datos2 = por.datos_grafica_barras(datos_tabla_porcentajes)
    por.grafica2(datos1,datos2)
def series_tiempo():
    print('''
        ==================================================================================
        ==                                                                              ==
        ==  Teclea el nombre de algún estado de la república o la opción "Nacional"     ==
        ==                                                                              ==    
        ==================================================================================
        ''')
    lista_casos_estado = ser.busca_estado()
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