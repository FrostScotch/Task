#===================Student Register================================
#Program captures students registered for an exam

try:
    number_of_students = int(input("Enter the total number of registered students: "))
except ValueError:
    print("That's not a valid number of students!")
else:
    try:
        f = open('reg_form.txt', 'a')
    except IOError:
        print("Unable to open the file")
    else:
        #Heading for the student register
        f.write("=========Student Register========="+"\n"+"\n")

        # A for loop is used to request the user to enter each of the students' ID
        # Each student ID is written in the register including a place to sign the student
        for i in range (0, number_of_students):
            student_id = input("Enter student ID: ")
            f.write(student_id)
            f.write("..........................." + "\n"+"\n")
        f.close()
