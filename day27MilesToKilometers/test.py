from tkinter import *
import time
window = Tk()
window.title("First GUI Program")
window.minsize(width=500,height=300)

#Label
my_label = Label(text = "I am a Label!")
my_label.pack()

def button_clicked():
    print("I got clicked!")
    my_label.config(text = "I got clicked!")
    time.sleep(0.1)
    my_label.config(text = input.get())

button = Button(text="Click me", command = button_clicked)
button.pack()

#entry

input = Entry()
input.pack()
print(input.get())
window.mainloop()