#Uneditable code
student_scores = input("Input a list of student scores   ").split()
for n in range(0,  len(student_scores)):
    student_scores[n] = int(student_scores[n])


# To know the maximum value of the scores
maximum = 0
for max in student_scores :
    if max>maximum:
        maximum = max


#FINAL PRINT STATEMENT
print(f"The highest score is : {maximum}")



    
