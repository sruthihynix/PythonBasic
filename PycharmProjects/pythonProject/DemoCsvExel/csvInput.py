
import csv

# 2 Opening or creating the file
with open('Academic Details.csv', 'w', newline="") as file:
    myFile = csv.writer(file)

    # 3 Writing the column headers
    myFile.writerow(["EducationLevel", "CourseStream", "UniversityInstituteBoard", \
                     "PassingOutYear", "MarksinPercentage"])

    # 4 Getting the number of rows to add
    noOfEducationLevels = int(input("Enter how many education levels you want: "))

    # 5 Using for loopDemo to write user input to the file
    for i in range(noOfEducationLevels):
        edu = input("Education " + str(i + 1) + ": Enter level(10th/12th/Graduation...): ")
        course = input("Education " + str(i + 1) + ": Enter course/stream: ")
        institute = input("Education " + str(i + 1) + ": Enter University/Institute/Board: ")
        year = input("Education " + str(i + 1) + ": Enter Passing Out Year: ")
        marks = input("Education " + str(i + 1) + ": Enter marks in percentage: ")
        myFile.writerow([edu, course, institute, year, marks])