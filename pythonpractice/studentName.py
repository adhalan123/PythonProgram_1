# create class send student information at run time and print that information
# and in another class print average based on this information and print student information along with average

class studentInfo:
    def __init__(self, Sname, mark):
        self.Sname1 = Sname
        self.mark1 = mark

    def display(self):
        print("This is student information from studentInfo class =", self.Sname1, self.mark1)
