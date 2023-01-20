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

def grade_checker(score):
    for score in student_scores:
        check = student_scores[score]
        if check >= 91:
            student_grades[f"{score}"] = "Outstanding"
        elif (check>=81) and (check<90):
            student_grades[f"{score}"] = "Exceeds Expectations"
        elif (check>=71) and (check<80):
            student_grades[f"{score}"] = "Acceptable"
        else:
            student_grades[f"{score}"] = "Fail"
    

grade_checker(score=student_scores)





    

# 🚨 Don't change the code below 👇
print(student_grades)


