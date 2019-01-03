from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, with=400, height=400)
canvas.pack()

x = 10
y = 10
chaos = 2

def first_line(x,y):
    while y < 390:
        canvas.create_line(x, y, x+2, y+random.randrange(-2,chaos))
