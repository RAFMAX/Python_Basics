class Employee:
    def __init__(self, fname, lname, asalary):
        self.fname = fname
        self.lname = lname
        self.asalary = int(asalary)
    def give_raise(self, added=5000):
        self.asalary += int(added)
        return self.asalary

