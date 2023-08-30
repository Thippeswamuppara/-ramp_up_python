import random

# Emp Id(1 to 9999) : Random Number
# Emp Location (Kormangala, HSR Layout, Ballary, Mumbai, Chennai, Nellore, Gurgon, Hyderabad) Choose any city from the list dynamically
# Emp salary (20,000 to 1,50,000) Random Numbe

def generator_emp_id(init,end):
    return random.randrange(init,end+1)
def emp_location(list_of_emp_location):
    return list_of_emp_location[random.randrange(0,len(list_of_emp_location))]
    #return list_of_emp_location[random.randrange(0,len(list_of_emp_location))]
def emp_salary_range(init,end):
    return random.randrange(init,end+1)
#print(emp_location(["hello","hello1"]))
enter_employees_numbers=int(input("enter how many employees details to generate: "))
def generate_employee_details():
    emp_dict={}
    for i in range(enter_employees_numbers+1):
        emp_id=generator_emp_id(1,9999)
        emp_loc=emp_location(["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgon", "Hyderabad"])
        salary=emp_salary_range(20000,150000)
        emp_dict['emp_id']=emp_id
        emp_dict["location"]=emp_loc
        emp_dict["salary"]=salary
        yield emp_dict

obj=generate_employee_details()
print(next(obj))
print(next(obj))
print(next(obj))
for i in obj:
    print(i)



