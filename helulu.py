class Employee:
    employee_count={}
    total_employee=0
    def __init__(self,name,date,work_experience,weekly_work_hour=40,job=None):
        self.name,self.date,self.work_experience,self.weekly_work_hour=name,date,work_experience,weekly_work_hour
        if weekly_work_hour>60 or weekly_work_hour<40:
            print(f"{self.name} can not work for {weekly_work_hour} hours.")
            weekly_work_hour=40
        if job!=None:
            Employee.total_employee+=1
            if job in Employee.employee_count:
                Employee.employee_count[job]+=1
            else:
                Employee.employee_count[job]=1
    @classmethod
    def showDetails(cls):
        print("Company workforce:")
        print(f"Total Employee/s: {cls.total_employee}")
        for e,n in cls.employee_count.items():
            print(f"Total {e} Employee/s: {n}")
    def showEmployeeDetails(self,job=None):
        print(f"{job} Employee:\n"
        f"Name: {self.name}\n"
        f"ID: {self.id}\n"
        f"Joining Date: {self.date[8:]+'-'+self.date[5:7]+'-'+self.date[:4]}")
    def createID(self,job=None):
        return  f"{job}-{self.date[2:4]+self.date[5:7]+self.date[8:]}-{Employee.total_employee}"
class Programmer(Employee):
    designation_list= [ "Junior Software Engineer", "Software Engineer", "Senior Software Engineer", "Technical Lead" ]
    def __init__(self,name,date,work_experience,weekly_work_hour=40,job="Programmer"):
        super().__init__(name,date,work_experience,weekly_work_hour,job)
        index=3
        self.designation=""
        for i in [8,4,2,-1]:
            if work_experience>i:
                self.designation=Programmer.designation_list[index]
                break
            index-=1
        self.id=self.createProgrammerID()
    def showProgrammerDetails(self,job="Programmer"):
        super().showEmployeeDetails(job)
        print(f"Designation: {self.designation}\n"
        f"Salary: BDT {self.salary}")
    def calculateSalary(self):
        salary=[30000,45000,70000,120000]
        self.salary=salary[Programmer.designation_list.index(self.designation)]*(1.15**(2023-int(self.date[:4])))
    def createProgrammerID(self):
        return super().createID('P')
    def calculateOvertime(self):
        amount=(self.weekly_work_hour-40)*4*500
        if amount>0:
            print(f"{self.name} will get BDT {amount} overtime.")
            self.salary+=amount
        else:
            print(f"{self.name} will not get overtime.")
class HR(Employee):
    def __init__(self,name,date,work_experience,weekly_work_hour=40):
        super().__init__(name,date,work_experience,weekly_work_hour,job="HR")
        self.id=self.createHREmployeeID()
    def showHREmployeeDetails(self):
         super().showEmployeeDetails('HR')
    def createHREmployeeID(self):
        return super().createID('HR')
class InternProgrammer(Programmer):
    integer_count=0
    def __init__(self,name,date,intern_type="Unpaid"):
        super().__init__(name,date,0,40,None)
        InternProgrammer.integer_count+=1
        self.temp_id="Temp_"+str(InternProgrammer.integer_count)
        self.intern_type=intern_type
        y=2023-int(self.date[:4])
        m=8-int(self.date[5:7])
        d=17-int(self.date[8:])
        if d<0:
            d+=30
            m-=1
        if m<0:
            m+=12
            y-=1
        if y>0 or m>3:
            self.status="Eligible for promotion"
        else:
            self.status="Not Eligible for promotion"
    def showInternDetails(self):
        print("Intern (Programmer)")
        print(f"Name: {self.name}\n"
        f"ID: {self.temp_id}\n"
        f"Joining Date: {self.date}\n"
        f"Type: {self.intern_type}\n"
        f"Status: {self.status}")
    def promoteToProgrammer(self):
        if self.status=="Eligible for promotion":
            print(f"{self.name} is promoted!")
            return Programmer(self.name,"2023-08-17",0,40)
        else:
            print(f"{self.name} cannot be promoted.")
            return self
