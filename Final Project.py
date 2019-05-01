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
        self.master.title("Music Online System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg = 'black')
        self.frame = Frame(self.master, bg = 'black')
        self.frame.pack()

        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.NextName = StringVar()
        self.ThirdName = StringVar()
        self.FourthName = StringVar() 

        self.lblTitle = Label(self.frame, text = 'Music Group Online', font = ('Nanum Brush Script', 60, 'bold'),
                              bg = 'black', fg = 'white')
        self.lblTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        #======================================================================================================
        self.LoginFrame1 = LabelFrame(self.frame, width = 1350, height = 200
                                        , text = "Info", font = ('Nanum Brush Script', 20, 'bold'), relief = 'ridge', bg = 'dark blue', bd = 40)
        self.LoginFrame1.grid(row = 1, column = 0)

        self.LoginFrame2 = LabelFrame(self.frame, width = 1000, height = 200
                                      , text = "Log", font = ('Nanum Brush Script', 20, 'bold'), relief = 'ridge', bg = 'navy blue', bd = 40)
        self.LoginFrame2.grid(row = 2, column = 0) 
        #======================================================================================================
        self.lblFirstName = Label(self.LoginFrame1, text = 'First Name', font = ('Nanum Brush Script', 20, 'bold'), bd=5, bg = 'black', fg = 'white')
        self.lblFirstName.grid(row=0, column=0)
        self.txtFirstName = Entry(self.LoginFrame1, font = ('Nanum Brush Script', 20, 'bold'), bd = 5, textvariable = self.FirstName, width = 33)
        self.txtFirstName.grid(row = 0, column = 1, padx = 88)
        self.lblLastName = Label(self.LoginFrame1, text = 'Last Name', font = ('Nanum Brush Script', 20, 'bold'), bd = 5, bg = 'black', fg = 'white')
        self.lblLastName.grid(row = 1, column = 0)
        self.txtLastName = Entry(self.LoginFrame1, font = ('Nanum Brush Script', 20, 'bold'), bd = 5, textvariable = self.LastName, width = 33)
        self.txtLastName.grid(row = 1, column = 1, columnspan = 2, pady = 10)
        self.lblNextName = Label(self.LoginFrame1, text = 'Instrument of Choice', font = ('Nanum Brush Script', 20, 'bold'), bd = 5, bg = 'black', fg = 'white')
        self.lblNextName.grid(row = 2, column = 0)
        self.txtNextName = Entry(self.LoginFrame1, font = ('Nanum Brush Script', 20, 'bold'), bd = 5, textvariable = self.NextName, width = 33)
        self.txtNextName.grid(row = 2, column = 1, columnspan = 2, pady = 10)
        self.lblThirdName = Label(self.LoginFrame1, text = 'Genre of interest', font = ('Nanum Brush Script', 20, 'bold'), bd = 5, bg = 'black', fg = 'white')
        self.lblThirdName.grid(row = 3, column = 0)
        self.txtThirdName = Entry(self.LoginFrame1, font = ('Nanum Brush Script', 20, 'bold'), bd = 5, textvariable = self.ThirdName, width = 33)
        self.txtThirdName.grid(row = 3, column = 1, columnspan = 2, pady = 10)
        self.lblFourthName = Label(self.LoginFrame1, text = 'Zip code', font = ('Nanum Brush Script', 20, 'bold'), bd = 5, bg = 'black', fg = 'white')
        self.lblFourthName.grid(row = 4, column = 0)
        self.txtFourthName = Entry(self.LoginFrame1, font = ('Nanum Brush Script', 20, 'bold'), bd = 5, textvariable = self.FourthName, width = 33)
        self.txtFourthName.grid(row = 4
                                , column = 1, columnspan = 2, pady = 10) 
        #===========================#
        self.btnLogin = Button(self.LoginFrame2, text = 'Proceed', width = 15, font = ('Nanum Brush Script', 20, 'bold'),
                               bg = 'cadet blue', fg = 'black', command = self.Login_System)
        self.btnLogin.grid(row = 3, column = 0, pady = 20, padx = 8)
        self.btnReset = Button(self.LoginFrame2, text = 'Reset', width = 15, font = ('Nanum Brush Script', 20, 'bold'),
                               bg = 'cadet blue', fg = 'black', command = self.iReset)
        self.btnReset.grid(row = 3, column = 1, pady = 20, padx = 8)
        self.btnExit = Button(self.LoginFrame2, text = 'Exit', width = 15, font = ('Nanum Brush Script', 20, 'bold'),
                              bg = 'cadet blue', fg = 'black', command = self.iExit)
        self.btnExit.grid(row = 3, column = 2, pady = 20, padx = 8) 
        #===========================#

        
    def Login_System(self):
        input1 = (self.FirstName.get())
        input2 = (self.LastName.get())
        input3 = (self.NextName.get()) 
        input4 = (self.ThirdName.get()) 
        input5 = (self.FourthName.get()) 
         
        top = Toplevel()
        label1 = Label(top, text=input1, height=0, width=50)
        label1.pack()
        label2 = Label(top, text=input2, height=0, width=50)
        label2.pack()
        label3 = Label(top, text=input3, height=0, width=50)
        label3.pack()
        label4 = Label(top, text=input4, height=0, width=50)
        label4.pack()
        label5 = Label(top, text=input5, height=0, width=50)
        label5.pack()
        top.title("Individual Order for Group Placement")
         
            
        #msg = Message(top, MusicManagement)#
            
        print (input1, input2, input3, input4, input5)
        

    def iReset(self):
        self.FirstName.set("")
        self.LastName.set("")
        self.NextName.set("")
        self.ThirdName.set("")
        self.FourthName.set("") 

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Music Login System", "Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
            return

    def Login_window(self):
        self.SaleWindow = TopLevel.MusicManagement (self.master)
        self.app = SalesManagement(self.SaleWindow)
        

class MusicManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Management System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg = 'cadet blue')
        self.frame = Frame(self.master, bg = 'cadet blue')
        self.frame.pack()


    #=======================================================================
    
    #=======================================================================
if __name__ == '__main__':
    main() 
