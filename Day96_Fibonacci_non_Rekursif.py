def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            next_term = fib_list[i-1] + fib_list[i-2]
            fib_list.append(next_term)
        return fib_list

# coba function
print(fibonacci(10)) # output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
