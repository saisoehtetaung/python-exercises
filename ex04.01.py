def computePay(hour,rate):
    if hour>40:
        otp=(hour-40)*(rate*0.5)
        pay=(40*rate)+otp
    else:
        pay=hour*rate
    return pay

try :
    fh=float(input("Hour: "))
    fr=float(input("Rate: "))
except:
    print("Please enter numeric value.")
    quit()

print ("Total Salary",computePay(fh,fr))