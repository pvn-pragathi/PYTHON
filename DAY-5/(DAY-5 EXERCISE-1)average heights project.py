#Uneditable code
student_heights = input("Input a list of student heights   ").split()
for n in range(0,  len(student_heights)):
    student_heights[n] = int(student_heights[n])


# To know the number of students
count = 0
for counts in student_heights :
    count += 1


# To know the sum of all heights of studnts
sum = 0
for sums in student_heights :
    sum += int(sums)


# To know the average of student heights
average  = int(sum / count)


#FINAL PRINT STATEMENT
print(f"Average of the student heights is {average}")







