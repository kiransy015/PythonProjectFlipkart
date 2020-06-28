class Organization():
    companyname = 'Nokia'

class Employee(Organization):
    def __init__(self,EmployeeName):
        self.empname=EmployeeName

    def applyleave(self,startdate,enddate):
        print('Applying leave for employee :',self.empname,' Organization',Organization.companyname)
        Manager.ApproveLeave(self)

    def modifyleave(self,startdate,enddate):
        print('Modifying leave for employee :', self.empname, ' Organization', Organization.companyname)
        Manager.ApproveLeave(self)

    def cancelleave(self,startdate,enddate):
        print('Cancelling leave for employee :', self.empname, ' Organization', Organization.companyname)
        Manager.ApproveLeave(self)

class Manager(Employee):
    def __init__(self,EmployeeName):
        Employee.__init__(self,EmployeeName)

    def ApproveLeave(self):
        print('Approving leave for employee :', self.empname, ' Organization', Organization.companyname)

class TL(Employee):
    def __init__(self,EmployeeName):
        Employee.__init__(self,EmployeeName)

class Engg(Employee):
    def __init__(self,EmployeeName):
        Employee.__init__(self,EmployeeName)

print('----------By Employee --------------')
E1 = Engg('Ram')
E1.applyleave('01/01/2019','01/09/2019')
E1.modifyleave('01/01/2019','01/09/2019')
E1.cancelleave('01/01/2019','01/09/2019')

print('----------By Teamlead --------------')
T1 = TL('Sam')
T1.applyleave('01/01/2019','01/09/2019')
T1.modifyleave('01/01/2019','01/09/2019')
T1.cancelleave('01/01/2019','01/09/2019')

print('----------By Manager --------------')
M1 = Manager('Jam')
M1.applyleave('01/01/2019','01/09/2019')
M1.modifyleave('01/01/2019','01/09/2019')
M1.cancelleave('01/01/2019','01/09/2019')




