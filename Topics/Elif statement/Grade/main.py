student_marks = int(input())
maximum = int(input())

mark = maximum // student_marks

if 0.9 >= mark <= 1:
    print("A")
elif 0.8 >= mark <= 0.9:
    print("B")
elif 0.7 >= mark <= 0.8:
    print("C")
elif 0.6 >= mark <= 0.7:
    print("D")
else:
    print("F")
