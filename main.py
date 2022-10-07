students = []


def createStudent():
  name = input("Enter student name: ")
  students.append(name)


def updateStudent():
  name = input("Enter student name: ")
  index = students.index(name)
  newName = input("Enter new name: ")
  students[index] = newName


def deleteStudent():
  print("delete student")


def listAllStudent():
  print("\n------------------------\n")
  print("List of all students")
  print("\n------------------------\n")
  print(students)


choice = 0

while choice != 5:
  print("Operations")
  print("1. Create a student")
  print("2. Update a student")
  print("3. Delete a student")
  print("4. List all students")
  print("5. Exit")
  print("\n-------------------------\n")
  choice = int(input("Input your choice: "))

  if choice == 1:
    createStudent()
  elif choice == 2:
    updateStudent()
  elif choice == 3:
    deleteStudent()
  elif choice == 4:
    listAllStudent()
  elif choice == 5:
    print("Bye")
  else:
    print("Wrong choice")
