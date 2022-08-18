from tkinter import *
import time
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=150,height=150)
FONT = ("Arial", 14)
#Label

miles_label = Label(text = "Miles", font = FONT)
miles_label.grid(column = 2, row = 0)

equal_label = Label(text = "is equal to", font = FONT)
equal_label.grid(column = 0, row = 1)

km_num_label = Label(text = "0", font = FONT)
km_num_label.grid(column = 1, row = 1)

km_label = Label(text = "Km", font = FONT)
km_label.grid(column = 2, row = 1)

input_miles = Entry()
input_miles.grid(column = 1, row = 0)

def button_clicked():
    km_num_label.config(text = int(input_miles.get())*1.609)

button = Button(text="Calculate", font = FONT, command = button_clicked)
button.grid(column = 1, row = 2)

window.mainloop()