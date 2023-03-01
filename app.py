from tkinter import *
root =Tk()
root.title("The Calculator")
def click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def clear():
    e.delete(0,END)

def add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0,END)


e = Entry(root ,borderwidth=5)

button_1 = Button(root , text="1" , padx=20 , pady=20 , command=lambda: click(1))
button_2 = Button(root , text="2" , padx=20 , pady=20 , command=lambda: click(2))
button_3 = Button(root , text="3" , padx=20 , pady=20 , command=lambda: click(3))
button_4 = Button(root , text="4" , padx=20 , pady=20 , command=lambda: click(4))
button_5 = Button(root , text="5" , padx=20 , pady=20 , command=lambda: click(5))
button_6 = Button(root , text="6" , padx=20 , pady=20 , command=lambda: click(6))
button_7 = Button(root , text="7" , padx=20 , pady=20 , command=lambda: click(7))
button_8 = Button(root , text="8" , padx=20 , pady=20 , command=lambda: click(8))
button_9 = Button(root , text="9" , padx=20 , pady=20 , command=lambda: click(9))
button_0 = Button(root , text="0" , padx=20 , pady=20 , command=lambda: click(0))
button_equal = Button(root , text="=" , padx=20 , pady=84 , command=lambda: click())
button_add = Button(root , text="+" , padx=20 , pady=20 , command=add)
button_clear = Button(root , text="C" , padx=20 , pady=20 , command=clear)
button_minus = Button(root , text="-" , padx=20 , pady=20 , command=lambda: click())



e.grid(row=0 , column=0 ,columnspan=4 )
button_1.grid(row=3 , column=0 )
button_2.grid(row=3 , column=1 )
button_3.grid(row=3 , column=2 )
button_4.grid(row=2 , column=0 )
button_5.grid(row=2 , column=1 )
button_6.grid(row=2 , column=2 )
button_7.grid(row=1 , column=0 )
button_8.grid(row=1 , column=1 )
button_9.grid(row=1 , column=2 )
button_0.grid(row=4 , column=0 )
button_equal.grid(row=1 , column=3 ,rowspan=3 )
button_add.grid(row=4 , column=2 )
button_clear.grid(row=4 , column=3 )
button_minus.grid(row=4 , column=1 )




root.mainloop()