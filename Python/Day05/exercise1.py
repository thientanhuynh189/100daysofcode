student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

count = 0
total = 0
for student_height in student_heights:
  count += 1
  total += student_height
result = round(total / count)
print(result)
