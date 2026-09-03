class employee:
    def __init__(self,name,emp_id,base_salary):
        self.name=name
        self.emp_id=emp_id
        self.base_salary=base_salary

    def calculate_pay(self):
        #print(self.base_salary)
        return self.base_salary

Emily=employee('Emily','FT001',50000)
Emily.calculate_pay()