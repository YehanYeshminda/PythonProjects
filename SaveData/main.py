import csv
from csv import DictWriter
from tkinter import *

# csv header
fieldnames = ['name', 'date of birth', 'number', 'email']

# csv test data
# rows = [
#     {'name': 'Albania',
#     'area': 28748,
#     'country_code2': 'AL',
#     'country_code3': 'ALB'},
#     {'name': 'Albania',
#     'area': 28748,
#     'country_code2': 'AL',
#     'country_code3': 'ALB'}
# ]
#
# rows_update = {'name':'04','area':'John','country_code2':'Mathematics', 'country_code3':'Mathematics'}

def user_input():
    d = {}
    for i in range(4):
        keys = fieldnames[i]  # setting the field names as a key inside the loop
        print(f"Enter {fieldnames[i]}")
        values = input()  # getting the input from the user in order for the field names
        d[keys] = values # setting to the dictionary
    return [d]

def user_input_update():
    d = {}
    for i in range(4):
        keys = fieldnames[i]  # setting the field names as a key inside the loop
        print(f"Enter {fieldnames[i]}")
        values = input()  # getting the input from the user in order for the field names
        d[keys] = values # setting to the dictionary
    return d

def write_csv():
    user_input_get = user_input()
    with open('data.csv', 'w', encoding='UTF8', newline='') as f_object:
        writer = csv.DictWriter(f_object, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(user_input_get)
        f_object.close()

def append_data():
    user_input_get = user_input_update()
    with open('data.csv', 'a', newline='') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=fieldnames) # Pass the CSV  file object to the Dictwriter() function
        # Pass the data in the dictionary as an argument into the writerow() function
        dictwriter_object.writerow(user_input_get)
        # Close the file object
        f_object.close()

def interface():
    # creates the main window
    main_window = Tk()

    # Labels
    Label(main_window, text="CSV EDITOR").grid(row=0, column=1)
    Label(main_window, text="Name").grid(row=1, column=0,)
    Label(main_window, text="date of birth").grid(row=2, column=0)
    Label(main_window, text="Number").grid(row=3, column=0,)
    Label(main_window, text="Email").grid(row=4, column=0,)

    # entry
    Entry(main_window, width=50, borderwidth=5).grid(row=1, column=1)
    Entry(main_window, width=50, borderwidth=5).grid(row=2, column=1)
    Entry(main_window, width=50, borderwidth=5).grid(row=3, column=1)
    Entry(main_window, width=50, borderwidth=5).grid(row=4, column=1)
    main_window.mainloop()

    # BUILD THE USER INTERFACE AND MAKE THE WHOLE THING INTERACTIVE


interface()
