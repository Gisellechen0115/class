#Class
'''why we need class
it allows ud logically group our data and functions in a way that's easy to reuse
and also easy to build upon if need be.

data and functions are associated with a specific class
we call those attributes and methods
'''
class Employee:
    
    num_of_emps = 0
    raise_amount= 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last +'@company.com' 
        
        Employee.num_of_emps += 1
    
    def fullname(self):     # 一定要給Argument    
        return '{}{}'.format(self.first, self.last)   
    
    def aplly_raise(self):
        #self.pay = int(self.pay * Employee.raise_amount)    #前面要加CLASS名稱
        self.pay = int(self.pay * self.raise_amount) 
print(Employee.num_of_emps)        
    #pass #in a statement and python will know that you just want to skip that for now
# this is a simple employee class with  no attributes or methods.
emp_1 = Employee('Giselle', 'Chen', 30000)
emp_2 = Employee('Test', 'User', 4000)


print(Employee.num_of_emps)
'''
emp_1.first = "Giselle"
emp_1.last = "Chen"
emp_1.email = "gisellechen@company.com"
emp_1.pay = 30000

emp_2.first = "Fiobe"
emp_2.last = "Lin"
emp_2.email = "fiobelin@company.com"
emp_2.pay = 35000

print(emp_1.pay)
print(emp_2.pay)
print(emp_1.email)
print(emp_2.email)
'''

#print('{}{}'.format(emp_1.first, emp_1.last))    #full name
#print(emp_1.fullname())  #這邊雖然沒給Argument﹑但他會自己帶入SELF
'''print(emp_1.__dict__)  #{'first': 'Giselle', 'last': 'Chen', 'pay': 30000, 'email': 'Giselle.Chen@company.com'}  
print(Employee.__dict__) 

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.06

#print(Employee.fullname(emp_1))
print(emp_1.raise_amount)  #1.04
print(emp_2.raise_amount)  #1.04
#print(emp_1.aplly_raise()) #NONE 

'''
'''