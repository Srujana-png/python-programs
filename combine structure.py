#combine structure
class  employee:
    def __init__(self,name):
        self.name=name
    def works(self):
        print("employee's do the work")
class manager(employee):
    def work(self):
        print(self.name,"the manager manages the team")
class tester(employee):
    def work(self):
        print(self.name,"the tester test the code")
def employee_details(emp):
    emp.work()
M=manager("girls")
T=tester("boys")
employee_details(M)
employee_details(T)
              
