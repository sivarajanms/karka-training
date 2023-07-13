# a=[500,200,300,1000]
# sum=0
# enum_a=enumerate(a)
# for i,num in enum_a:
#     print("entering iteration process or item"+str(i))
#     print("before",sum)    
#     sum=sum+num
#     print("after",sum)  
#     print("exiting iteration process or item"+str(i))  
#     print("\n")

# print("sum of the list is:",sum) 
# print("average of the list is:",sum/len(a))



# a=[1,2,3,4,5,6]
# sum=0
# for i,num in enumerate(a):
#     sum=sum+num
# print(sum)    

# a=[500,200,300,1000]
# c=[]
# for i,num in enumerate(a):
#     b="INR"+str(num)
#     c.append(b)
# print(c)


# a=[1,2,3,4]
# b=[]
# c=[]
# for i,num in enumerate(a):
#     if(num%2==0):
#         b.append(num)
#     else:
#         c.append(num)

# print("even",b)
# print("odd",c)

a=[0,0,1,2,3]  
for i,num in enumerate(a):
  if num==0:
    a.append(num)
print(a)
