from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500 , height=500)

# Entry
enter_distance = Entry(width=10)
print(enter_distance.get())
enter_distance.grid(column=2 , row=0)

my_label = Label(text="Miles")
my_label.grid(column=3 , row=0)
# my_label.config(padx=50, pady=50)

my_label_2 = Label(text="is equal to")
my_label_2.grid(column=1 , row=1)

my_label_3 = Label(text="0")
my_label_3.grid(column=2 , row=1)



def button_clicked():
    print("I got clicked")
    display_distance = round(int(enter_distance.get()) * 1.609344)
    my_label_3.config(text=display_distance)

my_label_4 = Label(text="Km")
my_label_4.grid(column=3, row=1)

button_click = Button(text="Calculate" , command=button_clicked)
button_click.grid(column=2 , row=3)

window.mainloop()
