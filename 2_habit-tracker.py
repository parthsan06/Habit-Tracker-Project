import tkinter as tk
import json
from datetime import datetime

def get_current_month():
    month = datetime.now().strftime('%B').upper()
    year = datetime.now().strftime('%Y')
    return f'{month} {year}'

def load_habits():
    try:
        with open("entries.json", 'r') as file:
            content = file.read().strip() # read the file and remove any whitespace
            if not content:
                return {"months": {}}
            return json.loads(content)
    except FileNotFoundError:
        return {"months": {}}

# Saving the user input
def save_entry(entries, checkboxes, filename="entries.json"):
    saved_entries = load_habits
    current_month = get_current_month()

    if "months" not in saved_entries():
        saved_entries["months"] = {} 

    data = {"months" : {current_month : {}}}

    for i, entry in enumerate(entries):
        checkbox_vars = checkboxes[i]
        habit_name = entry.get()
        checkbox_states = [var.get() for var in checkbox_vars]
        data["months"][current_month][f'habit_{i}'] = {
            "entry" : habit_name,
            "checkboxes" : checkbox_states
            }
        
    with open(filename, 'w') as file:
        json.dump(data, file, indent= 4)

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

    current_month = get_current_month()

    month_data = saved_entries['months'].get(current_month, {})
    
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
        habit_key = f'habit_{j}'
        if habit_key in month_data:
            habit_data = month_data[habit_key]
            entry.insert(0, habit_data["entry"])
            checkbox_states = habit_data["checkboxes"]
            for k, state in enumerate(checkbox_states):
                if k < len(checkbox_vars):
                    checkbox_vars[k].set(int(state))

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
