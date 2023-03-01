from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)
window.config(padx=40, pady=75)


def convert():
    miles = float(input.get())
    km = round(miles * 1.60934, 2)
    output["text"] = km


main_text = Label(text="is equal to: ")
main_text.grid(row=2, column=0)

input = Entry(width=10)
input.grid(row=1, column=2)

output = Label(text=0)
output.grid(row=2, column=2)

calculate = Button(text="calculate", command=convert)
calculate.grid(row=3, column=2)

miles_label = Label(text="miles")
miles_label.grid(row=1, column=3)


km_label = Label(text="Km")
km_label.grid(row=2, column=3)

window.mainloop()
