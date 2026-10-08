# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # O(1)

def random_function(students):
    first = students[0] # O(1)
    total = 0 # O(1)
    new_list = [] # O(1)
    

    for student in students:
        print("Se le suma 1 al total")
        total += 1 # O(n) es n por el numero de estudiantes en la lista
        new_list.append(student) # O(n) por que se ejecuta tantas veces tenga la lista

    print(new_list) # O(1)
    return total # O(1)

print(random_function(student_list_01))
print(f"Tamaño de lista {len(student_list_01)}")
print(random_function(student_list_01))
                                                                                                                    
#calcular O(2n)+O(5)=O(2n+5) = O(n)

#notas:
#sumando los O(1) en el codigo nos da O(5) y sumando O(n) nos da 2(n)
#los for no cuentan para  O(1 ni O(n) ya que solo es una expresion)
#si hay un for dentro de otro for si cuenta para O(n^2) ya que se ejecuta n veces por cada n veces del primer for