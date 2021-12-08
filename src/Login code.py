from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector###########################################


login = tk.Tk()
login.geometry("1000x1000")
login.title("NBA Login")
  
 
lblfrstrow = tk.Label(login, text ="User - Student or Admin: ", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(login, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(login, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(login, width = 35)
password.place(x = 150, y = 50, width = 100)
 
submitbtn = tk.Button(login, text ="Login",
                      bg ='blue', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)

def submit():
    user = Username.get()
    password = password.get()
    login(user, password)

#def login(user, password):
    
