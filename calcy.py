# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:40:27 2020

@author: Vinay
"""


#creating a calcy

from tkinter import *
import parser

root = Tk()
root.title("manoj_calcy")

#adding entry
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

#getting input from user

i = 0
def get_variable(num):
    global i
    display.insert(i, num)
    i+=1
 
def clear():
    display.delete(0, END)
    
def undo():
    string1 = display.get()
    if len(string1):
        new = string1[:-1]
        clear()
        display.insert(0, new)
    else:
        clear()
        display.insert(0, "Error")

def operator(op):
    global i
    length = len(op)
    display.insert(i, op)
    i+=length


def calculation():
    s1 = display.get()
    try:
        a = parser.expr(s1).compile()
        result = eval(a)
        clear()
        display.insert(i, result)
    except EXCEPTION:
        clear()
        display.insert(i, "error")

def fact(x):
    if x==1:
        print(x)
    else:
        print(x*(fact(x-1)))
                


#adding buttons

Button(root, text="1", command=lambda: get_variable(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_variable(2)).grid( row=2, column=1)
Button(root, text="3", command=lambda: get_variable(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: get_variable(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_variable(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_variable(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: get_variable(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_variable(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_variable(9)).grid(row=4, column=2)

#adding other buttons to calcy

Button(root, text="AC", command=lambda: clear()).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_variable(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculation()).grid(row=5, column=2)

Button(root, text="/", command=lambda: operator("/")).grid(row=2, column=4)
Button(root, text="*", command=lambda: operator("*")).grid(row=3, column=4)
Button(root, text="+", command=lambda: operator("+")).grid(row=4, column=4)
Button(root, text="-", command=lambda: operator("-")).grid(row=5, column=4)

Button(root, text="pi", command=lambda: operator("*3.14")).grid(row=2, column=5)
Button(root, text="exp", command=lambda: operator("**")).grid(row=3, column=5)
Button(root, text="<", command=lambda: operator("<")).grid(row=4, column=5)
Button(root, text="(", command=lambda: operator("()")).grid(row=5, column=5)

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=6)
Button(root, text="x!", command=lambda: fact(x)).grid(row=3, column=6)
Button(root, text="^2", command=lambda: operator("**2")).grid(row=4, column=6)
Button(root, text=")", command=lambda: operator()).grid(row=5, column=6)






root.mainloop()
