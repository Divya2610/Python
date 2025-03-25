student_heights = input("Input a list of student height").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_heights = sum(student_heights)
number_student_heights = len(student_heights)
average_height = round(total_heights / number_student_heights)
print(average_height)

