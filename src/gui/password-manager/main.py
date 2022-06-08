# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(400, 400)

canvas = Canvas(height=200, width=300)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=pass_img)
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
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, columnspan=1)

password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=48)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()