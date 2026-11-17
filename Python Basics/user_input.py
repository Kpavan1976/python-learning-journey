name = input("Enter your name: ")

sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 marks: "))

total = sub1 + sub2 + sub3

avg = total / 3

print("----STUDENT RESULT----")

print("Student Name: ", name)
print("Sub1 Marks: ", sub1)
print("Sub2 Marks: ", sub2)
print("Sub3 Marks: ", sub3)

print("Total Marks: ", total)
print("Avg Marks: ", avg)

# f-strings
print(f"Student Name: {name}")
print(f"Sub1: {sub1}")
print(f"Sub2: {sub2}")
print(f"Sub3: {sub3}")

print(f"Total Marks: {total}")
print(f"Average Marks: {avg:.2f}")