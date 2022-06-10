import scripts as scr
string_matriz = scr.leer_archivo()
int_matriz = scr.matriz_a_entero(string_matriz)
fechas = string_matriz[0]
estados = scr.regresa_estados(int_matriz)
def busca_estado(estado):
    resultado = None
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
    
    estado = input('Lugar -> ')
    # if estado != 'nacional':

def main():
    print(busca_estado('nacional'))
if __name__ == '__main__':
    main() 