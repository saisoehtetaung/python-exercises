fname=input("Enter the filename:")
han=open(fname)


dmName=''
days=dict()
for line in han:
    line=line.rstrip()
    words=line.split()
    if len(words)<3 or words[0] != "From":
        continue
    a=words[1].find('@')
    b=words[1][a+1:]
    days[b]=days.get(b,0)+1
print(days)
mostmail=None
for k,v in days.items():
    if mostmail is None:
        mostmail=v
    if mostmail<v:
        dmName=k
        mostmail=v
print("Most Mail:",dmName,mostmail)

