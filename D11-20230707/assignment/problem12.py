q1=input("Is it animal,vegetable,or mineral?\n")
q2=input("Is it bigger than a breadbox?\n")

# if(q1=="animal"):
#     if(q2=="yes"):
#         print("my guess is that you are thinking of a mouse.\nI would ask you if I'm right ,but I don't actually care.")
#     elif(q2=="no"):    
#         print("my guess is that you are thinking of a squirrel.\nI would ask you if I'm right ,but I don't actually care.")


# if(q1=="vegetable"):
#     if(q2=="yes"):
#         print("my guess is that you are thinking of a watermelon.\nI would ask you if I'm right ,but I don't actually care.")
#     elif(q2=="no"):
#         print("my guess is that you are thinking of a carrot.\nI would ask you if I'm right ,but I don't actually care.")



# if(q1=="mineral"):
#     if(q2=="yes"):
#         print("my guess is that you are thinking of a camaro.\nI would ask you if I'm right ,but I don't actually care.")
#     elif(q2=="no"):
#         print("my guess is that you are thinking of a paper clip.\nI would ask you if I'm right ,but I don't actually care.")


def check(q1,q2):
    ans="  "
    if q1=="animal"and q2=="yes":
        ans="mouse"
    elif q1=="animal"and q2=="no":
        ans="squriel"
    elif q1=="vegetable"and q2=="yes":
        ans="watetmelon"
    elif q1=="vegetable"and q2=="no":
        ans="carrot"
    elif q1=="mineral" and q2=="yes":
        ans="camaro"        
    elif q1=="mineral" and q2=="no":
        ans="paper clip"
    return ans
q=check(q1,q2)
print(f"my guess is that you are thinking of a ,{q}.\nI would ask you if I'm right ,but I don't actually care.")   


        
