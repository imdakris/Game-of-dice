from tkinter import *
import random, time


def dice_roll():
    """Randomly selects a file name and returns a value"""
    random_cube = random.choice(
        ["b.png", "b2.png", "b3.png", "b4.png", "b5.png", "b6.png"]
    )
    return random_cube


def img(event):
    """Returns a picture of a cube"""
    global throw1, throw2
    throw1 = PhotoImage(file=(dice_roll()))
    throw2 = PhotoImage(file=(dice_roll()))
    lab1['image'] = throw1
    lab2['image'] = throw2
    root.update()


root = Tk()
root.geometry("400x200")
root.title("Game of Dice")
root.resizable(height=False, width=False)
root.iconphoto(False, PhotoImage(file=("iconka.png")))
font = PhotoImage(file="holst.png")
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind('<1>', img)
root.mainloop()
