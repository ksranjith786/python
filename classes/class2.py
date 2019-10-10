
class Employee:
    totalEmployees = 0
    def __init__(self, fname, lname, id, gender, orgname, salary):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.gender = gender
        self.orgname = orgname
        self.salary = salary
        self.totalEmployees += 1

    def fullname(self):
        if self.gender in ["M", "m", "Male", "male"]:
            self.fullname = "Mr. {} {}".format(self.fname, self.lname)
        else:
            self.fullname = "Mrs. {} {}".format(self.fname, self.lname)
        
        return self.fullname

# Main()
emp1 = Employee("Ranjith", "KS", 786, "M", "NCR", 100000)
emp2 = Employee("Haritha", "G", 394672, "F", "TCS", 350000)


print(emp1.orgname)
print(emp1.fullname)
print(emp2.fullname())

print(Employee.fullname(emp1))
print(emp1.__dict__)

del emp1.gender

print(Employee.__dict__)
print(emp1.__dict__)
print(emp2.__dict__)
del emp1
