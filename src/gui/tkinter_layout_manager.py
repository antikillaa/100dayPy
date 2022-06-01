import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a lebel", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button1 = tkinter.Button(text="Click Me", command=button_clicked)
button1.grid(column=2, row=2)
button2 = tkinter.Button(text="New button")
button2.grid(column=3, row=0)


#Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

canvas = tkinter.Text()

window.mainloop()
