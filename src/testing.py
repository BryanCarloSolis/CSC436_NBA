import tkinter as tk
from tkinter import ttk
import mysql.connector as mysql

LARGEFONT =("Arial", 45)

class Application(tk.Tk):
     
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        frame = tk.Frame(self) 
        frame.pack(side = "bottom", fill = "both", expand = True)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterate through all the pages
        for pages in (Launch, Guest, Admin):
  
            page = pages(frame, self)
            page.configure(width=800, height=500)
            self.frames[pages] = page

            page.grid(row = 2, column = 2, sticky ="nsew")

        self.show_frame(Launch)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class Launch(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        guest_button = tk.Button(self, text = "Guest", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))
        #guest_button.grid(column = 0, row = 0)
        guest_button.place(relx = 0.55, rely = 0.5)

        admin_button = tk.Button(self, text = "Admin", bg = 'red', width = 5, height = 2,
        command = lambda : controller.show_frame(Admin))
        #admin_button.grid(column = 1, row = 0)
        admin_button.place(relx = 0.35, rely = 0.5)
  
          
  
  
# Guest page
class Guest(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        
        guest_button = tk.Button(self, text = "Guest", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))
        #guest_button.grid(column = 0, row = 0)
        guest_button.place(relx = 0.55, rely = 0.5)

  
  
  
  
# Admin Page
class Admin(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        admin_button = tk.Button(self, text = "Admin", bg = 'red', width = 5, height = 2,
        command = lambda : controller.show_frame(Admin))
        #admin_button.grid(column = 1, row = 0)
        admin_button.place(relx = 0.35, rely = 0.5)
  
  
# Driver Code
app = Application()
app.mainloop()


