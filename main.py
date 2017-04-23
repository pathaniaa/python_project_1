"""   This is a Launcher Program!!
 Designed by: Pankaj Pathaniaa
"""


print "Hello welcome to my Python projects \n\
Here you can run my projects ! "
print
print
print "List of My projects: \n\
A--> Student Becomes Teacher \n\
B--> Battleship \n\
C--> Exam Statistics"
print
print
choice = raw_input("Choose a program from above list to run !(A,B or C):").upper()
if choice == "A":
    import student_teacher  #importing file
    student_teacher.main() # calling main() function from the file
elif choice == "B":
    import battleship
    battleship.main()
elif choice == "C":
    import exam_status
    exam_status.main()

else:
    print "Choose correct option from above list i.e A,B or C"






