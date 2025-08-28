from pythonpractice.studentName import studentInfo


class student(studentInfo):

    def __init__(self, Sname, mark1, grade):
        super().__init__(Sname, mark1)
        self.grade1 = grade

    def average(self):
        return sum(self.mark1) / len(self.mark1)

    def info(self):
        self.display()
        print("am grade from student class=", self.grade1)


obj = student("aaru", [34, 56, 24], "A")

print("student average information from student class =", obj.average())
obj.info()
