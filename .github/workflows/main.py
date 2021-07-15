from tkinter import *
import hashlib, os


def delete1():
    display2.destroy()

def delete2():
    display4.destroy()

def delete3():
    display5.destroy()

def delete4():
    display6.destroy()

def AcctVault():
    global display6



def signin_valid():
    global display4
    display4 = Toplevel(display)
    display4.title("Sign-In Verification")
    display4.geometry("250x150")
    Label(display4, text = "Signed In Successfully").pack()
    Button(display4, text = "Close", command = delete2).pack()

def pwordNotValid():
    global display5
    display5 = Toplevel(display)
    display5.title("Sign In Verification")
    display5.geometry("250x150")
    Label(display5, text = "Invalid Password").pack()
    Button(display5, text = "Close", command = delete3).pack() 

def unameNotValid():
    global display6
    display6 = Toplevel(display)
    display6.title("Sign In Verification")
    display6.geometry("250x150")
    Label(display6, text = "There is no record of that username").pack()
    Button(display6, text = "Close", command = delete4).pack()       


def userInfo():
    uname_info = uname.get()
    pword_info = pword.get()
    h = hashlib.md5(pword_info.encode())
    h = h.hexdigest()
    file = open(uname_info, "w")
    file.write(uname_info + "\n")
    file.write(h)
    
    file.close()
    uname_input.delete(0, END)  
    pword_input.delete(0, END)
    
    Label(display2, text = "New Account Created\n Close the Window", font = ("calibri", 12)).pack()
    Button(display2, text = "Close", command = delete1).pack()

def signin_verif():
  
    uname2 = uname_verif.get()
    pword2 = pword_verif.get()
    h = hashlib.md5(pword2.encode())
    h = h.hexdigest()
    uname_input2.delete(0, END)
    pword_input2.delete(0, END)

    list_of_files = os.listdir()
    if uname2 in list_of_files:
        file1 = open(uname2, "r")
        verify = file1.read().splitlines()
        if h in verify:
            signin_valid()
        else:
            pwordNotValid()

    else:
        unameNotValid()

def create_acct():
    global display2
    display2 = Toplevel(display)
    display2.title("Create Account")
    display2.geometry("400x250")

    global uname
    uname = StringVar()
    global pword
    pword = StringVar()
    global uname_input
    global pword_input
    
    
    
    Label(display2, text = "Fillout the following information").pack()
    Label(display2, text = "").pack()
    Label(display2, text = "USERNAME").pack()
    uname_input = Entry(display2, textvariable = uname)
    uname_input.pack()
    Label(display2, text = "Pword").pack()
    pword_input =  Entry(display2, textvariable = pword, show = "*")
    pword_input.pack()
    
    Label(display2, text = "").pack()
    Button(display2, text = "Create Account", command = userInfo).pack()

def signin():
    global display3
    display3 = Toplevel(display)
    display3.title("Sign-In")
    display3.geometry("400x250")
    Label(display3, text = "Enter Your Sign-In Credentials").pack()
    Label(display3, text = "").pack()

    global uname_verif
    global pword_verif

    uname_verif = StringVar()
    pword_verif = StringVar()  

    global uname_input2
    global pword_input2

    Label(display3, text = "Username").pack()
    uname_input2 = Entry(display3, textvariable = uname_verif)
    uname_input2.pack()
    Label(display3, text = "").pack()
    Label(display3, text = "Password").pack()
    pword_input2 = Entry(display3, textvariable = pword_verif, show = "*")
    pword_input2.pack()
    Label(display3, text = "").pack()
    Button(display3, text = "Sign-In", command = signin_verif).pack()


def login_box():
    global display
    display = Tk()
    display.geometry("400x250")
    display.title("AMS")
    Label(display, text = "Accounts Management Service", font = ("Calibri", 20)).pack()
    Label(text = "").pack()
    Button(text = "Sign-In", command = signin).pack()
    Label(text = "").pack()
    Button(text = "Create Account", command = create_acct).pack()

    display.mainloop()
login_box()
