s="azcbobobegghakl"
count=0
i=0
while i<len(s):
    if s[i:i+3]=='bob':
        count+=1
    i+=1    
print("Number of times bob occurs is:",count)