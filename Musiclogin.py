from tkinter import*
import tkinter.messagebox 
from tkinter import ttk 
import random 
import time 
import datetime

def main(): 
    root = Tk()
    app = MusicLogin(root)

class MusicLogin: 
    def __init__(self, master):
        self.master = master
        self.master.title("Music Login System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg = 'cadet blue')
        self.frame = Frame(self.master, bg = 'cadet blue')
        self.frame.pack()
        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text = 'Music Login System', font = ('arial', 60, 'bold'), bg='cadet blue', fg='cornsilk')
        self.lblTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        user = (self.Username.get())
        paswd = (self.Password.get())
        #===========================#
        self.LoginFrame1 = LabelFrame(self.frame, width = 1350, height = 200
                                      , text = "Login", font = ('arial', 20, 'bold'), relief = 'ridge', bg = 'cadet blue', bd = 40)
        self.LoginFrame1.grid(row = 1, column = 0)
        self.LoginFrame2 = LabelFrame(self.frame, width = 1000, height = 200
                                      , text = "Log", font = ('arial', 20, 'bold'), relief = 'ridge', bg = 'cadet blue', bd = 40)
        self.LoginFrame2.grid(row = 2, column = 0) 

        #===========================#
        self.lblUsername = Label(self.LoginFrame1, text = 'Username', font = ('arial', 30, 'bold'), bd=22, bg = 'cadet blue', fg = 'Cornsilk')
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.LoginFrame1, font = ('arial', 30, 'bold'), bd = 7, textvariable = self.Username, width = 33)
        self.txtUsername.grid(row = 0, column = 1, padx = 88)
        self.lblPassword = Label(self.LoginFrame1, text = 'Password', font = ('arial', 30, 'bold'), bd = 22, bg = 'cadet blue', fg = 'Cornsilk')
        self.lblPassword.grid(row = 1, column = 0)
        self.txtPassword = Entry(self.LoginFrame1, font = ('arial', 30, 'bold'), show = '*', bd = 7, textvariable = self.Password, width = 33)
        self.txtPassword.grid(row = 1, column = 1, columnspan = 2, pady = 30) 
        #===========================#
        self.btnLogin = Button(self.LoginFrame2, text = 'Login', width = 15, font = ('arial', 30, 'bold'), bg = 'cadet blue', fg = 'Cornsilk', command = self.Login_System)
        self.btnLogin.grid(row = 3, column = 0, pady = 20, padx = 8)
        self.btnReset = Button(self.LoginFrame2, text = 'Reset', width = 15, font = ('arial', 30, 'bold'), bg = 'cadet blue', fg = 'Cornsilk', command = self.iReset)
        self.btnReset.grid(row = 3, column = 1, pady = 20, padx = 8)
        self.btnExit = Button(self.LoginFrame2, text = 'Exit', width = 15, font = ('arial', 30, 'bold'), bg = 'cadet blue', fg = 'Cornsilk', command = self.iExit)
        self.btnExit.grid(row = 3, column = 2, pady = 20, padx = 8) 
        #===========================#


    def Login_System(self):
        if (user == str(963852) and paswd == str(123456)):
            self.Login_window() 
        else:
            tkinter.messagebox.askyesno("Music Login System", "Invalid Login deatails.")
            self.Username.set("")
            self.Password.set("")

    def iReset(self):
        self.Username.set("")
        self.Password.set("")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Music Login Systems", "Confirm if you want to quit")
        if self.iExit > 0:
            self.master.destroy()
            return
            
    def Login_window(self):
        self.MusicWindow = Toplevel(self.master)
        self.app = MusicManagement(self.MusicWindow)

    class MusicManagement: 
        def __init__(self, master):
            self.master = master
            self.master.title("Music Login System")
            self.master.geometry("1350x750+0+0")
            self.master.config(bg = 'cadet blue')
            self.frame = Frame(self.master, bg = 'cadet blue')
            self.frame.pack()

            #========================#
            
            #========================#

if __name__ == '__main__':
                          main()
                          
