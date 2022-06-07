from tkinter import *
import csv
from csv import DictWriter


class todoApp():

    def __init__(self):
        pass

    def gui_interface(self):
        root = Tk()
        root.geometry('200x200')

        label_task_number = Label(root, text="Task-No", font=12)
        label_task = Label(root, text="Task", font=12)

        label_task_number.grid(row=1, column=1, sticky=W)
        label_task.grid(row=2, column=1)

        label_task_number_entry = Entry(root)
        label_task_entry = Entry(root)

        label_task_number_entry.grid(row=1, column=2)
        label_task_entry.grid(row=2, column=2)

        fieldnames = ['Task number', 'Task']

        def pass_input():
            return {'Task number': label_task_number_entry.get(), 'Task': label_task_entry.get()}

        def insert_data(data):
            user_input_get = data
            print(user_input_get)
            with open('data.csv', 'a', newline='') as f_object:
                dictwriter_object = DictWriter(f_object, fieldnames=fieldnames)  # Pass the CSV  file object to the Dictwriter() function
                # Pass the data in the dictionary as an argument into the writerow() function
                dictwriter_object.writerow(user_input_get)
                f_object.close()

        Button(root, text="enter data", command=lambda: insert_data(pass_input())).grid(row=4, columnspan=2)
        root.mainloop()


todoApp = todoApp()

todoApp.gui_interface()

# todoApp.insertData()
