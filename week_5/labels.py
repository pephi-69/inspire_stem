from tkinter import *

window = Tk()

window.configure(bg='lightblue')

# Adjust size
window.geometry("400x400")


window.title("Sensors Tutorial")

temp = 20
hum = 68

lbl = Label(window, text="Temperature : {0}".format(temp))

lbl.grid(column=400, row=100)

lb2 = Label(window, text="Humidity: {0}".format(hum))

lb2.grid(column=500, row=200)

window.mainloop()