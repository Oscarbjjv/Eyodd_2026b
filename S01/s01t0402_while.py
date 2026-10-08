# Clase del dia 05/10/2026 en esta clase analisamos lo que hace el while "mientras que"
#copiaremos parte del codigo 1 para analisar los tiempos
#y las graficas que nos brindan sus tiempos
import time
 
 
# funcion que suma los primeros n numeros naturales usando while
def sum_of_n(n):
    total_sum = 0
 
    # sumando los n numeros: n + (n-1) + ... + 1
    while n > 0:
        total_sum = total_sum + n
        n = n - 1
    # retornando la suma total
    return total_sum
 
 
# VARIABLE PARA GUARDAR
# El data set
dataset = []
 
# generando el contenido del dataset (100 repeticiones)
for repetition in range(1, 11):
    # creando una marca de tiempo t1
    timestamp_01 = time.time()
 
    n = repetition * 100
 
    # sumo los n numeros y guardo el resultado
    result = sum_of_n(n)
 
    # tomamos el t2 
    timestamp_02 = time.time()
 
    # tiempo de ejecucion en microsegundos
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)
 
    # agregar la tripleta de datos al dataset
    dataset.append((n, elapsed_time, result))
 
# imprimir el dataset
for tup in dataset:
    print(tup)