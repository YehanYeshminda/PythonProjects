from tkinter import *
import time

root = Tk()
root.title("Clock!")
root.geometry("400x200")

def clock_set():
    hours = time.strftime("%I") #change to H if we need 24 hours format else I
    minute = time.strftime("%M")
    second = time.strftime("%S")

    clock_label.config(text=hours + ' : ' + minute + ' : ' + second)
    # 1000 = 1 sec
    clock_label.after(1000, clock_set)

clock_label = Label(root, text='', font=('', 48), fg='red')
clock_label.pack()

clock_set()
# to execute the clock
root.mainloop()
