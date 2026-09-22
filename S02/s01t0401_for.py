"""
Escribir un programa que calcule la suma de los "n"
 numeros naturales, por ejemplo si  =100, el programa 
calcula la suma de 1 al 100
"""
# importamos bibilioteca time

import time

#Creando una marca de tiempo 
timestamp_01 = time.time()

#programa que calcula la suma de los"n"numeros naturales
n = 100
total_sum= 0
for number in range(1, n + 1):
  
    total_sum=total_sum + number


    #1: sum <- 0 + 1
    #sum =1
    #2: sum <-1+2
    #sum =3
    #3: sum <-3+3
    #sum =6
    #100: sum <- sum_(1) + 100


print(f"La suma de uno hasta {n} es: {total_sum}")
timestamp_02 = time.time()
print(f"Tiempo de ejecución: {(timestamp_02 - timestamp_01)*1e6:2f} μs")
