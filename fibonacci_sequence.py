f = (lambda r, n: n-1 if n<3 else r(r, n-1) + r(r, n-2)); print([f(f, i) for i in range(int(input('Enter the number of numbers in the Fibonacii sequence to calculate: ')))])
