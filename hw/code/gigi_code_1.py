class employee:
    def __init__(self,name,emp_id,base_salary):
        self.name=name
        self.emp_id=emp_id
        self.base_salary=base_salary

    def calculate_pay(self):
        return self.base_salary
    def get_detail(self):
        return '員工：'+ self.name + 'ID:'+ self.emp_id

class FullTimeEmployee(employee):
    def __init__(self,name,emp_id,base_salary,bonus):
        super().__init__(name,emp_id,base_salary)
        self.bonus=bonus

    def calculate_pay(self):
        return self.base_salary+self.bonus
class HourlyEmployee(employee):
    def __init__(self,name,emp_id,hourly_rate,hours_worked):
        super().__init__(name,emp_id,0)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_pay(self):
        return self.hourly_rate*self.hours_worked

def process_company_payroll(employees,performance_ratings):
    total_salary=0
    for employee in employees:
        rating=performance_ratings.get(employee.emp_id,'B')
        if rating =='A':
            if isinstance(employee,FullTimeEmployee):
                employee.bonus=int(employee.bonus*1.2)
                print(employee.name+'績效優異！時薪調升 10 '+'元。')
            elif isinstance(employee,HourlyEmployee):
                employee.hourly_rate+=10
                print(employee.name+'績效優異！時薪調升 10 '+str(employee.hourly_rate)+'元。')
        salary=employee.calculate_pay()
        if rating =='C':
            salary=int(salary*0.9)
            print(employee.name +'績效待加強，本月實領薪資打 9 折。')
    total_salary+=salary
    print(employee.get_detail() + '績效：'+ rating+'，實領薪資：'+str(employee.salary) +'元。')
    print('公司本次總計支出薪資：' + str(total_salary) + ' 元')

Emily=FullTimeEmployee('Emily','FT001',50000,10000)
David=FullTimeEmployee('David','FT002',45000,8000)
Helen=HourlyEmployee('Helen','HE001',200,120)
Jack=HourlyEmployee('Jack','HE002',180,150)
performance_ratings={'FT001':'A','FT002':'C','HE001':'A'}
process_company_payroll([Emily,David,Helen,Jack],performance_ratings)
performance_ratings={'FT001':'A','FT002':'A','HE001':'B'}