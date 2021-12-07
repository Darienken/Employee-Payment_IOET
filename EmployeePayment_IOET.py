#Importing algorithms
import server as algorithms

#Main_func
def employee_payment_func(employee_data_arg):
    #Conditionals
    week_days=["MO", "TU", "WE", "TH", "FR"]
    weekend_days=["SA", "SU"]
    
    #Defining objects
    employee=algorithms.class_employees(employee_data_arg)
    dict_employee=employee.dic_employees
    dict_employee_days=employee.dic_days_worked
    dict_employee_hours=employee.dic_hours_worked
    dict_employee_timeS=employee.dict_start_time
    dict_employee_timeE=employee.dict_end_time
    dict_employee_payment={}

    #Itering over employees
    for iter_employee_name in dict_employee:
        value_to_pay=0
        
        #Itering over week days
        for day in week_days:
            hours_worked=dict_employee_hours.get(iter_employee_name)
            #Evaluating days employee work
            if day in dict_employee_days.get(iter_employee_name):
                #Getting day index for start time and end time
                index=dict_employee_days.get(iter_employee_name).index(day)
                start_time=int(dict_employee_timeS.get(iter_employee_name)[index])
                end_time=int(dict_employee_timeE.get(iter_employee_name)[index])
                #Evaluating times and multiplying hours worked
                if  start_time >= 0 and end_time <= 9:
                    value_to_pay+=hours_worked[index]*25
                elif start_time >= 9 and end_time <= 18:
                    value_to_pay+=hours_worked[index]*15
                elif start_time >= 18 and end_time <= 24:
                    value_to_pay+=hours_worked[index]*20
        
        #Itering over weekend days
        for day_wknd in weekend_days:
            hours_worked=dict_employee_hours.get(iter_employee_name)
            #Evaluating days employee work
            if day_wknd in dict_employee_days.get(iter_employee_name):
                #Getting day index for start time and end time
                index=dict_employee_days.get(iter_employee_name).index(day_wknd)
                start_time=int(dict_employee_timeS.get(iter_employee_name)[index])
                end_time=int(dict_employee_timeE.get(iter_employee_name)[index])
                #Evaluating times and multiplying hours worked
                if  start_time >= 0 and end_time <= 9:
                    value_to_pay+=hours_worked[index]*30
                elif start_time >= 9 and end_time <= 18:
                    value_to_pay+=hours_worked[index]*20
                elif start_time >= 18 and end_time <= 24:
                    value_to_pay+=hours_worked[index]*25
                
        #Update dict_employee_payment dictionary
        dict_employee_payment.update({iter_employee_name:value_to_pay})
    #Return dict with payments
    return dict_employee_payment


#Opening file
if __name__ == '__main__':
    with open("data.txt") as data_txt:
        employees_txt=data_txt.readlines()
    
    #Calling main function
    employee_payment=employee_payment_func(employees_txt)
    
    #Itering over employee payments and printing it
    for ele_employee in employee_payment:
        var_employee=employee_payment.get(ele_employee)
        print(f"The amount to pay {ele_employee} is: {var_employee} USD")