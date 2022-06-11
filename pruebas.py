from matplotlib import pyplot as plt
fechas = ['04-2020', '05-2020', '06-2020', '07-2020']
casos = [1,5,3,4]

fig, ax = plt.subplots(figsize=(15,7))
ax.plot(fechas, casos)
ax.grid(True)
ax.set_title('Prueba')
plt.xticks(fechas, rotation= 80)
plt.show()
