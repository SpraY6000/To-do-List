from tkinter import *
from tkinter import filedialog

root = Tk()

root.title("To-Do list")

my_frame = Frame(root)
my_frame.pack(pady=20)

my_list = Listbox(my_frame, font=("Arial", 27), activestyle=NONE, selectbackground="#a6a6a6")
my_list.pack(side=LEFT, fill=BOTH)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

my_label = Label(text="Enter any task!", font=("Arial", 25))
my_label.pack(pady=15)

my_entry = Entry(root, font=("Arial", 25))
my_entry.pack(pady=5)

button_frame = Frame(root)
button_frame.pack(pady=20)

#FUNCTIONMS
def add_item():
    entryText = my_entry.get()
    if entryText == "":
        pass
    else:
        my_list.insert(END, entryText)
        my_entry.delete(0, END)

def remove_item():
    my_list.delete(ANCHOR)

def delete_all_items():
    my_list.delete(0, END)
    my_entry.delete(0, END)

def crossed_item():
    my_list.itemconfig(my_list.curselection(), fg="#a6a6a6")
    my_list.selection_clear(0, END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="black"
    )
    my_list.selection_clear(0, END)

def delete_crossed_items():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "a6a6a6":
            my_list.delete(my_list.index(count))

    count += 1
    
def save_file():
    saveFile = filedialog.asksaveasfile(defaultextension=".txt", 
                                        filetypes=[
                                            ("Text file", ".txt"),
                                            ("All files", ".*")
                                        ])
    saveText = my_list.get(0, END)
    for lines in saveText:
        saveFile.write(lines + "\n")
    saveFile.close()

    if saveFile is None:
        return

def open_file():
    my_list.delete(0, END)
    openFile = filedialog.askopenfile()
    for lines in openFile:
        my_list.insert(END, lines)
    openFile.close()

addButton = Button(button_frame, text="Add item", font=("Arial", 13), height=2, width=12, command=add_item)
removeButton = Button(button_frame, text="Remove item", font=("Arial", 13), height=2, width=12, command=remove_item)
removeAllButton = Button(button_frame, text="Remove all", font=("Arial", 13), height=2, width=12, command=delete_all_items)
crossButton = Button(button_frame, text="Cross item", font=("Arial", 13), height=2, width=12, command=crossed_item)
uncrossButton = Button(button_frame, text="Uncross item", font=("Arial", 13), height=2, width=12, command=uncross_item)
deleteCrossedButton = Button(button_frame, text="Delete crossed", font=("Arial", 13), height=2, width=12, command=delete_crossed_items)


addButton.grid(row=0, column=0)
removeButton.grid(row=0, column=1)
removeAllButton.grid(row=0, column=2)
crossButton.grid(row=1, column=0)
uncrossButton.grid(row=1, column=1)
deleteCrossedButton.grid(row=1, column=2)

menubar = Menu(root)
root.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0)
generalMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="General", menu=generalMenu)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Open", command=open_file)
generalMenu.add_command(label="Exit", command=exit)

root.mainloop()