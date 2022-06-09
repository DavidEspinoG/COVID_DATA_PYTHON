import scripts as scr
string_matriz = scr.leer_archivo()
int_matriz = scr.matriz_a_entero(string_matriz)
fechas = string_matriz[0]
def busca_estados(estado):
    resultado = None
    for e in int_matriz: 
            if estado in e:
                resultado = e
    return resultado
def main():
    print(busca_estados('YUCATAN'))
    
if __name__ == '__main__':
    main() 