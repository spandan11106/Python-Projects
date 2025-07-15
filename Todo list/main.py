prompt = "Command (help - for cmd info) : "

while True:
    user_action = input(prompt).strip().lower()

    if user_action.startswith("add"):
        task = user_action[4 : ]
        task += '\n'

        try:
            with open('task.txt', 'r') as file:
                tasks = file.readlines()

        except FileNotFoundError:
            tasks = []
        tasks.append(task)
        with open('task.txt', 'w') as file:
            file.writelines(tasks)

        prompt = "Command: "

    elif 'show' in user_action or 'display' in user_action:
        try:
            with open('task.txt', 'r') as file:
                tasks = file.readlines()

            if not tasks:
                print("No tasks available.")
            else:
                for index, item in enumerate(tasks):
                    item = item.capitalize().strip()
                    print(f"{index + 1}. {item}")

        except FileNotFoundError:
            print("No tasks file found.")

        prompt = "Command: "

    elif 'edit' in user_action:
        try:
            with open('task.txt', 'r') as file:
                tasks = file.readlines()

            num = int(input("Which task do you want to edit: "))
            tasks[num - 1] = input("Enter edited task: ") + "\n"

            with open('task.txt', 'w') as file:
                file.writelines(tasks)

        except (IndexError, ValueError):
            print("Invalid task number.")

        except FileNotFoundError:
            print("Task file not found.")

        prompt = "Command: "

    elif 'complete' in user_action:
        try:
            with open('task.txt', 'r') as file:
                tasks = file.readlines()

            if not tasks:
                print("No tasks to complete.")
                continue

            for index, item in enumerate(tasks):
                item = item.capitalize().strip()
                print(f"{index + 1}. {item}")

            num = int(input("Which task did you complete: "))
            tasks.pop(num - 1)
            print("Task marked as done.")

            with open('task.txt', 'w') as file:
                file.writelines(tasks)

        except (IndexError, ValueError):
            print("Invalid task number.")

        except FileNotFoundError:
            print("Task file not found.")

        prompt = "Command: "

    elif 'clear' in user_action:
        with open('task.txt', 'w'):
            pass
        print("All tasks cleared.")

        prompt = "Command: "

    elif 'help' in user_action:
        print("Hi, these are some useful commands:")
        print("1. add - Adds a task.")
        print("2. show/display - Shows all tasks.")
        print("3. edit - Helps edit a task.")
        print("4. complete - Marks a task as done and removes it.")
        print("5. clear - Removes all the tasks.")
        print("6. exit - Exits the program.")
        print("7. help - Shows this help menu.")

        prompt = "Command: "

    elif 'exit' in user_action:
        break

    else:
        print("Unknown command. Type 'help' for list of commands.")
        prompt = "Command: "

print("Bye!")
