import model as methods

#main_func
def employee_total_paid(employee_arg):
    employee=methods.employees(employee_arg)
    hours=employee.calculate_hours()
    days=employee.calculate_days()
    main_class=employee.calculate_time()
    
    to_paid=[]
    for empl in main_class:
        total=0
        for val in main_class.get(empl):
            total=val+total
            total_to_paid=f"The amount to pay {empl} is: {total} USD"
        to_paid.append(total_to_paid)
    return to_paid


#Open file
if __name__ == '__main__':
    with open("data.txt") as employee_txt:
        employee_data=employee_txt.readlines()
    print(employee_total_paid(employee_data))