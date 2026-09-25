""" Student Management System Functions:-
     1. add student
     2. show student
     3. search student
     4. delete student """



students=[]
password=12345

while True:
     user=int(input("Enter Your password := "))

     if user==password:
          print("==================== Web page login successfull =====================")

          break

     else:
          print("Invalid password try again")




# add student
def add_student():
    name = input("Enter Your Name:=")
    roll_number = int(input("Enter Your roll number:="))
    course = input("Enter Your course:=")

    students.append({
         "name": name,
         "roll_number": roll_number,
         "course": course
         })

    file = open("students.txt","w")
    for student in students:
         
      file.write(
          f"name: {student["name"]}, "
           f"roll_number: {student["roll_number"]}, "
           f"course: {student["course"]}\n"
      )

    file.close()
    print("Student Added Successfully")

# show student

def show_student():
     file = open("students.txt", "r")
     data = file.read()
     print(data)

     file.close()

# search student

def search_student():
     roll_number = int(input("Enter Your roll number:="))

     found = False

     for student in students:
         if student["roll_number"] == roll_number:
             print(student)
             found = True
             break

         if not found:
              print("Student not found")


# delete student

def delete_student():
     roll_number = int(input("Enter your roll number:="))

     found = False

     for student in students:
          if student["roll_number"] == roll_number:
               students.remove(student)
               file = open("students.txt", "w")
               for student in students:
                    file.write(
                         f"name: {student["name"]}, "
                         f"roll_number: {student["roll_number"]}, "
                         f"course: {student["course"]}\n"
                    )

                    file.close()

               print("deleted successfull")
               found = True
               break
     if not found:
          print("student not found")

while True:
     print("1. Add Student")
     print("2. Show Student")
     print("3. Search Student")
     print("4. Delete Student")
     print("5. Exit")

     break

while True:
     choice = int(input("Enter your choice:="))
     
     if choice == 1: 
          add_student()

     elif choice == 2:
          show_student()

     elif choice == 3:
          search_student()

     elif choice == 4:
          delete_student()

          break

     else:
          print("===========  Log Out  ==========")