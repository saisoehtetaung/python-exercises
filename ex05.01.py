num=0
total=0.0
count=0
average=0.0
while True :
    x=input("Enter a number(type 'done' for exit): ")
    try:
        num=float(x)
        total+=num
        count+=1
        average=total/count
    except:
        if x== 'done':
            print("Total:",total)
            print("Count:",count)
            print("Average:",average)
            break
        else:
            print("invalid input")
            continue


