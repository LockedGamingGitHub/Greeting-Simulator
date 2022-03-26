# Imports
from tkinter import *
from random import randint
import pickle

# Random Variables
count = 0
window = Tk()

# What Happens When You Click the Greet Button
def click():
    global count
    goodluck = randint(1, 50)
    if goodluck == 1:
        if count <= 100:
          if count == 0:
            SavedCount = pickle.load(open("score.dat", "rb"))
            if SavedCount >= 100:
              SavedCount = 0
              count = SavedCount
            else:
              count = SavedCount

        count+=10
        label.config(text=count)
    else:
        if count <= 100:
          if count == 0:
            SavedCount = pickle.load(open("score.dat", "rb"))
            if SavedCount >= 100:
              SavedCount = 0
              count = SavedCount
            else:
              count = SavedCount

          count+=1
          label.config(text=count)
        elif count >= 100:
          label.config(text="Sorry... I lost count", fg= "red")
    pickle.dump(count, open("score.dat", "wb"))

    

    
    
# Configuring the Greet Button
button = Button(window, text='Greet Someone Like a Gamer!')
button.config(command=click)
button.config(font=('Open Sans', 50, 'bold'))
button.config(bg='#b8860b')
button.config(fg='#000000')
button.config(activebackground='#daa520')
button.config(activeforeground='#000000')
# Configuring the Greet Counter
label = Label(window, text="Start greeting people!", fg= "blue")
label.config(font=('Monospace', 40, 'bold'))
# Displaying the Widgets
label.pack()
button.pack()
# Counfiguring the Window
window.title('Greeting Simulator ULTRA')
window.state("zoomed")
window.mainloop()




