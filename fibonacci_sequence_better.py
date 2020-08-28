f = (lambda r, n: n-1 if n<3 else r(r, n-1) + r(r, n-2)); print([f(f, i) for i in range(int(input('Pick the amount of numbers in the Fibonacci sequence to calculate: ')))])
