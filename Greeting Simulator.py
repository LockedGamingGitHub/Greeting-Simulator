from tkinter import *

count = 0
def click():
    global count
    count+=1
    label.config(text=count)
    
window = Tk()
button = Button(window, text='Greet Someone!')
button.config(command=click)
button.config(font=('Open Sans', 50, 'bold'))
button.config(bg='#4287f5')
button.config(fg='#000000')
button.config(activebackground='#2f6ed4')
button.config(activeforeground='#000000')
label = Label(window, text=count)
label.config(font=('Monospace', 40, 'bold'))
label.pack()
button.pack()
window.mainloop()
window.title("Greeting Simulator")
window.state("zoomed")



