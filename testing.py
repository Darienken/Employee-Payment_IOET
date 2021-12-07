import unittest
import server as algorithms
from EmployeePayment_IOET import employee_payment_func

class class_testing_employees(unittest.TestCase):

    #test 1
    def test_init_dic(self):
        #Testing the dic that I want to get
        self.dic_result={ #What I want to get
        'RENE': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00\n'],
        'ASTRID': ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00\n'],
        'DIEGO': ['MO10:00-12:00', 'TU18:00-23:00', 'WE09:00-15:00', 'TH12:00-14:00', 'FR00:00-06:00', 'SA08:00-09:00', 'SU20:00-21:00\n'],
        'DARIEN': ['SA00:00-04:00', 'SU10:00-18:00\n'],
        'VIVI': ['MO08:00-09:00', 'WE10:00-18:00', 'FR20:00-21:00', 'SA10:00-12:00', 'SU08:00-09:00']
        }    
        
        #Looking if self.dic_result is equals to self.init_employees_dic
        self.assertEqual(self.dic_result,employees_dic.dic_employees)
    
    #test 2
    def test_hours_worked_dic(self):
        #Testing hours worked that I want to get
        self.dic_hours_worked={ #What I want to get
        'RENE': [2, 2, 2, 4, 1],
        'ASTRID': [2, 2, 1],
        'DIEGO': [2, 5, 6, 2, 6, 1, 1], 
        'DARIEN': [4, 8],
        'VIVI': [1, 8, 1, 2, 1]
        }
        
        #Looking for equals
        self.assertEqual(self.dic_hours_worked,employees_dic.calculate_hours(employees_dic.dic_employees))
    
    #test 3
    def test_days_worked_dic(self):
        #Testing days worked that I want to get
        self.dic_hours_worked={ #What I want to get
        'RENE': ['MO', 'TU', 'TH', 'SA', 'SU'],
        'ASTRID': ['MO', 'TH', 'SU'],
        'DIEGO': ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU'],
        'DARIEN': ['SA', 'SU'],
        'VIVI': ['MO', 'WE', 'FR', 'SA', 'SU']
        }
        
        #Looking for equals
        self.assertEqual(self.dic_hours_worked,employees_dic.calculate_days(employees_dic.dic_employees))
    
    #test 4
    def test_times_worked_dic(self):
        #Testing times worked that I want to get
        self.dic_times_start={ #What I want to get
        'RENE': ['10', '10', '01', '14', '20'],
        'ASTRID': ['10', '12', '20'],
        'DIEGO': ['10', '18', '09', '12', '00', '08', '20'],
        'DARIEN': ['00', '10'],
        'VIVI': ['08', '10', '20', '10', '08']
        }
        
        self.dic_times_end={ #What I want to get
        'RENE': ['12', '12', '03', '18', '21'],
        'ASTRID': ['12', '14', '21'],
        'DIEGO': ['12', '23', '15', '14', '06', '09', '21'],
        'DARIEN': ['04', '18'],
        'VIVI': ['09', '18', '21', '12', '09']
        }
        
        #Looking for equals
        self.assertEqual(self.dic_times_start,employees_dic.dict_start_time)
        self.assertEqual(self.dic_times_end,employees_dic.dict_end_time)
    
    #test 5
    def test_func_payments_dic(self):
        #Testing payments that I want to get
        self.dic_payments={ #What I want to get
        'RENE': 215,
        'ASTRID': 85,
        'DIEGO': 455,
        'DARIEN': 280,
        'VIVI': 235
        }
        
        #Looking for equals
        self.assertEqual(self.dic_payments,employee_payment_func(employees_txt))


if __name__ == '__main__':
    #Open file and get list
    with open("data.txt") as data_txt:
        employees_txt=data_txt.readlines()
    
    #Creating "class_employees" object 
    employees_dic=algorithms.class_employees(employees_txt)
    
    #Run main
    unittest.main()
    