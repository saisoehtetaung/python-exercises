import re

rugex=input("Enter a regular expression: ")
file=open("aa.txt")
count=0
for line in file:
    line=line.rstrip()
    rstr=re.findall(rugex,line)
    if len(rstr)>0:
        print(rstr)
        count+=1
        print(count)
print("aa.txt had ",count,"lines that matched",rugex)
