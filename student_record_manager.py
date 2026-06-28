students=[]

def add_student():
    name=input("Enter student name: ")
    student_id=input("Enter id: ")
    age=input("Enter age: ")
    course=input("Enter course: ")
    
    student={"name":name,"age":age,"course":course,"id":student_id}
    
    students.append(student)
    print("Student added successfully")
    return
    
def view_students():
        for student in students:
            print(f"Name: {student['name']}")
            print(f"Id: {student['id']}")
            print(f"Age: {student['age']}")
            print(f"course: {student['course']}")
            
def search_student():
    search=input("Enter student name or id: ")
    for student in students:
        if student["name"]==search or student["id"]==search:
            print(f"Name: {student['name']}")
            print(f"Id: {student['id']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            return
    print("Student not found")        
            
def delete_student():
    search=input("Enter student name or id to delete: ")
    for student in students:
        if student["name"]==search or student["id"]==search:
            students.remove(student)
            print("Student removed successfully")
            return
    print("Student not found") 
        
print("*"*40)
print("    Welcome to Student Record Manager    ")
print("*"*40)
 
while True:
      print("\nMenu")
      print("1.Add student")
      print("2.View student")
      print("3.Search student")
      print("4.Delete student")
      print("5.Exit")
      c=(input("\nEnter your choice: ")) 
      if c=="1":
           add_student()
      elif c=="2":
           view_students()
      elif c=="3":
           search_student()
      elif c=="4":
           delete_student()
      elif c=="5":
           print("Thank you for using Student Record Manager!")
           break    
      else:
           print("Invalid choice! Please try again.")