from tkinter import *
import random
import time
from noise import pnoise2, snoise2

tk = Tk()
canvas = Canvas(tk, width=3000, height=3000, bg='black')
canvas.pack()

x = 10
y = 10

coordinates = [(x, y)]


def first_line(coordinates, colour):
    xi, yi = coordinates[0][0], coordinates[0][1]
    while xi < 2990:
        xf = xi + 20
        yf = yi + snoise2(xi, yi, 6)
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
    first_line(coordinates, colour)
    while coordinates[-1][1] < 1500:
        # seed_value += float(0.1)
        line_width = random.randint(1, 5)
        new_coordinates = [(coordinates[0][0], coordinates[0][1] + 10 + snoise2(coordinates[0][0],
                                                                                coordinates[0][1], octave))]
        for point in coordinates:
            xi = point[0]
            yi = new_coordinates[-1][1]
            xf = xi + 20
            yf = yi + snoise2(xi, yi, octave)
            canvas.create_line(xi, yi, xf, yf, fill=colour, width=line_width)
            tk.update_idletasks()
            tk.update()
            # time.sleep(0.001)
            new_coordinates.append((xf, yf))
        coordinates = new_coordinates


repeat_lines(coordinates, 'white')
coordinates = [(x, y)]
repeat_lines(coordinates, 'grey')

canvas.mainloop()
