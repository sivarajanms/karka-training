consumerdata = {
    "consumername": "siva",
    "reading": [1100, 1200, 1350, 1650, 2050]} 

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
file=open("/home/sivarajan/karka.txt","w")
for i in a:
    # print(f" month:{i['month']},\n  data:{i['data']},\n  amount:{i['amount']}")
    file.write(f" month:{i['month']},\n  data:{i['data']},\n  amount:{i['amount']},\n")
file.close
file=open("/home/sivarajan/karka.txt","r")
print(file.read())





    




















   