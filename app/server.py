#Creating main class
class class_employees:
    
    #Initializing Objects
    def __init__(self,employees_list):
        #Putting everything inside a dic
        self.dic_employees={}
        for el_employee in employees_list:
            self.replace_equal=el_employee.replace("=",",")
            self.dic_employees.update({el_employee[:el_employee.index("=")]:self.replace_equal.split(",")[1:]})
        #Calling calculate_hours method for getting hours worked
        self.dic_hours_worked=self.calculate_hours(self.dic_employees)
        #Calling calculate_days method for getting days worked
        self.dic_days_worked=self.calculate_days(self.dic_employees)
        #Calling times method for getting times
        self.time=self.times(self.dic_employees)
    
    def calculate_hours(self,dic_employees):
        #Creating new dic
        self.employees_hours={}
        #iterating over dic
        for employee in dic_employees:
            self.employee_data=dic_employees.get(employee)
            self.worked_hours=[]
            #Update employee hours
            self.employees_hours.update({employee:self.worked_hours})
            #iterating over hours
            for hours in self.employee_data:
                self.start=hours[2:4]
                self.end=hours[8:10]
                #Each round we append hours to worked_hours list
                self.worked_hours.append(int(self.end)-int(self.start))
        #Return dic with hours worked
        return self.employees_hours
    
    def calculate_days(self,dic_employees):
        #Creating new dic
        self.employees_days={}
        #iterating over dic
        for employee in dic_employees:
            self.employee_data=dic_employees.get(employee)
            self.worked_days=[]
            #Update employee days
            self.employees_days.update({employee:self.worked_days})
            #iterating over days
            for days in self.employee_data:
                self.worked_days.append(days[:2])
        #Return dic with days worked
        return self.employees_days
    
    def times(self, dic_employees):
        #Defining dics with times
        self.dict_start_time={}
        self.dict_end_time={}
        #Itering over employees
        for el_employee_name in dic_employees:
            self.li_start_time=[]
            self.li_end_time=[]
            #Itering over times
            for times in dic_employees.get(el_employee_name):
                self.start=times[2:4]
                self.end=times[8:10]
                self.li_start_time.append(self.start)
                self.li_end_time.append(self.end)
            #Updating dicts
            self.dict_start_time.update({el_employee_name:self.li_start_time})
            self.dict_end_time.update({el_employee_name:self.li_end_time})