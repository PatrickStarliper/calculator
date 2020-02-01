from tkinter import *

window = Tk()
window.title("Calculator")
window.resizable(False,False)
#window.geometry('300x400')
#text = entry1.get()
#label1 = Label(window,text='1',font=(16),relief='solid').place(x=50,y=100)

# entry box 
e = Entry(window,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

# operand functions

def btn_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def btn_clear():
    e.delete(0, END)

def btn_add():
    num1 = e.get()
    global fnum
    global math
    math = "add"
    fnum = int(num1)
    e.delete(0, END)

def btn_sub():
    num1 = e.get()
    global fnum
    global math
    math = "sub"
    fnum = int(num1)
    e.delete(0, END)

def btn_mul():
    num1 = e.get()
    global fnum
    global math
    math = "mul"
    fnum = int(num1)
    e.delete(0, END)

def btn_div():
    num1 = e.get()
    global fnum
    global math
    math = "div"
    fnum = int(num1)
    e.delete(0, END)

def btn_equal():
    num2 = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, fnum + int(num2))
    elif math == "sub":
        e.insert(0, fnum - int(num2))
    elif math == "mul":
        e.insert(0, fnum * int(num2))
    elif math == "div":
        e.insert(0, fnum / int(num2))

# Define and create buttons

button9 = Button(window,text='9',padx=20,pady=10,font=40,command=lambda: btn_click(9)).grid(row=1,column=2)
button8 = Button(window,text='8',padx=20,pady=10,font=40,command=lambda: btn_click(8)).grid(row=1,column=1)
button7 = Button(window,text='7',padx=20,pady=10,font=40,command=lambda: btn_click(7)).grid(row=1,column=0)
button6 = Button(window,text='6',padx=20,pady=10,font=40,command=lambda: btn_click(6)).grid(row=2,column=2)
button5 = Button(window,text='5',padx=20,pady=10,font=40,command=lambda: btn_click(5)).grid(row=2,column=1)
button4 = Button(window,text='4',padx=20,pady=10,font=40,command=lambda: btn_click(4)).grid(row=2,column=0)
button3 = Button(window,text='3',padx=20,pady=10,font=40,command=lambda: btn_click(3)).grid(row=3,column=2)
button2 = Button(window,text='2',padx=20,pady=10,font=40,command=lambda: btn_click(2)).grid(row=3,column=1)
button1 = Button(window,text='1',padx=20,pady=10,font=40,command=lambda: btn_click(1)).grid(row=3,column=0)
button0 = Button(window,text='0',padx=20,pady=10,font=40,command=lambda: btn_click(0)).grid(row=4,column=1)
button_clear = Button(window,text='C',padx=20,pady=10,font=40,command=btn_clear).grid(row=4,column=0)
button_enter = Button(window,text='=',padx=19,pady=10,font=40,command=btn_equal).grid(row=4,column=2)
button_add = Button(window,text='+',padx=19,pady=10,font=40,command=btn_add).grid(row=4,column=3)
button_minus = Button(window,text='-',padx=19,pady=10,font=40,command=btn_sub).grid(row=3,column=3)
button_multiply = Button(window,text='x',padx=19,pady=10,font=40,command=btn_mul).grid(row=2,column=3)
button_divide = Button(window,text='/',padx=19,pady=10,font=40,command=btn_div).grid(row=1,column=3)

window.mainloop()
