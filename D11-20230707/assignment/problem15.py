gender=input("what is your gender(m or f):")
f_name=input("enter your firstname:")
l_name=input("enter your lastname:")
age=int(input('age:'))
if(gender=='m') and (age>20):
    print(f"then i shall call you mr.{f_name}{l_name}.")
elif(gender=='m') and (age<20):
    print(f"then i shall call you {f_name}{l_name}.")    
elif(gender=='f') and (age>20):
    married=input("are you married.(y or n)?") 
    if(married=='y'):
        print(f"then i shall call you mrs{f_name}{l_name}.")         
    elif(married=='n'):    
        print(f"then i shall call you ms{f_name}{l_name}.")
elif(gender=='f') and (age<20):
    print(f"then i shall call you ms{f_name}{l_name}.")
   
