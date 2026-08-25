class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name=name
        self.emp_id=emp_id
        self.base_salary=base_salary
    def calculate_pay(self):
        return self.base_salary
    def get_details(self):
        return '員工：'+ self.name +' ('+'ID:'+ self.emp_id +')'


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        super().__init__(name, emp_id, base_salary)
        self.bonus=bonus
    def calculate_pay(self):
        return self.base_salary+self.bonus
    
class HourlyEmployee(Employee):
    def __init__(self,name,emp_id,hourly_rate,hours_worked):
        super().__init__(name,emp_id,0)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked        
        
    def calculate_pay(self):
        return self.hourly_rate*self.hours_worked

def process_company_payroll(employees, performance_ratings):
    total_payment=0
    for employee in employees:
        emp_pay=0
        if employee.emp_id not in performance_ratings:
            performance_ratings[employee.emp_id]='B'
            
        if performance_ratings[employee.emp_id]=='A':
            if type(employee) == FullTimeEmployee:
                employee.bonus *=1.2
                employee.bonus = int(employee.bonus)
                print(employee.name+'績效優異！獎金提高為'+ str(employee.bonus)+' 元。')
                emp_pay=employee.calculate_pay()
            else:
                employee.hourly_rate +=10
                print(employee.name+'績效優異！時薪調升'+ str(employee.hourly_rate)+' 元。')
                emp_pay=employee.calculate_pay()
        if performance_ratings[employee.emp_id]=='C':
            emp_pay = employee.calculate_pay() * 0.9
            print(employee.name+'績效待加強，本月實領薪資打9折。')
        if performance_ratings[employee.emp_id]=='B':
            emp_pay = employee.calculate_pay()
        total_payment += emp_pay
        
    print('公司本次總計支出薪資：' + str(total_payment) + ' 元')

Emily=FullTimeEmployee('Emily','FT001',50000,10000)
David=FullTimeEmployee('David','FT002',45000,8000)
Helen=HourlyEmployee('Helen','HE001',200,120)
Jack=HourlyEmployee('Jack','HE002',180,150)
performance_ratings={'FT001':'A','FT002':'C','HE001':'A'}
process_company_payroll([Emily,David,Helen,Jack],performance_ratings)