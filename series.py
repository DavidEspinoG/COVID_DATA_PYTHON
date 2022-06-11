import scripts as scr
from matplotlib import pyplot as plt
# STRING_MATRIZ = scr.leer_archivo()
# int_matriz = scr.matriz_a_entero(STRING_MATRIZ)
def grafica_historico_estado(meses, casos_por_mes, estado):
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(meses, casos_por_mes)
    ax.grid(True)
    ax.set_title(f'Histógrama {estado}')
    ax.set_xlabel('Meses')
    ax.set_ylabel('Casos')
    plt.subplots_adjust(bottom=0.25)
    plt.xticks(meses, rotation= 80)
    plt.show()
def quita_dias(lista_fechas):
    sin_dias = []
    for i in range(len(lista_fechas)):
        if i < 3:
            sin_dias.append(lista_fechas[i]) 
        else:
            fecha = lista_fechas[i]
            sin_dias.append(fecha[3:])
    return sin_dias
def busca_estado(estado):
    resultado = None
    estado = estado.upper()
    for e in scr.INT_MATRIZ: 
            if estado in e:
                resultado = e
    if resultado == None:
        estado = estado.capitalize()
        for e in scr.INT_MATRIZ: 
            if estado in e:
                resultado = e
    return resultado
def menu_series():
    print('''
        ==================================================================================
        ==                                                                              ==
        ==  Teclea el nombre de algún estado de la república o la opción "Nacional"     ==
        ==                                                                              ==    
        ==================================================================================
        ''')
    entrada = input('Lugar -> ')
    estado = busca_estado(entrada)
    while estado == None:
        print('Lugar inválido')
        entrada = input('Lugar -> ')
        estado = busca_estado(entrada)
def suma_casos_mes(lista_fechas, lista_casos):
    casos_mes = []
    suma = lista_casos[3]
    for i in range(4,len(lista_casos)):
        if lista_fechas[i] == lista_fechas[i - 1]:
            suma += lista_casos[i]
        elif lista_fechas[i] != lista_fechas[i - 1]:
            casos_mes.append(suma)
            suma = lista_casos[i]
        if i + 1 == len(lista_casos):
            casos_mes.append(suma)   
    return casos_mes
def regresa_meses(lista):
    resultado = []
    for i in range(4, len(lista)):
        element = lista[i]
        if element not in resultado:
            resultado.append(element)
    return resultado        