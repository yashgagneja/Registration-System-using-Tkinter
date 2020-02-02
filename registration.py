# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
def login_verify():
    print("currently off")

def register_user():
    username_info=username.get()
    password_info=password.get()
    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    
    username_entry.delete(0, END)
    password_entry.delete(0,END)
    
    Label(screen1,text=" Registration Successful").pack()
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("login")
    screen2.geometry("300x250")
    Label(screen2,text="please enter details to login").pack()
    Label(screen2,text="").pack()
    global username_verify
    global password_verify
    username_verify=Stringvar()
    password_verify=Stringvar()
    Label(screen2,text="Username").pack()
    username_entry1=Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2,text="").pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_verify.pack()
    Label(screen2,text="")
    Button(screen2,text="Login",command=login_verify).pack()
    

def register():
    global screen1
    screen1= Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    
    username = StringVar()
    password = StringVar()
    Label(screen1,text="please enter details").pack()
    Label(screen1,text="").pack()
    Label(screen1,text = "Username").pack()
    username_entry=Entry(screen1,textvariable = username)
    username_entry.pack()
    Label(screen1,text = "Password").pack()
    password_entry=Entry(screen1,textvariable = password)
    password_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1, text="Register",command=register_user).pack()
    
def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0",bg = "grey", width = "300", font = ("Calibry",13)).pack()
    Label(text="").pack()
    Button(text="Login", height = "2", width="30",command = login).pack()
    Label(text="").pack()
    Button(text= "Register",height="2",width= "30",command = register).pack()
    
    screen.mainloop()
main_screen()
