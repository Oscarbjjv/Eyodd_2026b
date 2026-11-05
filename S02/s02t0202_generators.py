"""
generators son fuunciones que pueden 
pausar su ejecucion

cuando se invoca una funcion generadora
devuelve un objeto generador(aka iterador)

el codigo dentro de la funcion no se ejecuta
de inmediato, solo se compila.

la funcion se ejecuta unicamente cuando
iteras sobre el generador

"""

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10
    yield 11
    yield 12
    

#se invoca funcion generadora
my_iterator = my_generator()

#se itera manualmente sobre el generador
# print(next(my_iterator))#imprime 1
# print(next(my_iterator))#imprime 2
# print(next(my_iterator))#imprime 3
# print(next(my_iterator))#imprime 4

#los iteratores se puede iterar con un for
for value in my_iterator:
    print(value)

