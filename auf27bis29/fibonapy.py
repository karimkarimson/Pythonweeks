fib = 0
buffer = 0
result = 0
for i in range(8):
    print(result)
    if result == 0:
        result += 1
        print(result)
    else:
        buffer = fib
        fib = result
        result = fib + buffer
        