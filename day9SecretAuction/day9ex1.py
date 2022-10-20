# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 18:02:38 2022

@author: victo
"""

# here i am making a silent dictionary
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
letter = ""
#TODO-2: Write your code below to add the grades to student_grades.👇
#comment: iterates through each key to assign the proper grade!
for key in student_scores:
  if student_scores[key] >= 91:
    letter = "Outstanding"
  elif student_scores[key] >= 81:
    letter = "Exceeds Expectations"
  elif student_scores[key] >= 71:
    letter = "Acceptable"
  else:
    letter = "Fail"
  student_grades[key] = letter
    

# 🚨 Don't change the code below 👇
print(student_grades)
