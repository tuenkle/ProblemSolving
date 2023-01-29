def fibonacci(x):
    first = 0
    second = 1
    if x == 0:
        return first
    elif x == 1:
        return second
    else:
        for _ in range(x - 1):
            first, second = second, first + second
    return second


print(fibonacci(10))
