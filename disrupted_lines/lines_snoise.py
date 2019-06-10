from tkinter import *
import random
import time
from noise import pnoise2, snoise2

tk = Tk()
canvas = Canvas(tk, width=800, height=800, bg='black')
canvas.pack()

x = 10
y = 10
num = 20

coordinates = [(x, y)]


def first_line(coordinates, colour):
    xi, yi = coordinates[0][0], coordinates[0][1]
    while xi < 790:
        xf = xi + 20
        yf = yi * (1 + snoise2(yi, xi, 6)/num)
        canvas.create_line(xi, yi, xf, yf, fill=colour)
        tk.update_idletasks()
        tk.update()
        # time.sleep(0.001)
        coordinates.append((xf, yf))
        xi = xf
        yi = yf
    return coordinates


def repeat_lines(coordinates, colour):

    octave = 4
    line_width = 1 #random.randint(1, 5)

    first_line(coordinates, colour)
    num = 50


    while coordinates[-1][1] < 790:
        new_coordinates = [(coordinates[0][0], 20 + coordinates[0][1]*( 1 + snoise2(coordinates[0][1], coordinates[0][0], octave)/num))]
        for point in coordinates:
            xi = point[0]
            yi = point[1]
            xf = xi + 20
            yf = yi * (1 + snoise2(yi, xi, octave)/num)
            canvas.create_line(xi, yi, xf, yf, fill=colour, width=line_width)
            tk.update_idletasks()
            tk.update()
            # time.sleep(0.001)
            new_coordinates.append((xf, yf))

        # import ipdb; ipdb.set_trace()
        coordinates = new_coordinates


repeat_lines(coordinates, 'white')
coordinates = [(x, y)]
repeat_lines(coordinates, 'grey')

canvas.mainloop()
