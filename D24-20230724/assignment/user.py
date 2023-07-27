
from datetime import datetime
curr_datetime=time(2023,7,25,12,16,56)
time=datetime.now()
b=datetime.strptime("24 december 2022","%d%B%y")
print(b)


# import pytz
# import datetime
# from datetime import datetime
# utc = pytz.utc
# kiev_tz = pytz.timezone('Europe/Kiev')
# print('UTC Time =', datetime.now(tz=utc))
# print('IST Time =', datetime.now(tz=kiev_tz))



# a=10
# b=50
# c=60
# e=0
# if a>e:
#     e=a
# if b>e:
#     e=b
# if c>e:
#     e=c
  
# print(f"{e}")    




# monthly_gold_rate=[{"monthname":"jan",
#                     "rate":1500,
#                     "jwel_list":[{"name":"chain",
#                                 "making_cost":12},
#                                 {"name":"ring",
#                                 "making_cost":14}]},
#                    {"monthname":"feb", 
#                     "rate":2000,
#                     "jwel_list":[{"name":"chain",
#                                 "making_cost":14},
#                                 {"name":"ring",
#                                 "making_cost":14}]},
#                    {"monthname":"mar",
#                     "rate":1000,
#                     "jwel_list":[{"name":"chain",
#                                 "making_cost":16},
#                                 {"name":"bracelet",
#                                 "making_cost":14}]}]
# max=0
# for i in monthly_gold_rate:
#     if max<(i["rate"]):
#         max=(i["rate"])
# # print(f'{max}')

# min=5000
# for i in monthly_gold_rate:
#     if min>(i["rate"]):
#         min=(i["rate"])
# # print(f"{min}") 

# for i in monthly_gold_rate:
#     print(i["jwel_list"])

    

   

    
    











# for i in monthly_gold_rate:
#     if max<(i["rate"]):
#         max=(i["rate"])
    
# print(f"{max}")     
# min=1500
# for i in monthly_gold_rate:
#     if min>(i["rate"]):
#         min=(i["rate"])
# print(f"{min}")        





