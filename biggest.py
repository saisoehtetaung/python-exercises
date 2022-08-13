def biggest(aDict):
    result=None
    biggestValue=0
    for key in aDict.keys():
        if len(aDict[key])>=biggestValue:
            result=key
            biggestValue=len(aDict[key])
    return result


some={'a':[1,4,2,1],'b':[3,5,2,6,6],'c':[1,3]}
big=biggest(some)
print(big)