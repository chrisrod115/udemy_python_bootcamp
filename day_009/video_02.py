"""student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
  score = student_scores[student]
  if score>90:
    student_grades[student] = "Outstanding"
  elif score >80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)


"""
from replit import clear

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
def student_results():
  for name in student_scores:
    grade = student_scores[name]
    if grade>90:
      student_grades[name] = "Outstanding"
    elif grade >80:
      student_grades[name] = "Exceeds Expectations"
    elif grade > 70:
      student_grades[name] = "Acceptable"
    else:
      student_grades[name] = "Fail"
  print(student_grades)
    
student_results()