# Den permiso para correrlo ?

import tkinter as tk
import random #Para escoger una palabra random de la lista


#Lista de palabras posibles para el ahorcado
palabrasPosibles = ['magnetosfera','cohete','computadora']

palabra = random.choice(palabrasPosibles)
print(palabra)
caracteres = len(palabra)
for x in range(1,caracteres+1):
    print('_', end=' ')

root = tk.Tk() #
root.title("Place Example")

# Create a label
label = tk.Label(root, text="Label")

# Place the label at specific coordinates
label.place(x=50, y=50)

root.mainloop()
