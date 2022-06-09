import scripts as scr
def main():
    string_matriz = scr.leer_archivo()
    int_matriz = scr.matriz_a_entero(string_matriz)
    fechas = string_matriz[0]
    print(int_matriz)
if __name__ == '__main__':
    main() 