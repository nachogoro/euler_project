# Utilities related to the Fibonacci sequence, to be reused among problems

def fibonacci_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

