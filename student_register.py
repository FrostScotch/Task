#===================Compulsory Task 1================================
#Program captures the number of student registered for an exam
#A register of registered students as per student numbers is created
#Register is created and as stored as text file "reg_form"

number_of_students = int(input("Enter the total number of registered students: "))
f = open('reg_form.txt', 'w')

#Heading for the student register
f.write("=========Student Register========="+"\n"+"\n")

# A for loop is used to request the user to enter each of the students' ID
# Each student ID is written in the register including a place to sign student
for i in range (0, number_of_students):
    student_id = input("Enter student ID: ")
    f.write(student_id)
    f.write("..........................." + "\n"+"\n")
f.close()