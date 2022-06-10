import scripts as scr
string_matriz = scr.leer_archivo()
int_matriz = scr.matriz_a_entero(string_matriz)
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
    for e in int_matriz: 
            if estado in e:
                resultado = e
    if resultado == None:
        estado = estado.capitalize()
        for e in int_matriz: 
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
    suma = 0
    for i in range(2,len(lista_casos)):
        if i == len(lista_fechas) -1:
            break
        elif lista_fechas[i] == lista_fechas[i + 1]:
            suma += lista_casos[i]
        else: 
            casos_mes.append(suma)
            suma = 0
    return casos_mes        
def main():
    fechas = string_matriz[0]
    estados = scr.regresa_estados(int_matriz)
    fecha_sin_dias = scr.quita_enter(quita_dias(fechas))
    lista_estado = busca_estado('Aguascalientes')
    print(suma_casos_mes(fecha_sin_dias, lista_estado ))
if __name__ == '__main__':
    main() 