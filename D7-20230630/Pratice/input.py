# input("which year you passed out from college")
passed_out_yr = input("which year you passed out from college")
print(passed_out_yr)
type_of_passed_out_yr=type(passed_out_yr)
print(type_of_passed_out_yr)
int_passed_out_yr=int(passed_out_yr)
print(type(int_passed_out_yr))
passed_out_year = input("which year you passed out from college")

year_int=int(passed_out_year)
is_eligible=not year_int == 2023
if is_eligible:
    print("person is eligible")
else:
    print("person is not eligible")  

