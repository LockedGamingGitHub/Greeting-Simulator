from glob import glob
from multiprocessing.connection import wait
from random import randint
from re import U
from tkinter import *

count = 0

def click():
    global count
    if count <= 100:
        count+=1
        label.config(text=count)
        luck = randint(1, 15)
        if luck == 1:
            count = 0
        badluck = randint(1, 30)
        if badluck == 1:
            exit()
    elif count >= 100:
        label.config(text="Sorry... I lost count", fg= "red")

    
    
window = Tk()
button = Button(window, text='Greet Someone Like a Gamer!')
button.config(command=click)
button.config(font=('Open Sans', 50, 'bold'))
button.config(bg='#b8860b')
button.config(fg='#000000')
button.config(activebackground='#daa520')
button.config(activeforeground='#000000')
label = Label(window, text="Start greeting people!", fg= "blue")
label.config(font=('Monospace', 40, 'bold'))
label.pack()
button.pack()
window.title('Greeting Simulator ULTRA IMPOSSIBLE')
window.state("zoomed")
window.mainloop()




