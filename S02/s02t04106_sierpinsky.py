from array import array as arr

#parametros de mi cuadricula
rows = 8
columns = 2 * rows - 1

matrix=[]

for rows in range(rows):
    new_rows = arr('i',[0]* columns)
    matrix.append(new_rows)

#validando l ocnstruccion del grid
print(f"cantidad de filas{len(matrix)}")
print(f"Cantidad de columnas{len(matrix[0])}")

for rows in matrix:
    print(list(rows))