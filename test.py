from tkinter import *
from tkinter import simpledialog
from functools import partial
import hashlib, os, sqlite3

with sqlite3.connect("AccountsVault.db") as db:
    cursor = db.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS masterkey(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);    
""")    

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")

display = Tk()
display.title("AMS")

def delete1():
    display.destroy()

def delete2():
    display.destroy()

def delete3():
    display.destroy()

def delete4():
    display.destroy()

def destroyDisplay():
    for widget in display.winfo_children():
        widget.destroy()

def popp(text):
    answer = simpledialog.askstring("Info Required", text)
    return answer

def AcctVault():
    destroyDisplay()
    def addAcct():
        wsite = "Website"
        uname3 = "Username/Email"
        pword3 = "Password"
        website = popp(wsite)
        username = popp(uname3)
        password = popp(pword3)

        insertBox = """INSERT INTO vault(website,username,password)
        VALUES(?,?,?)"""

        cursor.execute(insertBox, (website, username, password))
        db.commit()

        AcctVault()

    def removeAcct(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()

        AcctVault()
    display.title("Accounts Vault")
    display.geometry("750x350")    
    Label(display, text = " Accounts Vault", font=("Calibri", 20)).grid(column = 1, pady= 10)
    Button(display, text = "+", command = addAcct).grid(column=1,pady=10)

    Label(display, text = "Website").grid(row = 2, column = 0, padx = 80)
    Label(display, text = "Username").grid(row = 2, column = 1, padx = 88)
    Label(display, text = "Password").grid(row = 2, column = 2, padx = 88)

    cursor.execute("SELECT * FROM vault")
    if(cursor.fetchall() != None):
        i = 0
        while True:
            cursor.execute("SELECT * FROM vault")
            array = cursor.fetchall()

            Label(display, text = (array[i][1]), font = ("Calibri, 12")).grid(column = 0, row = i + 3)
            Label(display, text = (array[i][2]), font = ("Calibri, 12")).grid(column = 1, row = i + 3)
            Label(display, text = (array[i][3]), font = ("Calibri, 12")).grid(column = 2, row = i + 3)

            Button(display, text = "Remove", command= partial(removeAcct, array [i][0])).grid(column = 3, row = i + 3, pady = 10)
            i = i + 1

            cursor.execute("SELECT * FROM vault")
            if(len(cursor.fetchall()) < i):
                break

def signin_valid():
    destroyDisplay()
    display.title("Sign-In Verification")
    display.geometry("250x150")
    Label(display, text = "Signed In Successfully").pack()
    Button(display, text = "View Your Accounts Vault", command = AcctVault).pack()

def pwordNotValid():
    destroyDisplay()
    display.title("Sign In Verification")
    display.geometry("250x150")
    Label(display, text = "Invalid Password").pack()
    Button(display, text = "Close", command = login_box).pack() 

def unameNotValid():
    destroyDisplay()
    display.title("Sign In Verification")
    display.geometry("250x150")
    Label(display, text = "There is no record of that username").pack()
    Button(display, text = "Close", command = login_box).pack()       


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
    
    Label(display, text = "New Account Created\n Close the Window", font = ("calibri", 12)).pack()
    Button(display, text = "Close", command = login_box).pack()

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
    destroyDisplay()
    display.title("Create Account")
    display.geometry("400x250")

    global uname
    uname = StringVar()
    global pword
    pword = StringVar()
    global uname_input
    global pword_input
    
    
    
    Label(display, text = "Fillout the following information").pack()
    Label(display, text = "").pack()
    Label(display, text = "USERNAME").pack()
    uname_input = Entry(display, textvariable = uname)
    uname_input.pack()
    Label(display, text = "Pword").pack()
    pword_input =  Entry(display, textvariable = pword, show = "*")
    pword_input.pack()
    
    Label(display, text = "").pack()
    Button(display, text = "Create Account", command = userInfo).pack()

def signin():
    destroyDisplay()
    display.title("Sign-In")
    display.geometry("400x250")
    Label(display, text = "Enter Your Sign-In Credentials").pack()
    Label(display, text = "").pack()

    global uname_verif
    global pword_verif

    uname_verif = StringVar()
    pword_verif = StringVar()  

    global uname_input2
    global pword_input2

    Label(display, text = "Username").pack()
    uname_input2 = Entry(display, textvariable = uname_verif)
    uname_input2.pack()
    Label(display, text = "").pack()
    Label(display, text = "Password").pack()
    pword_input2 = Entry(display, textvariable = pword_verif, show = "*")
    pword_input2.pack()
    Label(display, text = "").pack()
    Button(display, text = "Sign-In", command = signin_verif).pack()


def login_box():
    destroyDisplay()
    display.geometry("400x250")
    Label(display, text = "Accounts Management Service", font = ("Calibri", 20)).pack()
    Label(text = "").pack()
    Button(text = "Sign-In", command = signin).pack()
    Label(text = "").pack()
    Button(text = "Create Account", command = create_acct).pack()

    display.mainloop()
login_box()
