import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk 

selected_index = None
dark_mode = False

def add_task():
    global selected_index
    task = task_input.get()
    if task != "":
        if selected_index is not None:
            task_listbox.insert(selected_index, task)
            selected_index = None
        else:
            task_listbox.insert(tk.END, task)
        task_input.delete(0, tk.END)
        save_tasks()

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task[0])
        task_listbox.selection_clear(0, tk.END)  
        save_tasks()

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def edit_task():
    global selected_index
    selected_task = task_listbox.curselection()
    if selected_task:
        selected_index = selected_task[0]
        task_text = task_listbox.get(selected_index)
        task_input.delete(0, tk.END)
        task_input.insert(0, task_text)
        task_listbox.delete(selected_index)
        save_tasks()

def apply_dark_scrollbar_style():
    style.configure("Vertical.TScrollbar",
        gripcount=0,
        background="#888888",
        darkcolor="#5C6BC0",
        lightcolor="#5C6BC0",
        troughcolor="#2E2E2E",
        bordercolor="#2E2E2E",
        arrowcolor="white"
    )

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode 
    if dark_mode:
        root.config(bg="#2E2E2E")
        frame.config(bg="#2E2E2E")
        button_frame.config(bg="#2E2E2E")
        task_listbox.config(bg="#3E3E3E", fg="white")
        task_input.config(bg="#3E3E3E", fg="white")
        add_button.config(bg="#5C6BC0")
        delete_button.config(bg="#EF5350")
        edit_button.config(bg="#26A69A")
        dark_mode_button.config(text="Light Mode")
        title_label.config(bg="#2E2E2E", fg="white")
        header_frame.config(bg="#2E2E2E")
        task_listbox.config(bg="#3E3E3E", fg="white")
        apply_dark_scrollbar_style()

    else:
        root.config(bg="#f1f1f1")
        frame.config(bg="#f1f1f1")
        button_frame.config(bg="#f1f1f1")
        task_listbox.config(bg="#e0e0e0", fg="Black")
        task_input.config(bg="#e0e0e0", fg="Black")
        add_button.config(bg="#4CAF50")
        delete_button.config(bg="#FF5722")
        edit_button.config(bg="#2196F3")
        dark_mode_button.config(text="Dark Mode")
        title_label.config(bg="#f1f1f1", fg="#333")
        header_frame.config(bg="#f1f1f1")
        task_listbox.config(bg="#e0e0e0", fg="Black")
        style.configure("Vertical.TScrollbar",
            gripcount=0,
            background="#c1c1c1",
            darkcolor="#c1c1c1",
            lightcolor="#e0e0e0",
            troughcolor="#f1f1f1",
            bordercolor="#f1f1f1",
            arrowcolor="black"
        )

root = tk.Tk()
root.title("Planster - Your daily task buddy!")
root.geometry("450x500")
root.config(bg="#f1f1f1")

style = ttk.Style()
style.theme_use("default")
style.configure("Vertical.TScrollbar",
    gripcount=0,
    background="#c1c1c1",
    darkcolor="#c1c1c1",
    lightcolor="#e0e0e0",
    troughcolor="#f1f1f1",
    bordercolor="#f1f1f1",
    arrowcolor="black"
)

#
img = Image.open(r"E:\Summer Project\logo.png")
img = img.resize((45, 40), Image.Resampling.LANCZOS)  
logo_img = ImageTk.PhotoImage(img)

header_frame = tk.Frame(root, bg="#f1f1f1")
header_frame.pack(pady=10)

logo_label = tk.Label(header_frame, image=logo_img, bg="#f1f1f1")
logo_label.image = logo_img  
logo_label.pack(side=tk.LEFT)

title_label = tk.Label(header_frame, text="Planster", font=("Arial", 18, "bold"), bg="#f1f1f1", fg="#333")
title_label.pack(side=tk.LEFT, padx=10)
#
frame = tk.Frame(root, bg="#f1f1f1")
frame.pack(pady=20)

task_input = tk.Entry(frame, width=30, font=("Arial", 12), bg="#e0e0e0", bd=1.5, relief="sunken")
task_input.grid(row=0, column=0, padx=10, pady=10)

task_listbox = tk.Listbox(frame, width=35, height=10, selectmode=tk.SINGLE, font=("Arial", 12), bg="#e0e0e0", bd=3, relief="sunken")
task_listbox.grid(row=1, column=0, padx=(10, 0), pady=10)

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=task_listbox.yview, style="Vertical.TScrollbar")
scrollbar.grid(row=1, column=1, sticky="ns", pady=10)
task_listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root, bg="#f1f1f1")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="ADD TASK", command=add_task, width=15, font=("Arial", 12), bg="#4CAF50", fg="white", relief="ridge", bd=2)
add_button.grid(row=0, column=0, padx=10, pady=5)

delete_button = tk.Button(button_frame, text="DELETE TASK", command=delete_task, width=15, font=("Arial", 12), bg="#FF5722", fg="white", relief="ridge", bd=2)
delete_button.grid(row=0, column=1, padx=10, pady=5)

edit_button = tk.Button(button_frame, text="EDIT TASK", command=edit_task, width=15, font=("Arial", 12), bg="#2196F3", fg="white", relief="ridge", bd=2)
edit_button.grid(row=1, column=0, padx=10, pady=5)

dark_mode_button = tk.Button(button_frame, text="Dark Mode", command=toggle_dark_mode, width=15, font=("Arial", 12), bg="#561066", fg="white", relief="ridge")
dark_mode_button.grid(row=1, column=1, padx=10, pady=5)

load_tasks()

root.mainloop()