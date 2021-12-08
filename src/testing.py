from tkinter import *
import tkinter as tk
import mysql.connector as mysql

'''
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Kobebryant24",
    database = "NBA"
)

mycursor = db.cursor()

mycursor.execute("select * from Divisions")

for i in mycursor:
    print(i)

'''

root = Tk()
root.geometry("600x300")
root.title("2018-19 NBA Season")

guest_button = tk.Button(root, text = "Guest", bg = 'red', width = 5, height = 2)
#guest_button.grid(column = 0, row = 0)
guest_button.place(relx = 0.55, rely = 0.5)

admin_button = tk.Button(root, text = "Admin", bg = 'red', width = 5, height = 2)
#admin_button.grid(column = 1, row = 0)
admin_button.place(relx = 0.35, rely = 0.5)


root.mainloop()



#id = Label(root, text = 'Enter ID', font = ('bold', 10))
#id.place(x = 20, y = 30)

