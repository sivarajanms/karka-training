q1=input("does it stay inside or outside or both?")
q2=input("is it a living thing?")


# if(q1=="outside")and(q2=="yes"):
#     outside=("bison")
#     print(outside)
# elif(q1=="inside")and(q2=="yes"):
#     inside=("houseplant")
#     print(inside)    
# elif(q1=="both")and(q2=="yes"):
#     both=("dog")  
#     print(both)  
# elif(q1=="outside")and(q2=="no"):
#     outside=("billboard")
#     print(outside)
# elif(q1=="inside")and(q2=="no"):
#     inside=("shower curtain")
#     print(inside)    
# elif(q1=="both")and(q2=="no"):
#     both=("cell phone")  
#     print(both)    


def check(q1,q2):
    ans=" "
    if(q1=="outside")and(q2=="yes"):
        ans="bison"
    elif(q1=="outside")and(q2=="no"):
        ans="billboard"    
    elif(q1=="inside")and(q2=="yes"):
        ans="houseplant"
    elif(q1=="inside")and(q2=="no"):
        ans="shower curtain"    
    elif(q1=="both")and(q2=="yes"):
        ans="dog"
    elif(q1=="both")and(q2=="yes"):
        ans="cellphone"
    return ans
q=check(q1,q2)    
print(q)
#print(print(f"my guess is that you are thinking of a ,{q}.\nI would ask you if I'm right ,but I don't actually care."))


