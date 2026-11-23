student_marks = 90
student_attendance = 75
is_student = True

print("------STUDENT ELIGIBILITY CHECK------")

eligible = student_marks >= 85 and student_attendance >= 70
print("Eligible for scholarship :", eligible)

special_eligible = student_marks >= 90 or student_attendance >= 80
print("Eligible for special scholarship :", special_eligible)

not_student = not is_student
print("Is not a student :", not_student)