tasks = []#Empty list created
while True:

    print("\n----- TO DO LIST -----")#Display Menu
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = int(input("Enter your choice: "))#Get the choice from user

    if choice == 1:
        task = input("Enter Task: ")#Add task
        tasks.append(task)
        print("Task Added Successfully")

    elif choice == 2:
        print("\nYour Tasks:")#view tasks
        if len(tasks) == 0:
            print("No Tasks Available")
        else:
            for task in tasks:
                print(task)

    elif choice == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")