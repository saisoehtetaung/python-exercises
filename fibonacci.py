first = int(input("Enter First Number: "));
second = int(input("Enter second Number: "));
index = int(input("Enter how many index do you want: "));

def fibonacci(first,second,index):
    arr = [first,second];
    index_number = 0;
    while (index_number <= index):
        # print(arr[index_number-1]);
        arr.append( arr[index_number] + arr[index_number+1]);
        index_number += 1;
    
    return arr;

arr=fibonacci(first,second,index);
print(arr);