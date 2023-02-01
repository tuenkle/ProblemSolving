def binomial_coefficient_divide_and_conquer(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return binomial_coefficient_divide_and_conquer(n - 1, k - 1) + binomial_coefficient_divide_and_conquer(n - 1, k)


def binomial_coefficient_dynamic_programming(n, k):
    b = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                b[i][j] = 1
            else:
                b[i][j] = b[i - 1][j - 1] + b[i - 1][j]
    return b[n][k]


def binomial_coefficient_dynamic_programming_optimized(n, k):
    if k > n // 2:
        k = n - k
    b = [0] * (k + 1)
    b[0] = 1
    for i in range(n + 1):
        j = min(i, k)
        while j > 0:
            b[j] = b[j] + b[j - 1]
            j -= 1
    return b[k]


print(binomial_coefficient_dynamic_programming(10, 3))
print(binomial_coefficient_divide_and_conquer(10, 3))
print(binomial_coefficient_dynamic_programming_optimized(10, 3))
