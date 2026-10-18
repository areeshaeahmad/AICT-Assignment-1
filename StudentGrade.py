
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
print("Welcome,", name)
print("Your marks are:", marks)
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade)
print("Program finished!")

