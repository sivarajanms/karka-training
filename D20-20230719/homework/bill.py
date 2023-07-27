name=(input("enter consumername:"))    
reading1=(int(input("enter reading 1:")))
reading2=(int(input("enter reading 2:")))
reading3=(int(input("enter reading 3:")))
reading4=(int(input("enter reading 4:")))
reading5=(int(input("enter reading 5:")))
saving_type=input("in which format you want save your data:" )


consumerdata = {
    "consumername": name,
    "reading": [reading1,reading2,reading3,reading4,reading5]} 


a=[]

for i in range(0,len(consumerdata ["reading"])-1):
    data=consumerdata ["reading"] [i+1]-consumerdata ["reading"][i]
    if data <=100:
        amount=0
    elif 100< data <=200:
        amount=(data)*2
    elif 200< data <=500:
        amount=(data)*5  
    elif 500< data <=1000:
        amount=(data)*10     
    elif data<=1000:
        amount=(data)*14    
    month=(i+1)
    view={"month":month,
          "data":data,
          "amount":amount,}
    a.append(view)      
# print(type (a))
b=str(a)
# print(type(b))
# file=open("/home/sivarajan/karka.txt","w")
# for i in a:
#     # print(f" month:{i['month']},\n  data:{i['data']},\n  amount:{i['amount']}")
#     file.write(f" month:{i['month']},\n  data:{i['data']},\n  amount:{i['amount']},\n")
# file.close
# file=open("/home/sivarajan/karka.txt","r")
# print(file.read())
# print(consumerdata)










    




















   