import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from todo import Task, TodoList

# Create a TodoList object
todo_list = TodoList()


# Functions
def add_task():
    description = add_task_entry.get()
    task = todo_list.add_task(description)
    show_tasks()
    add_task_entry.delete(0, tk.END)


def remove_task():
    selected_task = show_tasks_box.curselection()
    if selected_task:
        task_id = int(selected_task[0]) + 1 
        if todo_list.remove_task(task_id):
            show_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")
    show_tasks()



def mark_completed():
    selected_task = show_tasks_box.curselection()
    if selected_task:
        task_id = int(selected_task[0]) + 1  
        if todo_list.mark_completed(task_id):
            show_tasks() 
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")
    show_tasks()


def edit_task():
    selected_task = show_tasks_box.curselection()
    if selected_task:
        task_id = int(selected_task[0]) + 1  
        new_description = simpledialog.askstring("Edit Task", "Enter the new description:")
        if new_description:
            if todo_list.edit_task(task_id, new_description):
                show_tasks()



def search_task():
    task_id = simpledialog.askinteger("Search Task", "Enter the task ID:")
    if task_id:
        task = todo_list.search_task(task_id)
        if task:
            messagebox.showinfo("Task Details", f"Task ID: {task.unique_id}\nDescription: {task.description}\nCompleted: {task.completed}")
        else:
            messagebox.showwarning("Warning", "Task not found.")


def show_tasks():
    show_tasks_box.delete(0, tk.END)
    for task_id, task in todo_list.tasks.items():
        task_text = f"ID: {task_id} - {task.description}"
        checkbox_text = f"[{'✓' if task.completed else ' '}] "
        show_tasks_box.insert(tk.END, checkbox_text + task_text)

def get_file():
    file = todo_list.create_file()
    messagebox.showinfo("File Created", f"File {file.name} created successfully.")




#Window
window = tk.Tk()
window.title("To-Do List App")
window.minsize(width=750, height=600)
window.configure(bg="lavender")
window.config(padx=20, pady=20)

#Logo
logo_image = tk.PhotoImage(file="./todo_logo.png")
resized_image = logo_image.subsample(5)
logo_label = tk.Label(window, image=resized_image, width=80, height=80)
logo_label.grid(column=0, row=0)
logo_label.config(padx=10)

#Title
custom_color = "#C8A2C8"
title_label = tk.Label(text="Welcome to the To-Do List App", font=("Arial", 24, "bold"), fg="white", bg=custom_color)
title_label.grid(column=1, row=0, columnspan=2, pady=10, padx=80, sticky="ew")


# Add an empty label to occupy row 1
empty_label = tk.Label(window, text="", bg="lavender")
empty_label.grid(column=0, row=1)


# Add an empty label to occupy column 1
empty_label = tk.Label(window, text="", bg="lavender")
empty_label.grid(column=1, row=1)


#Menu frame
# Create a frame for the custom menu bar
menu_bar = tk.Frame(window, relief="raised", borderwidth=3)
menu_bar.grid(column=0, row=3)

# Buttons
add_task_button = tk.Button(menu_bar, text="Add task", command=add_task)
add_task_button.grid(column=0, row=4)


edit_task_button = tk.Button(menu_bar, text="Edit Task", command=edit_task)
edit_task_button.grid(column=0, row=5)


search_task_button = tk.Button(menu_bar, text="Search Task", command=search_task)
search_task_button.grid(column=0, row=6)

show_task_button = tk.Button(menu_bar, text="Show Tasks", command=show_tasks)
show_task_button.grid(column=0, row=7)

remove_task_button = tk.Button(menu_bar, text="Remove Task", command=remove_task)
remove_task_button.grid(column=0, row=8)

mark_completed_button = tk.Button(menu_bar, text="Mark Completed", command=mark_completed)
mark_completed_button.grid(column=0, row=9)

get_file_button = tk.Button(menu_bar, text="Create File", command=get_file)
get_file_button.grid(column=0, row=10)


# Add an empty label to occupy row 1
empty_label = tk.Label(window, text="", bg="lavender")
empty_label.grid(column=0, row=1)


#Type
add_task_label = tk.Label(text="Type here", font=("Arial", 24, "bold"), fg="white", bg=custom_color)
add_task_label.grid(column=1, row=2)

add_task_entry = tk.Entry()
add_task_entry.grid(column=1, row=3)

#Show tasks
show_tasks_label = tk.Label(text="List of tasks", font=("Arial", 24, "bold"), fg="white", bg=custom_color)
show_tasks_label.grid(column=2, row=4)

show_tasks_box = tk.Listbox(width=35, height=20)
show_tasks_box.grid(column=2, row=5)
show_tasks_box.config(border=2)


window.mainloop()