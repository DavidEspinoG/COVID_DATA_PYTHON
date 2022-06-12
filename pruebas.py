import scripts as scr
import series as ser

def busca_estado():
    entrada = input('Lugar -> ')
    resultado = False
    entrada = entrada.upper()
    for e in scr.INT_MATRIZ: 
            if entrada in e:
                resultado = e
    if resultado == False:
        entrada = entrada.capitalize()
        for e in scr.INT_MATRIZ: 
            if entrada in e:
                resultado = e
    while resultado == False:
        print('Lugar inválido')
        resultado = busca_estado()
    return resultado
    

resultado = busca_estado()
print(resultado)
# lista_prueba = scr.INT_MATRIZ[0]
# print('AGUASCALIENTES' in lista_prueba)
