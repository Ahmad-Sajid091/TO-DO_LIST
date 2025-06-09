def main():
    tasks = []

    while True:
        print("\n---TO-DO LIST---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as DONE")
        print("4. Exit")

        choice = input("\nEnter your choice: ")
       


        if choice == "1":
            print()
            n_tasks = int(input("How many task you want to input: "))
            for i in range(n_tasks):
                task = input("Enter your task: ")
                tasks.append({"task" : task, "Done":False})
                print("TASK ADDED!")

        elif choice == "2":
            print("\nTasks:")
            if len(tasks) == 0:
                print("no task added yet")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["Done"] else "NOT Done"
                    print(f"{index + 1 }.{task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task Number to mark as DONE ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["Done"] = True
                print("Task marked as Done")
            else:
                print("Invalid Task Number")

        elif choice == "4":
            print("Exiting the Program")
            break
        else:
            print("Invalid choise ")

        



main()
