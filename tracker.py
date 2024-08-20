import tkinter as tk

def load_habits():
    try:
        with open("entries.txt", 'r') as file:
            return file.readlines()
        
    except FileNotFoundError:
        return[]

#make the window
root = tk.Tk()
#make the grid
for i in range(31):
    tk.Label(root, text=str(i + 1)).grid(row=0, column=i + 1)
#user input for habits
def enter_habits(root):
    entries = []
    saved_entries = load_habits()
    
    for j in range(3):  # For 3 habits
        for k in range(31):
            tk.Checkbutton(root).grid(row=j + 1, column=k + 1)
        entry = tk.Entry(root)
        entry.grid(row=j + 1, column=0)
        #load the saved data if available
        if j < len(saved_entries):
            entry.insert(0, saved_entries[j].strip())
        entry.bind("<FocusOut>", lambda event, e= entry: save_entry(e))
        entries.append(entry)
    return entries
#saving the user input
def save_entry(entry, filename= "entries.txt"):
    with open(filename, 'w') as file:
        for entry in entries:
            file.write(entry.get() + '\n')

#initialize entry loop
entries = enter_habits(root)        

root.mainloop()
