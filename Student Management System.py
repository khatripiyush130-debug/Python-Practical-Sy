student_names=[]
student_marks=[]

while True:
    print("="*40)
    print("STUDENT MARKS MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Insert Student Record")
    print("2. Delete Student Record")
    print("3. Update Student Record")
    print("4. Traverse / Display All Records")
    print("5. Search Student")
    print("6. Show Statistics")
    print("7. Exit")
    print("="*40)
    
    choice=input("Enter your choice(1-7): ").strip()
    
    if choice=='1':
        name=input("Enter Student name: ").strip()
        
        if name in student_names:
            print(f"Student '{name}' already exists! Use update option instead.\n")
        else:
            marks=float(input(f"Enter marks for {name}: "))
            student_names.append(name)
            student_marks.append(marks)
            print(f"Record for '{name}' Instead successfully.\n")
    
    elif choice=='2':
        name=input("Enter Student name to Delete:").strip()
        
        if name in student_names:
            index=student_names.index(name)
            student_names.pop(index)
            student_marks.pop(index)
            print(f"Records for '{name}' deleted successfully.\n")