import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("To do list")

def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END, todo)
        task_add.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention", message="To add a task, please enter some task")

def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
    except IndexError:
        tkinter.messagebox.showwarning(title="Attention", message="To delete a task, you must select a task")

def task_save():
    todo_list = todo_box.get(0, todo_box.size())
    with open("tasks.dat", "wb") as file:
        pickle.dump(todo_list, file, protocol=pickle.HIGHEST_PROTOCOL)

todo_box = tkinter.Listbox(window, height=5, width=50)
todo_box.pack()

scroller = tkinter.Scrollbar(window)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)
todo_box.config(yscrollcommand=scroller.set)

task_add = tkinter.Entry(window, width=70)
task_add.pack()

add_task_button = tkinter.Button(window, text="Click to add task", font=("arial", 20, "bold"), background="red", width="40", command=task_adding)
add_task_button.pack()

remove_task_button = tkinter.Button(window, text="Click to delete task", font=("arial", 20, "bold"), background="yellow", width="40", command=task_removing)
remove_task_button.pack()

save_task_button = tkinter.Button(window, text="Click to save task", font=("arial", 20, "bold"), background="green", width="40", command=task_save)
save_task_button.pack()

window.mainloop()