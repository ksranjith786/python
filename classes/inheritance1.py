
class Employee:
    totalEmployees = 0
    def __init__(self, fname, lname, id, gender = 'M', orgName = "", salary = 50000):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.gender = gender
        self.orgName = orgName
        self.salary = salary
        self.totalEmployees += 1

    def fullname(self):
        if self.gender in ["M", "m", "Male", "male"]:
            self.fullname = "Mr. {} {}".format(self.fname, self.lname)
        else:
            self.fullname = "Mrs. {} {}".format(self.fname, self.lname)
        
        return self.fullname

    def emailid(myemp):
        return "{}.{}@{}.com".format(myemp.fname, myemp.lname, myemp.orgName)

class Manager(Employee):
    def __init__(mgr, fname, lname, id, gender, orgName, salary, projectName):
        super().__init__(fname, lname, id, gender, orgName, salary)
        mgr.projectName = projectName

class Tester(Manager):
    def __init__(self, fname, lname, id, gender, orgName, salary, projectName, teamName):
        Manager.__init__(self, fname, lname, id, gender, orgName, salary, projectName)
        self.teamName = teamName

class Developer(Manager):
    def __init__(dev, fname, lname, id, gender, orgName, salary, projectName, teamName):
        super().__init__(fname, lname, id, gender, orgName, salary, projectName)
        dev.teamName = teamName

# Main()
emp1 = Employee("Ranjith", "KS", 786, "M", "NCR", 100000)
emp2 = Employee("Haritha", "G", 394672, "F", "TCS")

mgr1 = Manager("Manager1", "MM", 123, 'M', "TCS", 300000, "Flexi")

dev1 = Developer("Ranjith", "KS", 786, "M", "NCR", 100000, "Retail", "AMS")
test1 = Tester("Haritha", "G", 394672, "F", "TCS", 50000, "Telecom", "TNMS")

print(dev1.__dict__)
print(test1.__dict__)