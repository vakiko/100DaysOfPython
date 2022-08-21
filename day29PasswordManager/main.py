from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    print("Password generated")
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = ''.join(password_list)

    print(f"Your password is: {password}")
    pass_entry.delete(0,END)
    pass_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    
    print("Password added")
    f = open("user_pass.txt", "a")
    username = user_entry.get()
    password = pass_entry.get()
    website = website_entry.get()
    
    if password.strip() == "" or username.strip() == "" or website.strip() == "":
        messagebox.showinfo(title = "Error", message = "You have entered an empty field. Please try again!")
    else:      
        is_ok = messagebox.askokcancel(title = website, message=f"You entered that your username/email is {username} and that your password is {password}. Is this correct?")
        
        if is_ok:
            f.write(f"{website} | {username} | {password}\n")
            f.close()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass Manager")
window.config(padx = 50, pady = 50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column = 1, row = 0)

website_label = Label(text="Website")
website_label.grid(column = 0, row = 1)
user_label = Label(text="Email/Username:")
user_label.grid(column = 0, row = 2)
pass_label = Label(text="Password:")
pass_label.grid(column = 0, row = 3)

website_entry = Entry(width=50)
website_entry.grid(column = 1,row = 1,columnspan=2)
user_entry = Entry(width=50)
user_entry.grid(column = 1,row = 2,columnspan=2)
user_entry.insert(0,"user@email.com")
pass_entry = Entry(width=32)
pass_entry.grid(column = 1,row = 3)

start_button = Button(text="Generate Password", command=gen_pass)
start_button.grid(column=2, row=3)

reset_button = Button(text="Add", command=add_pass, width = 43)
reset_button.grid(column=1, row=4, columnspan=2)


window.mainloop()