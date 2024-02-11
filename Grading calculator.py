# Byron Garcia
# This program will average 3 test scores and give you the average, it will also let you knwo if you passing or failing.
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.


exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum_grades = 0

for grade in grades:
  sum_grades = sum_grades + grade

grade_average = sum_grades / len(grades)

if grade_average >= 90:
    letter_grade = "A"
elif grade_average >= 80 and grade_average < 90:
    letter_grade = "B"
elif grade_average > 69 and grade_average < 80:
    letter_grade = "C"
elif grade_average <= 69 and grade_average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(grade_average))
print("Grade: " + letter_grade)

if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
