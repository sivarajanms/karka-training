#year=int(input("enter a year:"))
#def checkleapyear (a):
#    if(a%4==0 and a%100!=0 or a% 400==0):
 #       return "year is a leap year"
  #  else:
  #      return "not a leap year"       

#leap = checkleapyear(year)        
#print(leap)



age=int(input("enter a age:"))
def person (b):
    if(b>=18):
        return "you are eligible to vote"
    else:
        return "you are not eligible to vote"

number = person(age)
print(number)        