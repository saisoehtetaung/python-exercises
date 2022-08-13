def gcdIter(a,b):
    large=0
    d=1
    while d<=a or d<=b:
        if a%d==0 and b%d==0:
            if d>large:
                large=d
        d+=1
    return large

print(gcdIter(23,0))