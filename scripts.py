def dia_con_mas_casos():
    print('Día con más casos')
def porcentaje_casos():
    print('Porcentaje de casos')
def series_tiempo():
    print('Series de tiempo')
def menu():
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
    option = 0
    while option != 4:
        option = int(input("Opción: "))
        if option == 1:
            dia_con_mas_casos()
        elif option == 2:
            porcentaje_casos()
        elif option == 3:
            series_tiempo()
        else:
            print("Elige una opción válida")    
       

def main():
    
    menu()

if __name__ == '__main__':
    main()