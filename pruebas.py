import series as ser
fechas = ['cve_ent', 'poblacion', 'nombre', '02-2020', '02-2020', '02-2020','03-2020','03-2020','04-2020']
casos = [000,81728,'Probando', 2, 1, 1, 1,1,1]
casos_mes = []
suma = casos[3]
for i in range(4,len(casos)):
    if fechas[i] == fechas[i - 1]:
        suma += casos[i]
    elif fechas[i] != fechas[i - 1]:
        casos_mes.append(suma)
        suma = casos[i]
        if i + 1== len(casos):
            casos_mes.append(suma)   
print(casos_mes)


    # if fechas[i] != fechas[i-1]:
    #     if type(fechas[i - 1]) != str:
    #         
    #     suma = casos[i]
        
    # else: 
    #     suma = suma + casos[i]

   
   
   
   
    # print(f'iteracion: {i} , casos:  {casos[i]}')
    # print('i = ', i)
    # print('len casos = ', len(casos))
    # if fechas[i + 1] 
    # if i + 1 == len(fechas):
    #     break
    # elif fechas[i] == fechas[i + 1]:
    #     suma += casos[i]
    # else: 
    #     casos_mes.append(suma)
    #     suma = 0







# resultado = ser.suma_casos_mes(fechas, casos)
# print(resultado)