student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0
for student_high_score in student_scores:
  if high_score <= student_high_score:
    high_score = student_high_score
# low_score = student_scores[0]
# for student_low_score in student_scores:
#   if low_score >= student_low_score:
#     low_score = student_low_score

print(f"The highest score in the class is: {high_score}")