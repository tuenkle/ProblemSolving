def matrix_multiplication(a, b):  # square matrix only!!
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c


print(matrix_multiplication([[2, 3], [4, 1]], [[5, 7], [6, 8]]))
