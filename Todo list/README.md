# 📝 To-Do List App (CLI)

A simple and beginner-friendly command-line to-do list manager built using Python. This project is designed to help you learn practical Python skills while managing tasks efficiently from your terminal.

---

## 🚀 Features

- ✅ Add tasks interactively from the CLI  
- ✅ View all tasks with numbers  
- ✅ Edit tasks by task number  
- ✅ Mark tasks as completed (removes them)  
- ✅ Clear all tasks  
- ✅ Help menu with usage instructions  
- ✅ Persistent data between sessions (stored in `task.txt`)  
- ✅ Modular codebase with reusable functions in `functions.py`  

---

## 🧠 Concepts Practiced

- Writing reusable functions & default parameters  
- Organizing code with modules (`functions.py`, `main.py`)  
- File handling in Python (`open`, `read/write`, exception handling`)  
- Command parsing through string inspection  
- CLI interaction using `input()` and control structures  

---

## ⚙️ How to Use

### ⚡ Interactive Commands (prompt-based)

Run the program:
python main.py

Then use these interactive commands at the prompt:

<pre>
    add Do homework ➜ Adds a new task
    show ➜ Displays the list of tasks
    edit 2 ➜ Edits the 2nd task
    complete 1 ➜ Completes (removes) the 1st task
    clear ➜ Removes all tasks
    help ➜ Shows the help menu
    exit ➜ Exits the program
</pre>

---

## 📂 Folder Structure

<pre> 
        Todo list/
    ├── README.md <- You are reading this.
    ├── main.py <- Main CLI application logic
    ├── functions.py <- Helper functions for file I/O
    └── task.txt <- Stores all tasks (auto-generated if missing)
</pre>

---

## 🔍 Future Enhancements

- [ ] Add task priority levels (Low / Medium / High)  
- [ ] Include due dates for tasks  
- [ ] Color-coded output using `colorama`  
- [ ] Save tasks in JSON or CSV format  
- [ ] Migrate from `input()` to `argparse` for true CLI commands  

---

## 🧠 Note

🛠️ This project is part of my Python learning. It focuses on:

- Python input/output (I/O)  
- Working with files  
- Structuring a Python project  
- Developing logic and writing clean code  

Feel free to fork and build on top of it for your own use case!

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).