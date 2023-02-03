import tkinter
import backend
from tkinter import *

# Importamos las librerias previamente instaladas.

import nltk
from nltk.stem.lancaster import \
    LancasterStemmer  # Este es un modulo que se encuentra en la libreria NLTK que nos proporciona las herramientas necesarias para el lenguaje natural
import tensorflow
import tflearn

# Agregamos dos librerias adicionales para responderle al usuario.
import \
    random  # Sirve para responder aleatoriamene cuando ya conoces la categoria a la que corresponde la frase ingresada por el usuario.
import numpy as np
import pickle  # Libreria que sirve para guardar variables temporales de manera permanente.

stemmer = LancasterStemmer()

base = Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

ChatLog = Text(base, bd=10, bg="white", height="8", width="50", font="Arial")
ChatLog.config(foreground="black", font=("Verdana", 12))
ChatLog.insert(END, "Bienvenido a Electrox" + '\n\n')
ChatLog.place(x=6, y=6, height=386, width=370)

scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
scrollbar.place(x=376, y=6, height=386)

ChatLog.config(state=DISABLED)


def send():
    msg = EntryBox.get("1.0", "end-1c").strip()
    EntryBox.delete("0.0", END)

    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, "You : " + msg + '\n\n')
    ChatLog.config(foreground="black", font=("verdana", 12))
    ChatLog.yview(END)

def chatbot_respond():

   return backend.get_response(send())



SendButton = Button(base, font=("verdana", 12, 'bold'), text="Send", width=9,
                    height=5, bd=0, bg="skyblue", activebackground="gold",
                    fg='#ffffff', command=send)

SendButton.place(x=282, y=401, height=90)

EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")
EntryBox.place(x=6, y=401, height=90, width=265)

base.bind('<Return>', lambda event: send())
base.mainloop()