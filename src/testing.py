import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import mysql.connector as mysql

LARGEFONT =("Arial", 45)

def add(indicator):
    
    if indicator == 1: # If from Player
        answer = simpledialog.askstring("Input", "Insert: Player name, age, weight, height, total points, total assists, total rebounds, total steals, total blocks, total turnovers, team",
            parent = Application)
        print(answer)
    elif indicator == 2: # If from Team
        print("test")
    elif indicator == 3: # If from Division
        print("test")
    elif indicator == 4: # If from Conference
        print("test")
    else: # If from Draft
        print("test")

def submit(queryName):
    query = queryName.get()
    print("here it is", query)


class Application(tk.Tk):
     
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        frame = tk.Frame(self) 
        frame.pack(side = "bottom", fill = "both", expand = True)

        # initializing frames to an empty array
        self.frames = {} 
  
        # iterate through all the pages
        for pages in (Launch, Guest, Admin, Add, Remove, Edit):
  
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

        # Buttons
        guest_button = tk.Button(self, text = "Guest", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))
        

        admin_button = tk.Button(self, text = "Admin", bg = 'red', width = 5, height = 2,
        command = lambda : controller.show_frame(Admin))

        # Placement
        guest_button.place(relx = 0.55, rely = 0.5)
        admin_button.place(relx = 0.35, rely = 0.5)
  
          
  
  
# Guest page
class Guest(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        queryName = tk.StringVar()

        queryLabel = tk.Label(self, text = "Enter your query here: ", )#login has to be the name of the master window
        queryLabel.place(x = 310, y = 40)

        queryEntrySpace = tk.Entry(self, textvariable = queryName, width = 35)
        queryEntrySpace.place(x = 280, y = 75, width = 200)

        submitbtn = tk.Button(self, text = "Submit", command = submit(queryName))
        submitbtn.place(x = 340, y = 110, width = 75)


        


  
  
  
  
# Admin Page
class Admin(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        # Buttons
        add_button = tk.Button(self, text = "Add", bg = 'red', width = 5, height = 2,
        command = lambda : controller.show_frame(Add))

        remove_button = tk.Button(self, text = "Remove", bg = 'red', width = 5, height = 2,
        command = lambda : controller.show_frame(Remove))

        edit_button = tk.Button(self, text = "Edit", bg = 'red', width = 5, height = 2,
        command = lambda : controller.show_frame(Edit))

        # Placement
        add_button.place(relx = 0.25, rely = 0.5)
        remove_button.place(relx = 0.45, rely = 0.5)
        edit_button.place(relx = 0.65, rely = 0.5)

# Guest page
class Add(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        
        # Buttons
        player_button = tk.Button(self, text = "Player", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))

        team_button = tk.Button(self, text = "Team", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))

        division_button = tk.Button(self, text = "Division", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))

        conference_button = tk.Button(self, text = "Conference", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))
    
        draft_player_button = tk.Button(self, text = "Draft Player", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))
        
        
        # Placement
        player_button.place(relx = 0.15, rely = 0.5)
        team_button.place(relx = 0.3, rely = 0.5)
        division_button.place(relx = 0.45, rely = 0.5)
        conference_button.place(relx = 0.6, rely = 0.5)
        draft_player_button.place(relx = 0.75, rely = 0.5)


class Remove(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        
        # Buttons
        player_button = tk.Button(self, text = "Player", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))

        team_button = tk.Button(self, text = "Team", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))

        division_button = tk.Button(self, text = "Division", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))

        conference_button = tk.Button(self, text = "Conference", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))
    
        draft_player_button = tk.Button(self, text = "Draft Player", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))

        # Placement
        player_button.place(relx = 0.15, rely = 0.5)
        team_button.place(relx = 0.3, rely = 0.5)
        division_button.place(relx = 0.45, rely = 0.5)
        conference_button.place(relx = 0.6, rely = 0.5)
        draft_player_button.place(relx = 0.75, rely = 0.5)

class Edit(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        
        # Buttons
        player_button = tk.Button(self, text = "Player", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))

        team_button = tk.Button(self, text = "Team", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))

        division_button = tk.Button(self, text = "Division", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))

        conference_button = tk.Button(self, text = "Conference", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))
    
        draft_player_button = tk.Button(self, text = "Draft Player", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Guest))
        
        
        # Placement
        player_button.place(relx = 0.15, rely = 0.5)
        team_button.place(relx = 0.3, rely = 0.5)
        division_button.place(relx = 0.45, rely = 0.5)
        conference_button.place(relx = 0.6, rely = 0.5)
        draft_player_button.place(relx = 0.75, rely = 0.5)

# Driver Code
app = Application()
app.mainloop()


