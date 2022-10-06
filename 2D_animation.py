
from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity=3
yVelocity=2

window = Tk()
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
Space_image = PhotoImage(file='space.png')
background = canvas.create_image(0,0,image=Space_image,anchor=NW)
Alien_image = PhotoImage(file='astro1.png')
my_image = canvas.create_image(0,0,image=Alien_image,anchor=NW)

image_width = Alien_image.width()
image_height = Alien_image.height()

while True:
    coordinates= canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)
window.mainloop()
