from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

eixo_x_dias = [1,5,10,15,20,25,30]
eixo_y_temp_max = [28,29,25,32,34,36,31]
eixo_y_temp_min = [21,22,17,23,23,24,20]

plt.title("Temperaturas máximas e mínimas")
plt.xlabel("Data")
plt.ylabel("Temperatura (°C)")

plt.plot(eixo_x_dias, eixo_y_temp_max, label='Temp Máx')
plt.plot(eixo_x_dias, eixo_y_temp_min, label='Temp Mín')

plt.legended()
plt.show()