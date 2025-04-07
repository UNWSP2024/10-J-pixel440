class Student:
    def check_pass_fail(self):
        if self.marks>=60:
            return True
        else:
            return False

    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

student1=Student("Josh",93)
student2=Student("Sam",10)
did_pass=student1.check_pass_fail()
print(did_pass)
did_pass=student2.check_pass_fail()
print(did_pass)
