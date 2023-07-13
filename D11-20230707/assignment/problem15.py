gender=input("what is your gender(M or F):")
f_name=input("enter your firstname:")
l_name=input("enter your lastname:")
age=int(input('age'))
married=input(f"are you married.{f_name},(y or n)?")


def check(age):
    if(age<=20):
        print(f"then i shall call you mrs.{f_name}")
        
