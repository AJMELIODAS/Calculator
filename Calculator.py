from tkinter import *

#Gui creation
root=Tk()
root.title('Calculator')
root.geometry('700x470')
root.config(bg='white')
root.resizable(0,0)
root.iconbitmap('C:/Users/new/Downloads/Blackvariant-Shadow135-System-Calculator.ico')

#Frame
expression=''
new_frame=Frame(root)
new_frame.pack(pady=10,padx=10)
new_frame.config(bg='#9933ff')

#Number intake
def num(number):
    global expression
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))
    expression=e.get()
    
#Clears everything
def clscreen():
    e.delete(0,END)

#Deletes last number
def bspace():
    if str(e.get())=='ERROR':
        e.delete(0,END)
    temp=list(str(e.get()))
    e.delete(0,END)
    p=''
    if len(temp)>0:
        temp.pop()
    for i in range(len(temp)):
        p+=temp[i]
    e.insert(0,p)

#Checks for exceptions
def check():
    try:
        temp=float(e.get())
    except ValueError:
        e.delete(0,END)
        e.insert(0,'ERROR')


#Dot for decimal values
def dt():
    check()
    cnum=str(e.get())
    if '.' not in cnum:
        e.delete(0,END)
        e.insert(0,cnum+'.')

#Equals to button to show the answer after calculating the query
def equals():
    try:
        answer=str(eval(expression))
        e.delete(0,END)
        e.insert(0,answer)
    except (ValueError,SyntaxError,ZeroDivisionError):
        e.delete(0,END)
        e.insert(0,'ERROR')

#Colours
numbers_colour='white'
button_colour='#ac3973'



# Entry Frame
E_frame=Frame(new_frame,bg='black',width=100,height=100)
E_frame.pack(pady=(10,0),padx=10) #pady=(above,below)

# Buttons Frame
B_frame=Frame(new_frame)
B_frame.pack(padx=10,pady=10)
B_frame.config(bg=button_colour)

#Entry box
e=Entry(E_frame,width=60,font=('sans-serif',20))
e.grid(row=0,column=0)

#buttons
b1=Button(B_frame,text=1,font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=40,pady=20,command=lambda: num(1))
b2=Button(B_frame,text=2,font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=40,pady=20,command=lambda: num(2))
b3=Button(B_frame,text=3,font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=40,pady=20,command=lambda: num(3))
b4=Button(B_frame,text=4,font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=40,pady=20,command=lambda: num(4))
b5=Button(B_frame,text=5,font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=40,pady=20,command=lambda: num(5))
b6=Button(B_frame,text=6,font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=40,pady=20,command=lambda: num(6))
b7=Button(B_frame,text=7,font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=40,pady=20,command=lambda: num(7))
b8=Button(B_frame,text=8,font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=40,pady=20,command=lambda: num(8))
b9=Button(B_frame,text=9,font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=40,pady=20,command=lambda: num(9))
b0=Button(B_frame,text=0,font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=40,pady=20,command=lambda: num(0))

#Operation buttons
multi=Button(B_frame,text='X',font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=46.5,pady=20,command=lambda: num('*'))
div=Button(B_frame,text='/',font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=44,pady=20,command=lambda: num('/'))
minus=Button(B_frame,text='-',font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=44.5,pady=20,command=lambda: num('-'))
plus=Button(B_frame,text='+',font=('sans-serif',21),bg=button_colour,fg=numbers_colour,bd=0,padx=47.8,pady=20,command=lambda: num('+'))
dot=Button(B_frame,text='.',font=('sans-serif',22),bg=button_colour,fg=numbers_colour,bd=0,padx=43,pady=20,command=dt)
exp=Button(B_frame,text='m^n',font=('sans-serif',19),bg=button_colour,fg=numbers_colour,bd=0,padx=42,pady=24,command=lambda: num('**'))
equal=Button(B_frame,text='=',font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=42.35,pady=20,command=equals)
clear=Button(B_frame,text='CLEAR',font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=9,pady=19,command=clscreen)
backspace=Button(B_frame,text='←',font=('sans-serif',25),bg=button_colour,fg=numbers_colour,bd=0,padx=30,pady=13,command=bspace)
sqt=Button(B_frame,text='n^1/2',font=('sans-serif',20),bg=button_colour,fg=numbers_colour,bd=0,padx=44.6,pady=15,command=lambda: num('**(1/2)'))

# Positioning the buttons

#Buttons- 7,8,9 and clear and backspace
b7.grid(row=0,column=0)
b8.grid(row=0,column=1)
b9.grid(row=0,column=2)
clear.grid(row=0,column=3)
backspace.grid(row=0,column=4)

#Buttons- 4,5,6 and multiplication and division
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
multi.grid(row=1,column=3)
div.grid(row=1,column=4)

#Buttons- 1,2,3 and addition and subtraction
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
plus.grid(row=2,column=3)
minus.grid(row=2,column=4)

#Buttons- 0,decimal point,exponent and square root and equals to
b0.grid(row=3,column=0)
dot.grid(row=3,column=1)
exp.grid(row=3,column=2)
sqt.grid(row=3,column=3)
equal.grid(row=3,column=4)

root.mainloop()