def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        d[n]=fib_efficient(n-1,d)+fib_efficient(n-2,d)
        return d[n]
    
d={1:1,2:2}
print(fib_efficient(18,d))
print(d)