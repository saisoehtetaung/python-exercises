han=open("aa.txt")

for line in han:
    line=line.rstrip()
    words=line.split()
    print(words);
    if len(words)<3 or words[0] != "From":
        continue
    print (words[2])
