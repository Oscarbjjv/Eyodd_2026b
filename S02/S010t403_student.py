#1 creando una lista de estudiantes 
#identifico el tamaño de la entrada "n"
#E tamaño de la entrada es el numero de estudiantes
#2 Es ver cuanto crece el numero el tamaño de la entrada
# Agrego las bigO identificadas
#O(n) * 4*0(1) = O(n+4) = O(n)


studen_list_01 = ["Jordan", "Pipen", "curry", "Shack"]
studen_list_02 = ["Mike", "Saul", "Walter", "Jessy"]
 #verficando si un estudiante esta en la lista
def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student:
            print("Estudiante encontrado") #O(1)
            return student #O(1)
      #si no encuentro a estuiante
    print("Estudiante no encontrado") #O(1)
    return None #O(1)

        #probando algoritmo
check_student("Walter", studen_list_01)