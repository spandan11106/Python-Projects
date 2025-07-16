from functions import read_file, write_file

prompt = "Command (help - for cmd info) : "

while True:
    user_action = input(prompt).strip().lower()

    if user_action.startswith("add"):
        task = user_action[4:]
        task += '\n'
        tasks = read_file()
        tasks.append(task)
        write_file(tasks)
        prompt = "Command: "

    elif 'show' in user_action or 'display' in user_action:
        tasks = read_file()

        if not tasks:
            print("No tasks available.")
        else:
            for index, item in enumerate(tasks):
                item = item.capitalize().strip()
                print(f"{index + 1}. {item}")

        prompt = "Command: "

    elif user_action.startswith('edit'):
        try:
            parts = user_action.split()
            if len(parts) == 2 and parts[1].isdigit():
                task_num = int(parts[1])
                tasks = read_file()

                if 1 <= task_num <= len(tasks):
                    print(f"Current task {task_num}: {tasks[task_num - 1].strip()}")
                    new_task = input("Enter edited task: ").strip()
                    tasks[task_num - 1] = new_task + '\n'
                    write_file(tasks)
                    print(f"Task {task_num} updated.")
                else:
                    print("Invalid task number.")
            else:
                print("Usage: edit <task number>")

        except Exception as e:
            print(f"Error editing task: {e}")

        prompt = "Command: "

    elif user_action.startswith('complete'):
        try:
            parts = user_action.split()
            if len(parts) == 2 and parts[1].isdigit():
                task_num = int(parts[1])
                tasks = read_file()

                if not tasks:
                    print("No tasks to complete.")
                    continue

                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    write_file(tasks)
                    print(f'Task {task_num} "{removed.strip()}" marked as done and removed.')
                else:
                    print("Invalid task number.")
            else:
                print("Usage: complete <task number>")

        except Exception as e:
            print(f"Error completing task: {e}")

        prompt = "Command: "

    elif 'clear' in user_action:
        write_file([])
        print("All tasks cleared.")
        prompt = "Command: "

    elif 'help' in user_action:
        print("Hi, these are some useful commands:")
        print("1. add <task description>  - Adds a task (e.g., add clean room)")
        print("2. show / display           - Shows all tasks.")
        print("3. edit <task number>       - Edits a specific task (e.g., edit 2).")
        print("4. complete <task number>   - Marks a task as done and removes it (e.g., complete 1).")
        print("5. clear                    - Removes all the tasks.")
        print("6. exit                     - Exits the program.")
        print("7. help                     - Shows this help menu.")
        prompt = "Command: "

    elif 'exit' in user_action:
        break

    else:
        print("Unknown command. Type 'help' for list of commands.")
        prompt = "Command: "

print("Bye!")
