#name=input("enter name:")
#age=input("enter age:")
#dob=input("enter dob:")
#location=input("enter location:")
#college=input("enter college name:")
#print('Hello,my name is',name,'i am',age,'year old and was born on',dob,'currently,i am located in',location,'and i completed my degree at' ,college,)

# age=int(input("age:"))
# if(age>=18):
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

#number=int(input("number:"))
#if(number%2==0):
    #print(number,"is an even number")
#else:
 #   print(number,"is an odd number")    

item1=int(input("enter the amount of item1:"))
item2=int(input("enter the amount of item2:"))
item3=int(input("enter the amount of item3:"))
item4=int(input("enter the amount of item4:"))
items=item1+item2+item3+item4


if(items <1000) and (items>500):
    print("you have owend a silver token")
elif(items >1000):
    print("you have owend a golden token")
    

