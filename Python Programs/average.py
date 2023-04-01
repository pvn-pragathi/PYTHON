# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights.\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#Sum of observations

total_heights = 0
for sum in student_heights:
   total_heights += sum

number_heights = 0
for number in student_heights:
    number_heights += 1
    
average = int(total_heights/ number_heights)

print(f"The average is {average}")
