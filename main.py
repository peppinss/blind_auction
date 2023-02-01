student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


student_grades = {}
for x in student_scores:
    uga = int(student_scores[x])
    if uga >= 91:
        student_grades[x] = "Outstanding"
    elif uga >= 81:
        student_grades[x] = "Exceeds Expectations"
    elif uga >= 71:
        student_grades[x] = "Acceptable"
    else:
        student_grades[x] = "Fail"



print(student_grades)