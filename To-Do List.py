def choice():
    tasks = []

    while True:
        print("\n ====== To-Do List======")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Enter your choice : ")

        if choice == '1' :
            print()
            n_tasks = int(input("\n How many tasks will you add : "))

            for i in range(n_tasks):
                task  = input("Enter the Task : ")
                tasks.append({"task" : task })
                print("Task Added !!")

        elif choice == '2':
            print(tasks)

        elif choice == '3':
            task_index = int(input("Enter the task number to be marked as done : ")) - 1
            if 0<= task_index< len(tasks):
                print("Task marked as done")
            else:
                print("Task number invalid")

        elif choice == '4':
            print("Exiting")
            break
        else:
            print("Invalid choice !!!!")
            
            
            
print(choice())