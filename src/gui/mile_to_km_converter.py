from tkinter import *

window = Tk()
window.title("Mile to Kilometers Converter")
window.minsize(width=200, height=100)
window.config(pady=10, padx=10)

km_input = Entry()
km_input.insert(END, string="Enter Kilometers value")
km_input.grid(column=0, row=0)

miles = Label()
miles.grid(column=3, row=3)


def get_calculate():
    result = float(km_input.get()) * 0.6
    miles.config(text=round(result, 2))


calculate = Button(text="Calculate", command=get_calculate)
calculate.grid(column=3, row=0)

window.mainloop()
