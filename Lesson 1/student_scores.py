#Student Scores Analyzer

#Student Scores
score1=85
score2=72
score3=91
score4=64
score5=78

#display the scores of the five students

print("Student Scores:")
print( score1)
print( score2)
print( score3)
print( score4)  
print( score5)

#Determine the Grade and Status of each student
#student 1

if score1>=90:
    print("Student 1:",score1, "-Excellent -Passed")
elif score1>=80:
    print("Student 1:",score1, "-Very Good -Passed")
elif score1>=75:
    print("Student 1:",score1, "-Good -Passed")
else:
    print("Student 1:",score1, "-Failed")

#student 2

if score2>=90:
    print("Student 2:",score2, "-Excellent -Passed")
elif score2>=80:
    print("Student 2:",score2, "-Very Good -Passed")
elif score2>=75:
    print("Student 2:",score2, "-Good -Passed")
else:
    print("Student 2:",score2, "-Failed")

#student 3

if score3>=90:
    print("Student 3:",score3, "-Excellent -Passed")
elif score3>=80:
    print("Student 3:",score3, "-Very Good -Passed")
elif score3>=75:
    print("Student 3:",score3, "-Good -Passed")
else:
    print("Student 3:",score3, "-Failed")

#student 4

if score4>=90:
    print("Student 4:",score4, "-Excellent -Passed")
elif score4>=80:
    print("Student 4:",score4, "-Very Good -Passed")
elif score4>=75:
    print("Student 4:",score4, "-Good -Passed")
else:
    print("Student 4:",score4, "-Failed")

#student 5

if score5>=90:
    print("Student 5:",score5, "-Excellent -Passed")
elif score5>=80:
    print("Student 5:",score5, "-Very Good -Passed")
elif score5>=75:
    print("Student 5:",score5, "-Good -Passed")
else:
    print("Student 5:",score5, "-Failed")

#Calculate the Total Scores

total=score1+score2+score3+score4+score5
print("Total Score:",total)

#Calculate the Average Score
average=total/5
print("Average Score:",average)

#Highest Score

highest = score1

if score2>highest:
    highest = score2
if score3>highest:
    highest = score3
if score4>highest:
    highest = score4
if score5>highest:
    highest = score5

print("Highest Score:",highest)

#Lowest Score

lowest = score1

if score2<lowest:
    lowest = score2
if score3<lowest:
    lowest = score3
if score4<lowest:
    lowest = score4
if score5<lowest:
    lowest = score5

print("Lowest Score:",lowest)

#Count the students who passed and failed

passed = 0
failed = 0

if score1>=75:
    passed = passed + 1
else:
    failed = failed + 1

if score2>=75:
    passed = passed + 1
else:
    failed = failed + 1

if score3>=75:
    passed = passed + 1
else:
    failed = failed + 1

if score4>=75:
    passed = passed + 1
else:
    failed = failed + 1

if score5>=75:
    passed = passed + 1
else:
    failed = failed + 1

print("Passed:",passed)
print("Failed:",failed)

