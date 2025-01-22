import string, numpy, time, math, csv
import cv2 as c
import tkinter as tk
from PIL import ImageTk, Image


curImage = ""


Mx,My = 0,0

def Moushe(event):
    Mx,My = event.x, event.y
    circ = mainCanv.create_oval(Mx,My,50,50,fill="goldenrod")
    print (Mx,My)


def makeWindow():
    global mainWin
    global mainCanv

    mainWin = tk.Tk()
    mainWin.config(height=1080,width=1920)
    mainWin.minsize(480, 270)  # setting up program basics and startup options
    mainWin.title("Tweakatronics")
    mainWin.state("zoomed")  # Starts the program maximized
    mainWin.grid_columnconfigure(0, weight=1)
    mainWin.bind('<Motion>', Moushe)

    mainCanv = tk.Canvas(mainWin,height=mainWin.winfo_height(),width=mainWin.winfo_width(), bg="blue")
    mainCanv.grid(row=0,column=0, sticky="ew")






makeWindow()
mainWin.mainloop()