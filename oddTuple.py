def oddTuples(aTup):
    oddTup=tuple()
    for num in aTup:
        if len(num)%2==1:
            oddTup+=(num,)
    return oddTup

print(oddTuples(('hello','my','name','is','sai','soe','htet','aung')))
