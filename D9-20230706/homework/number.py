# def largest (list):
#   sum=0
#   for a in list:
#     if a>sum:
#         sum=a
               
#   return sum
# print(largest([1,100,3,1000,4]))    


# def smallest (list):
#   sum=list[0]
#   for a in list:
#     if a<sum:
#         sum=a
#   return sum
# print(smallest([50,0,100,1000,4]))    

a=[0,0,1,2,3]  
for i,num in enumerate(a):
  if num==0:
    a.append(num)
print(a)



    