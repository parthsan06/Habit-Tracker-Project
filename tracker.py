import tkinter as tk

def load_habits():
    try:
        with open("entries.txt", 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

# Saving the user input
def save_entry(entries, checkboxes, filename="entries.txt"):
    with open(filename, 'w') as file:
        for entry, checkbox_vars in zip(entries, checkboxes):
            file.write(entry.get() + ';' + ','.join(str(var.get()) for var in checkbox_vars) + '\n')

# Make the window
root = tk.Tk()
# Make the grid
for i in range(31):
    tk.Label(root, text=str(i + 1)).grid(row=0, column=i + 1)

# User input for habits
def enter_habits(root):
    entries = []
    checkboxes = []  # State of all the checkboxes
    saved_entries = load_habits()
    
    for j in range(3):  # For 3 habits
        checkbox_vars = []  # State of the checkboxes of each habit separately
        checkbox_states = ['0'] * 31  # Initial unchecked state
        for k in range(31):
            var = tk.IntVar(value=int(checkbox_states[k]))  # Set initial state of checkboxes from cb_states
            cb = tk.Checkbutton(root, variable=var)  # Create Checkbutton with variable
            cb.grid(row=j + 1, column=k + 1)
            checkbox_vars.append(var)
        
        entry = tk.Entry(root)
        entry.grid(row=j + 1, column=0)
        
        # Load the saved data if available
        if j < len(saved_entries):
            line = saved_entries[j].strip()
            print(f"Loaded line: '{line}'")  # Debugging: print the loaded line
            if ';' in line:
                entry_data, checkbox_data = line.split(';', 1)
                entry.insert(0, entry_data)
                checkbox_states = checkbox_data.split(',')
                for k, state in enumerate(checkbox_states):
                    if k < len(checkbox_vars):
                        checkbox_vars[k].set(int(state))
            else:
                print(f"Warning: Delimiter missing in entry at line {j}. Defaulting to empty.")
        else:
            print(f"Warning: No saved data for habit {j}. Defaulting to empty.")
        
        # Append the entry and checkbox_vars to their lists
        entries.append(entry)
        checkboxes.append(checkbox_vars)

    # Store references to entries and checkboxes in root
    root.entries = entries
    root.checkboxes = checkboxes

    # Bind the focus out event to save on focus out
    for entry in entries:
        entry.bind("<FocusOut>", lambda event, e=entry: save_entry(root.entries, root.checkboxes))

    # Bind the window close event to save and exit
    def on_closing():
        print("Window close event triggered.")  # Debugging: Check if function is called
        save_entry(root.entries, root.checkboxes)
        root.destroy()  # Properly close the window

    root.protocol("WM_DELETE_WINDOW", on_closing)
    return entries

# Initialize entry loop
entries = enter_habits(root)        

root.mainloop()
