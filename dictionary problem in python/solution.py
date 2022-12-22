"""Program 8. Demonstrate the use of dictionary for
measuring students marks in five subjects and you have
to find the student having maximum and minimum
average marks.
"""
CODE:-
def Average(lst):
return sum(lst) / len(lst)
def whoIstopperOf(students):
avgOfStudents=dict()
for student,marks in students.items():
avgOfStudents.__setitem__(student,Average(marks))
print("\nAverage marks of students are :- ")
for s, m in avgOfStudents.items():print(s, m)
# now we have average of all students
# now just find max and min values
max_marks=0
min_marks=20
toppers=list()
loosers=list()
for student,marks in avgOfStudents.items():
if marks>max_marks:
toppers.clear()
toppers.append(student)
max_marks=marks
elif marks==max_marks:
toppers.append(student)
if marks<min_marks:
loosers.clear()
loosers.append(student)
min_marks=marks
elif marks==min_marks and marks!=20:
loosers.append(student)
print("\n\nToppers are :- ",toppers,"\nwith marks :-
",avgOfStudents[toppers[0]])
if len(loosers)!=0:
print("loosers are :- ",loosers,"\nwith marks :-
",avgOfStudents[loosers[0]])
else:
print("Everbody is a topper :) ")
students = {
'Sahil': [9, 18, 13, 12, 11], # 0,1,2,3,4 index in list are the subjects
'Mayank': [8, 8, 13, 15, 14],
'Jyoti': [19, 17, 13, 15, 13],
'Don': [19, 17, 13, 15, 13],
'Sachin': [9, 10, 15, 17, 11],
'Sonia': [11, 18, 13, 9, 16],
}
print("\nOriginal data provided is :- ")
for s,m in students.items():
print(s,m)print("")
whoIstopperOf(students)
