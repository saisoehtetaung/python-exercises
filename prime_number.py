num = 20;
prime = [];
for k in range(2,num): 
    for i in range(2,k):
        if (k % i) == 0:
            break;
    else:
        prime.append(k);


print(prime);
    