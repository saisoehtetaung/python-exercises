fname=input("Enter fileName: ")
if fname == '':
    han=open("clown.txt")
else:
    han=open(fname)

di=dict()
for line in han:
    line=line.rstrip()
    words=line.split()
    for word in words:
        di[word]=di.get(word,0)+1
        
    #for word in words: 
    #	if di.get(word):
    #		di[word]+=1;
    #	else:
    #		di[word]=1;
    #		print(di);

print(di)
lst=list()
for k,v in di.items():
    a=(v,k)
    lst.append(a)

newlst=sorted(lst,reverse=True)
print("Top 5 most common words")
for v,k in newlst[:5]:
    print(k,v)

