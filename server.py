class employees:
    def __init__(self,employees_list):
        self.employees={}
        for employee in employees_list:
            self.index=employee.index("=")
            self.times=employee.replace("=",",")
            self.timess=self.times.split(",")
            self.employees.update({employee[:self.index]:self.timess[1:]})
    
    def calculate_hours(self):
        self.employees_hours={}
        for employee in self.employees:
            self.employee_data=self.employees.get(employee)
            self.worked_hours=[]
            self.employees_hours.update({employee:self.worked_hours})
            for hours in self.employee_data:
                self.start=hours[2:4]
                self.end=hours[8:10]
                self.worked_hours.append(int(self.end)-int(self.start))
        return self.employees_hours
    
    def calculate_days(self):
        self.employees_days={}
        for employee in self.employees:
            self.employee_data=self.employees.get(employee)
            self.worked_days=[]
            self.employees_days.update({employee:self.worked_days})
            for days in self.employee_data:
                self.worked_days.append(days[:2])
        return self.employees_days
    
    def calculate_time(self):
        week_days=["MO", "TU", "WE", "TH", "FR"]
        weekend_days=["SA", "SU"]
        self.amount_to_paid={}
        
        for employee in self.employees:
            self.hours_for_daytime=[]
            self.employee_data=self.employees.get(employee)
            
            for day in week_days:
                if day in self.employees_days.get(employee):
                    self.index=self.employees_days.get(employee).index(day)
                    self.hours=self.employees_hours.get(employee)
                    self.employee_hours=self.hours[self.index]
                    self.data=self.employee_data[self.index]
                    self.start=self.data[2:4]
                    self.end=self.data[8:10]
                    if int(self.start) >= 0 and int(self.end) <= 9:
                        self.hours_for_daytime.append(self.employee_hours*25)
                    elif int(self.start) >= 9 and int(self.end) <= 18:
                        self.hours_for_daytime.append(self.employee_hours*15)
                    elif int(self.start) >= 18 and int(self.end) <= 24:
                        self.hours_for_daytime.append(self.employee_hours*20)
            for day in weekend_days:
                if day in self.employees_days.get(employee):
                    self.index=self.employees_days.get(employee).index(day)
                    self.hours=self.employees_hours.get(employee)
                    self.employee_hours=self.hours[self.index]
                    self.data=self.employee_data[self.index]
                    self.start=self.data[2:4]
                    self.end=self.data[8:10]
                    if int(self.start) >= 0 and int(self.end) <= 9:
                        self.hours_for_daytime.append(self.employee_hours*30)
                    elif int(self.start) >= 9 and int(self.end) <= 18:
                        self.hours_for_daytime.append(self.employee_hours*20)
                    elif int(self.start) >= 18 and int(self.end) <= 24:
                        self.hours_for_daytime.append(self.employee_hours*25)
            self.amount_to_paid.update({employee:self.hours_for_daytime})
        return self.amount_to_paid