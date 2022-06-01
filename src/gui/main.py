import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a lebel", font=("Arial", 24, "bold"))

window.mainloop()
