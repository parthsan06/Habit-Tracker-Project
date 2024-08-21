# Functions

## load_habits:
This opens up the entries.txt file in read mode, in which the data of each habit and its corresponding checkbox states(checked or unchecked) is stored, and reads them as seperate strings so that they can be filled in their corresponding spaces.

## save_entry:
This function opens the entries.txt file in write mode, then pairs up each each entry widget(habit) with its corresponding checkbox states contained in the lists entries and checkboxes respectively.

## enter_habits:
Creates two empty lists for all habits and checkboxes resp. And using a for loop for rows, creates another empty list for checkbox states of each habit seperately and sets them to unchecked initially.
Then using a nested for loop for all the checkboxes, it creates checkbutton with variable, sets thier initial state from cb_states, places them in the grid and appends any new changes to the checkbox_vars list. It also creates entry widgets for the habits in the first column.
Then it checks if there are any saved entries to load by comparing j(row no.) with the length of the saved_entries, which is a function call to the load_habits, as function type cannot be directly used in len() as arguments. For example, for our first habit in the first row, j = 0, and if there is any saved entry to load, the length of the list will be greater than 0, and hence the conditional code will run, which is: it strips any extra characters from the row data, splits it into entry and checkbox data using ';' as formatted in the save_entry function, spilts the checkbox data using ',', inserts the entry data. In the for k loop, 'k' is the index for the checkbox and state is the value for it(either 0 or 1). And then there are else statements for when there are no habits or checkboxe states to load.
Finally it appends all the habit entries and their checkbox states to the entries and checkboxes lists. Then it stores references to entries and checkboxes in root, binds the focus out event to save entries when user stops typing, binds the window close event to save on closing and exit using **on_closing** function.

# Other things:
And at last the enter_habits function is called for it to, well, 'function', and the mainloop is run for the program to keep running and updating.

Also I used another for loop to make the the row of dates, using the Label function of tkinter.