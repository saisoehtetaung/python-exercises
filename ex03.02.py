try :
    fh=float(input("Hour: "))
    fr=float(input("Rate: "))
except:
    print("Please enter numeric value.")
    quit()
    
if fh>40:
        oh=fh-40
        orate=fr*0.5
        os=oh*orate
        print("Overtime hour: ",oh)
        print("Overtime Salary:",os)
        print("Total Salary:",(fr*40)+os)
else :
        print("Don't have overtime.")
        print("Salary:",fh*fr)