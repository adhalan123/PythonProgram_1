# create student information using different datatype

name = "Aaru"  # string
age = 27  # int
grade = [435, 626, 662]  # List
passed = True  # boolean

StudentInformation = {"name": name,
                      "age": age,
                      "grade": grade,
                      "passStatus": passed}

print("Student-info: ", StudentInformation)

# condition to check pass or failed based on average

studentAverage = sum(StudentInformation["grade"]) / len(StudentInformation["grade"])

print(studentAverage)

if studentAverage > 90:
    print(studentAverage, "=Grade A")
elif studentAverage < 90:
    print(studentAverage, "=Grade B")

# Step 3a: Use a for loop to print each grade
# for loop
print("Grades:")
for i in StudentInformation["grade"]:
    print(i)

# Use a while loop to entering 3 student names

studentName = []
count = 0

while count < 3:
    name = input("enter name")
    studentName.append(name)
    count += 1
print("student names:", studentName)


# Create a function to calculate average grade

def averageGeade(grade1):
    return sum(grade1) / len(grade1)


print("average of numbers", averageGeade([23, 56, 35]))
