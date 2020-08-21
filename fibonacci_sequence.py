print([(lambda a:lambda b:a(a, b))(lambda r, n: n-1 if n < 3 else (r(r, n-1)+r(r, n-2)))(i) for i in range(1, 10)])
