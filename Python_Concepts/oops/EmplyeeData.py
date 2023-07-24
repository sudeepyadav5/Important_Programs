class EmployeeDetails:
    def __init__(self,schoolname):
        self.schoolname = schoolname

    def empDetails(self, name, age):
        print("Student Name is ", name)
        print("Student age is ", age)

    def schoolName(self):
        print("Student School Name is ",self.schoolname)


# emp = EmployeeDetails("SCET")
# emp.empDetails("Sudeep",10)
# emp.schoolName()


