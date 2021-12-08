from tkinter import *
import tkinter as tk
from tkinter import ttk
#import mysql.connector###########################################


self = tk.Tk()
self.geometry("500x500")
self.title("NBA Login")


#| | |
#v v v This is the code to copy over, the stuff above this is just to test it
################################################################################
def queryPage():
    queryName =tk.StringVar()

    queryLabel = tk.Label(self, text = "Enter your query here: ", )#login has to be the name of the master window
    queryLabel.place(x = 50, y = 20)

    queryEntrySpace = tk.Entry(self, textvariable = queryName, width = 35)
    queryEntrySpace.place(x = 180, y = 21, width = 50)


def submit():
    query = queryName.get()
    print("here it is", query)
    #So i have it printing the query just to test it, I think we're gonna have to use the
    #execute function that you used before but I'm not 100% sure
    #mycursor.execute(query)
    


submitbtn = tk.Button(self, text ="Submit Query", command = submit)
submitbtn.place(x = 150, y = 135, width = 75)
