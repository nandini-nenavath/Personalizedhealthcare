from tkinter import *
from PIL import Image, ImageTk

def on_resize(event):
    # resize the background image to the size of label
    image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
    # update the image of the label
    li.image = ImageTk.PhotoImage(image)
    li.config(image=li.image)

root = Tk()
root.geometry('800x600')

bgimg = Image.open('C:/Users/Dell/OneDrive/Desktop/my_details/panace.ai/disease_pred/dataset/img.jpg') # load the background image
li = Label(root)
li.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
li.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized



root.mainloop()