total = 0
sum_credit = 0
gpa = 0

# enter how many courser in loop
num = int(input("How many coursers do you have in this semester: "))

# list of gpa scores
score = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0}

# for loop courser gpa
for course in range(num):
    grade = input(f'What is grade {course + 1}: ').upper()
    # ask course's credit
    credit = int(input(f'What is credit in this course:'))
    total = total + score[grade]*credit
    sum_credit = sum_credit + credit
gpa = total / sum_credit
print(f'The student gpa is {gpa}')
