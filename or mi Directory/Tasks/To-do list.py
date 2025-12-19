def todo_list():
    tasks = []

    while True:
        print("1. Добавить задачу")
        print("2. Посмотреть задачи")
        print("3. Удалить задачу")
        print("4. Выход")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a task: ")
            tasks.append(task)
        elif choice == '2':
            if tasks:
                print("Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks.")
        elif choice == '3':
            if tasks:
                task = input("Enter the task to remove: ")
                if task in tasks:
                    tasks.remove(task)
                    print("Task removed.")
                else:
                    print("Task not found.")
            else:
                print("No tasks.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

todo_list()