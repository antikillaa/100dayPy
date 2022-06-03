from tkinter import *

window = Tk()
window.title("Mile to Kilometers Converter")
window.minsize(width=100, height=50)
window.config(pady=20, padx=20)

km_input = Entry()
km_input.config(width=8)
km_input.insert(END, string="0")
km_input.grid(column=1, row=0)

miles = Label(text='0')
miles.grid(column=1, row=1)

is_eq_label = Label(text="is equal to")
is_eq_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def get_calculate():
    result = float(km_input.get()) * 1.609
    miles.config(text=round(result, 2))


calculate = Button(text="Calculate", command=get_calculate)
calculate.grid(column=1, row=2)

window.mainloop()
