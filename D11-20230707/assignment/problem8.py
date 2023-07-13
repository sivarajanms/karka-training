day=int(input("enter a weekday:"))
def day_checker(day):
    if day==0 or day==7:
        print("today is a saturday")
    elif day==1:
        print("today is a sunday")    
    elif day==2:
        print("today is a monday")
    elif day==3:
        print("today is a tuesday")  
    elif day==4:
        print("today is a wednesday")
    elif day==5:
        print("today is a thursday")       
    elif day==6:
        print("today is a friday")     
day_checker(day)

