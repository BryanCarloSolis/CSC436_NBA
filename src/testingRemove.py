import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import mysql.connector as mysql

LARGEFONT =("Arial", 45)

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Kobebryant24",
    database = "NBA"
)

mycursor = db.cursor()

#############
# Functions #
#############

def add(indicator):
    if indicator == 1: # If from Player
        answer = simpledialog.askstring("Input", "Insert:\n\nPlayer Name\nAge\nWeight\nHeight\nTotal Points\nTotal Assists\nTotal Rebounds\nTotal Steals\nTotal Blocks\nTotal Turnovers\nTeam\n\nCOMMA SEPARATED")
        
        answer_to_tuple = tuple(answer.split(", "))
        sql = "INSERT INTO Players (player_name, player_age, player_weight, player_height, player_points, player_assists, player_rebounds, player_steals, player_blocks, player_turnovers, player_team) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        mycursor.execute(sql, answer_to_tuple)
        db.commit()

    elif indicator == 2: # If from Team
        answer = simpledialog.askstring("Input", "Insert:\n\nTeam Name\nWins\nLoses\nLocation\nYear Founded\nTotal Championships\nTeam Conference\nTeam Division\n\nCOMMA SEPARATED")

        answer_to_tuple = tuple(answer.split(", "))
        sql = "INSERT INTO Teams (team_name, team_wins, team_losses, team_location, year_founded, team_championships, team_conference, team_division) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        mycursor.execute(sql, answer_to_tuple)
        db.commit()
    elif indicator == 3: # If from Division
        answer = simpledialog.askstring("Input", "Insert:\n\nDivision Name\nDivison Wins\nDivision Losses\nDivision Conference\n\nCOMMA SEPARATED")
        
        answer_to_tuple = tuple(answer.split(", "))
        sql = "INSERT INTO Divisions (division_name, division_wins, division_losses, division_conference) VALUES (%s, %s, %s, %s)"

        mycursor.execute(sql, answer_to_tuple)
        db.commit()
    elif indicator == 4: # If from Conference
        answer = simpledialog.askstring("Input", "Insert:\n\nConference Name\nConference Wins\nConference Losses\n\nCOMMA SEPARATED")
        
        answer_to_tuple = tuple(answer.split(", "))
        sql = "INSERT INTO Conferences (conference_name, conference_wins, conference_losses) VALUES (%s, %s, %s)"

        mycursor.execute(sql, answer_to_tuple)
        db.commit()
    else: # If from Draft
        answer = simpledialog.askstring("Input", "Insert:\n\nDraft Pick Overall\nDraft Pick Round Relative\nDraft Pick Round\nDraft Year\nPlayer Team\nPlayer Name\nPlayer Age\nPlayer Weight\nPlayer Height\n\nCOMMA SEPARATED")
        
        answer_to_tuple = tuple(answer.split(", "))
        sql = "INSERT INTO Draft_2020 (draft_pick_overall, draft_pick_round_relative, draft_pick_round, draft_year, player_team, player_name, player_age, player_weight, player_height) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()

def remove(indicator):
    if indicator == 1: # If from Player
        answer = simpledialog.askstring("Input", "Insert:\n\nPlayer Name\n\nCOMMA SEPARATED")

        answer_to_tuple = tuple(answer.split(", "))
        sql = "REMOVE FROM players where player_name = (player_name) VALUES (%s)" 

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()
        
    elif indicator == 2: # If from Team
        answer = simpledialog.askstring("Input", "Insert:\n\nTeam Name\n\nCOMMA SEPARATED")
        
        answer_to_tuple = tuple(answer.split(", "))
        sql = "REMOVE FROM teams where team_name = (team_name) VALUES (%s)"

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()
        
    elif indicator == 3: # If from Division
        answer = simpledialog.askstring("Input", "Insert:\n\nDivision Name\n\nCOMMA SEPARATED")
        
        answer_to_tuple = tuple(answer.split(", "))
        sql = "REMOVE FROM divisions where division_name = (division_name) VALUES (%s)"

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()

    elif indicator == 4: # If from Conference
        answer = simpledialog.askstring("Input", "Insert:\n\nConference Name\n\nCOMMA SEPARATED")

        answer_to_tuple = tuple(answer.split(", "))
        sql = "REMOVE FROM conferences where conference_name = (conference_name) VALUES (%s)"

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()
        
    else: # If from Draft
        answer = simpledialog.askstring("Input", "Insert:\n\nDraft Pick Overall\n\nCOMMA SEPARATED")

        answer_to_tuple = tuple(answer.split(", "))
        sql = "REMOVE FROM drafts where draft_name = (draft_name) VALUES (%s)"

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()
        
def edit(indicator):
    if indicator == 1: # If from Player
        answer = simpledialog.askstring("Input", "Insert:\n\nDesired Attribute to Edit\nNew Value of Attribute\nPlayer Name\n\nCOMMA SEPARATED")

        answer_to_tuple = tuple(answer.split(", "))
        sql = "UPDATE players SET (change_attribute)(%s) = (new_attribute)(%s) WHERE player_name = (player_name) VALUES (%s)" #VALUES only at the end?

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()

    elif indicator == 2: # If from Team
        answer = simpledialog.askstring("Input", "Insert:\n\nDesired Attribute to Edit\nNew Value of Attribute\nTeam Name\n\nCOMMA SEPARATED")

        answer_to_tuple = tuple(answer.split(", "))
        sql = "UPDATE teams SET (change_attribute)(%s) = (new_attribute)(%s) WHERE team_name = (team_name) VALUES (%s)"

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()
        
    elif indicator == 3: # If from Division
        answer = simpledialog.askstring("Input", "Insert:\n\nDesired Attribute to Edit\nNew Value of Attribute\nDivision Name\n\nCOMMA SEPARATED")

        answer_to_tuple = tuple(answer.split(", "))
        sql = "UPDATE divisions SET (change_attribute)(%s) = (new_attribute)(%s) WHERE division_name = (division_name) VALUES (%s)"

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()
        
    elif indicator == 4: # If from Conference
        answer = simpledialog.askstring("Input", "Insert:\n\nDesired Attribute to Edit\nNew Value of Attribute\nTeam Name\n\nCOMMA SEPARATED")

        answer_to_tuple = tuple(answer.split(", "))
        sql = "UPDATE conferences SET (change_attribute)(%s) = (new_attribute)(%s) WHERE conference_name = (conference_name) VALUES (%s)"

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()
        
    else: # If from Draft
        answer = simpledialog.askstring("Input", "Insert:\n\nDesired Attribute to Edit\nNew Value of Attribute\nTeam Name\n\nCOMMA SEPARATED")

        answer_to_tuple = tuple(answer.split(", "))
        sql = "UPDATE drafts SET (change_attribute)(%s) = (new_attribute)(%s) WHERE draft_name = (draft_name) VALUES (%s)"

        mycursor.execute("SET foreign_key_checks = 0")
        mycursor.execute(sql, answer_to_tuple)
        db.commit()
        
def submit(queryName):
    mycursor = db.cursor()
    query = queryName.get()
    mycursor.execute(query)          #Does this work?
    print("here it is", query)

#########
# Pages #
#########
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

        queryLabel = tk.Label(self, text = "Enter your query here: ", )
        queryLabel.place(x = 310, y = 40)

        queryEntrySpace = tk.Entry(self, textvariable = queryName, width = 35)
        queryEntrySpace.place(x = 280, y = 75, width = 200)

        submitbtn = tk.Button(self, text = "Submit", command = lambda: submit(queryName))
        submitbtn.place(x = 340, y = 110, width = 75)

        back_button = tk.Button(self, text = "Back", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Launch))
        #No placement for these buttons?
  
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

        back_button = tk.Button(self, text = "Back", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Launch))

        # Placement
        add_button.place(relx = 0.25, rely = 0.5)
        remove_button.place(relx = 0.45, rely = 0.5)
        edit_button.place(relx = 0.65, rely = 0.5)
        #Add 'Back' button

# Guest page
class Add(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        
        # Buttons
        player_button = tk.Button(self, text = "Player", bg = 'red', width = 5, height = 2, 
        command = lambda : add(1))

        team_button = tk.Button(self, text = "Team", bg = 'red', width = 5, height = 2, 
        command = lambda : add(2))

        division_button = tk.Button(self, text = "Division", bg = 'red', width = 5, height = 2, 
        command = lambda : add(3))

        conference_button = tk.Button(self, text = "Conference", bg = 'red', width = 5, height = 2, 
        command = lambda : add(4))
    
        draft_player_button = tk.Button(self, text = "Draft Player", bg = 'red', width = 5, height = 2, 
        command = lambda : add(5))

        back_button = tk.Button(self, text = "Back", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Admin))
        
        # Placement
        player_button.place(relx = 0.15, rely = 0.5)
        team_button.place(relx = 0.3, rely = 0.5)
        division_button.place(relx = 0.45, rely = 0.5)
        conference_button.place(relx = 0.6, rely = 0.5)
        draft_player_button.place(relx = 0.75, rely = 0.5)
        #Add 'Back' button


class Remove(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        
        # Buttons
        player_button = tk.Button(self, text = "Player", bg = 'red', width = 5, height = 2, 
        command = lambda : remove(1))

        team_button = tk.Button(self, text = "Team", bg = 'red', width = 5, height = 2, 
        command = lambda : remove(2))

        division_button = tk.Button(self, text = "Division", bg = 'red', width = 5, height = 2, 
        command = lambda : remove(3))

        conference_button = tk.Button(self, text = "Conference", bg = 'red', width = 5, height = 2, 
        command = lambda : remove(4))
    
        draft_player_button = tk.Button(self, text = "Draft Player", bg = 'red', width = 5, height = 2, 
        command = lambda : remove(5))

        back_button = tk.Button(self, text = "Back", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Admin))

        # Placement
        player_button.place(relx = 0.15, rely = 0.5)
        team_button.place(relx = 0.3, rely = 0.5)
        division_button.place(relx = 0.45, rely = 0.5)
        conference_button.place(relx = 0.6, rely = 0.5)
        draft_player_button.place(relx = 0.75, rely = 0.5)
        #Add 'Back' button


class Edit(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        
        # Buttons
        player_button = tk.Button(self, text = "Player", bg = 'red', width = 5, height = 2, 
        command = lambda : edit(1))

        team_button = tk.Button(self, text = "Team", bg = 'red', width = 5, height = 2, 
        command = lambda : edit(2))

        division_button = tk.Button(self, text = "Division", bg = 'red', width = 5, height = 2, 
        command = lambda : edit(3))

        conference_button = tk.Button(self, text = "Conference", bg = 'red', width = 5, height = 2, 
        command = lambda : edit(4))
    
        draft_player_button = tk.Button(self, text = "Draft Player", bg = 'red', width = 5, height = 2, 
        command = lambda : edit(5))

        back_button = tk.Button(self, text = "Back", bg = 'red', width = 5, height = 2, 
        command = lambda : controller.show_frame(Admin))
        
        # Placement
        player_button.place(relx = 0.15, rely = 0.5)
        team_button.place(relx = 0.3, rely = 0.5)
        division_button.place(relx = 0.45, rely = 0.5)
        conference_button.place(relx = 0.6, rely = 0.5)
        draft_player_button.place(relx = 0.75, rely = 0.5)
        #Add 'Back' button

##########
# Driver #
##########
app = Application()
app.mainloop()


