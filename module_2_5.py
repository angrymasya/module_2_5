def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        line = [value]*m
        matrix.append(line)
    return matrix
result1 = get_matrix(3,2 ,1 )
result2 = get_matrix(2, 4, 30)
result3 = get_matrix(5, 3, 17)
print(result1)
print(result2)
print(result3)