r = (lambda r, n=int(input('Number to test the multiplicative persistence of: ')), count=1, tmp=1, ll=(lambda n, tmp: list(reversed([tmp:=tmp*int(c) for c in str(n)]))[0]): count if ll(n, tmp) <= 9 else r(r, ll(n, tmp), count+1)); print(r(r))
