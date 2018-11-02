def Fibonacci(n):
    if n == 0:
        fib = 1
    elif n == 1:
        fib = 1
    else:
        fib = Fibonacci(n-2)+Fibonacci(n-1)
    return fib

print(Fibonacci(3))
