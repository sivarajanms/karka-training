# from datetime import date
# a_datetime=date(2023,7,26)
# date=a_datetime.today()
# b=datetime.strftime("%Y")
# print(date)

# # import the modules
# import pytz
# import datetime
# from datetime import  datetime
# # getting utc timezone
# utc=pytz.utc
# india= pytz.timezone("Asia/kolkata")
# # print("UTC time =",datetime.now(tz=utc))
# print("IST time =",datetime.now(tz=india))




for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print(" ")

# k=1
# for i in range(1,6):
#     for j in range(1,6):
#         print(k,end=" ")
#         k+=1
#     print( )    
# n= int(input("number"))    
# for i in range(n*n,0,-1):
#     if i%n==0:
#         print('')
#     print(i,end=' ')



a=[0,0,1,2,3,4]
# sum=0
# for i,num in enumerate(a):
#     sum=sum+num
#     print(sum)

# for i in range():
#     a.append(0)
#     print(a)


from datetime import datetime
curr_datetime=time(2023,7,25,12,16,56)
time=datetime.now()
b=datetime.strptime("24 december 2022","%d%B%y")
print(b)

