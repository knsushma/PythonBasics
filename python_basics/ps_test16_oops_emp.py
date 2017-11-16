from ps_test16_oops_person import Person

class Employee(Person):
    def __init__(self,emp_id, f_name, l_name):
        self.employee_id = emp_id
        # self.first_name = f_name
        # self.last_name = l_name
        super().__init__(f_name,l_name) # calling base class method with derived object

    def get_info(self):
        print("Employee ID:",self.employee_id)
        super().get_info()

if __name__ == '__main__':
    e = Employee("1234","Ana","Charlie")
    e.get_info() # calls base class init funct, if no init in emp(derived) class


