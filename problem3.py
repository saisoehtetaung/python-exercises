s="wxryeclbhgmujdiwqnrzaq"
longest=''
arr=list()
longests=list()
subString=''
for i in s:
    if subString=='':
        subString=i
    elif subString[-1]<=i:
        subString+=i
    else:
        arr.append(subString)
        subString=i
arr.append(subString)
print(arr)
for sub in arr:
    if len(longest)<len(sub):
        longest=sub
longests.append(longest)
for n in arr:
    if len(longest)==len(n):
        longests.append(n)
print(longests)



