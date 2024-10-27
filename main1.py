import random

def generate_matrix(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            if i == j:  
                row.append(random.randint(-10, 10))  
            elif i + j == n - 1:  
                row.append(random.randint(-10, 10))  
            else:
                row.append(random.randint(-10, 10)) 
        matrix.append(row)
    return matrix

def swap_columns(matrix):
    min_abs_value = float('inf')
    min_col_index = -1

    for j in range(len(matrix[0])):  
        for i in range(len(matrix)):  
            if abs(matrix[i][j]) < min_abs_value:
                min_abs_value = abs(matrix[i][j])
                min_col_index = j

    for i in range(len(matrix)):
        matrix[i][0], matrix[i][min_col_index] = matrix[i][min_col_index], matrix[i][0]

    return matrix

first_name = "Ульяна"  
last_name = "Митлович"  

n = len(first_name)
m = len(last_name)

matrix = generate_matrix(m, n)
print("Початкова матриця:")
for row in matrix:
    print(row)

swapped_matrix = swap_columns(matrix)
print("\nМатриця після зміни стовпчиків:")
for row in swapped_matrix:
    print(row)
