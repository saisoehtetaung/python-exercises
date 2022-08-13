def isIn(char,astr):
    if astr=='':
        return False
    elif len(astr)==1:
        return char==astr
    else:
        midIndex=len(astr)//2
        midChar=astr[midIndex]
        if char==midChar:
            return True
        elif char<midChar:
            return isIn(char,astr[:midIndex])
        else:
            return isIn(char,astr[midIndex+1:])


print(isIn('c','pqrstuvwxyz'))