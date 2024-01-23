from tkinter import Tk, Label, PhotoImage
from tkinter.constants import CENTER
from tkinter import Event
import random

def get_random_dice_image() -> str:
    """Randomly selects a file name for a dice image"""
    return random.choice(["b.png", "b2.png", "b3.png", "b4.png", "b5.png", "b6.png"])

def update_dice_images(count: int, dice_labels: tuple, window: Tk, dice_images: list) -> None:
    """Updates dice images with the effect of rolling dice"""
    if count > 0:
        # Update the images with random dice throws
        for i, dice_label in enumerate(dice_labels):
            dice_images[i].configure(file=get_random_dice_image())
            dice_label["image"] = dice_images[i]

        # Update the Tkinter window
        window.update()

        # Schedule the next image update after 120 milliseconds
        window.after(120, lambda: update_dice_images(count-1, dice_labels, window, dice_images))

def roll_dice(event: Event, dice_labels: tuple, window: Tk, dice_images_list: list) -> None:
    """Callback function for rolling dice on mouse click"""
    update_dice_images(18, dice_labels, window, dice_images_list)

# Initialize the main Tkinter window
main_window = Tk()
main_window.geometry("400x200")
main_window.title("Game of Dice")
main_window.resizable(height=False, width=False)
main_window.iconphoto(False, PhotoImage(file="iconka.png"))

# Load background image
background_image = PhotoImage(file="holst.png")
Label(main_window, image=background_image).pack()

# Create PhotoImage objects for initial dice throws
initial_dice_image1 = PhotoImage(file=get_random_dice_image())
initial_dice_image2 = PhotoImage(file=get_random_dice_image())

# Create labels for displaying dice throws
dice_label1 = Label(main_window, image=initial_dice_image1)
dice_label1.place(relx=0.3, rely=0.5, anchor=CENTER)

dice_label2 = Label(main_window, image=initial_dice_image2)
dice_label2.place(relx=0.7, rely=0.5, anchor=CENTER)

# Create PhotoImage objects for dice throws
dice_image1 = PhotoImage()
dice_image2 = PhotoImage()

# Store references to PhotoImage objects in a list
dice_images = [dice_image1, dice_image2]

# Bind the roll_dice function to mouse click event
main_window.bind("<1>", lambda event: roll_dice(event, (dice_label1, dice_label2), main_window, dice_images))

# Start the Tkinter main loop
main_window.mainloop()
