import random
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip as pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(0, 10)]
    password_symbols = [random.choice(symbols) for _ in range(2, 4)]
    password_numbers = [random.choice(numbers) for _ in range(2, 4)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox


def add_data():
    website = website_entry.get()
    user = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Do you want to save password:\n "
                                               f"Website: {website}\n"
                                               f"Username: {user}\n"
                                               f"Password: {password}")

        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {user} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            messagebox.showinfo(message='Password is saved')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(400, 400)

canvas = Canvas(height=200, width=300)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(165, 100, image=pass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username")
username_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=50)
username_entry.insert(END, "antikillaaaa@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, columnspan=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=48, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
