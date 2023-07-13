weight=int(input("enter your current earth weight:"))
print("i have information for the following planets:\n\t1.venus\t\t2.Mars\t\t3.jupiter\n\t4.saturn\t5.uranus\t6.neptune")      
planet=int(input("which planet are you visiting:"))      
def gravity(planet,weight):
    if(planet==1):
        total=0.78*weight
        print(f"your weight would be {total} pounds on that planet.")
    elif(planet==2):
        print(0.39*weight)
    elif(planet==3):
        print(2.65*weight)
    elif(planet==4):
        print(1.17*weight)
    elif(planet==5):
        print(1.05*weight)
    elif(planet==6):
        print(1.23*weight)
    


gravity(planet,weight)    
#print(f"your weight would be {total} pounds on that planet.")
