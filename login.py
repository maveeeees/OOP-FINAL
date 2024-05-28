import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def show_login_form():
    for widget in frame.winfo_children():
        widget.destroy()

    # introduction
    welcome = Label(frame, text='Welcome!', fg='white', bg='#189492', font=('Comic Sans MS', 28, "bold"))
    welcome.place(x=55, y=12)
    heading = Label(frame, text='Sign in', fg='white', bg='#189492', font=('Cambria', 18, "bold"))
    heading.place(x=100, y=80)

    # user section
    username = Entry(frame, width=25, fg='black', border=2, bg='#DDFFFE', font=('Arial', 11, 'bold'))
    username.place(x=35, y=132)
    username.insert(0, 'Username')
    Frame(frame, width=210, height=2, bg='black').place(x=35, y=162)

    # password section
    password = Entry(frame, width=25, fg='black', border=2, bg='#DDFFFE', font=('Arial', 11, 'bold'))
    password.place(x=35, y=192)
    password.insert(0, 'Password')
    Frame(frame, width=210, height=2, bg='black').place(x=35, y=222)

    # buttons section
    Button(frame, width=25, pady=7, text='Sign in', bg='#50b8b5', fg='black', cursor='hand2', border=1,
           font=('Helvetica', 10, "bold")).place(x=35, y=255)

    label = Label(frame, text="Don't have an account?", fg='white', bg='#189492', cursor='hand2', font=('Helvetica', 9))
    label.place(x=35, y=322)

    sign_up = Button(frame, width=6, text='Sign up', border=0, bg='#189492', cursor='hand2', fg='white', command=show_signup_form)
    sign_up.place(x=186, y=322)
    canvas = tk.Canvas(frame, bg='white')
    canvas.place(x=187, y=338, width=46, height=1)

def show_signup_form():
    for widget in frame.winfo_children():
        widget.destroy()

    # User type
    user_type_label = Label(frame, text='User Type', fg='white', bg='#189492', font=('Arial', 11, 'bold'))
    user_type_label.place(x=50, y=50)
    user_type = Entry(frame, width=20, fg='black', border=2, bg='#DDFFFE', font=('Arial', 11))
    user_type.place(x=150, y=50)

    # Username
    username_label = Label(frame, text='Username', fg='white', bg='#189492', font=('Arial', 12, 'bold'))
    username_label.place(x=50, y=100)
    username_signup = Entry(frame, width=30, fg='black', border=2, bg='#DDFFFE', font=('Arial', 11))
    username_signup.place(x=150, y=100)

    # Password
    password_label = Label(frame, text='Password', fg='white', bg='#189492', font=('Arial', 12, 'bold'))
    password_label.place(x=50, y=150)
    password_signup = Entry(frame, width=30, fg='black', border=2, bg='#DDFFFE', font=('Arial', 11), show='*')
    password_signup.place(x=150, y=150)

    # Confirm Password
    confirm_password_label = Label(frame, text='Confirm Password', fg='white', bg='#189492', font=('Arial', 12, 'bold'))
    confirm_password_label.place(x=50, y=200)
    confirm_password_signup = Entry(frame, width=30, fg='black', border=2, bg='#DDFFFE', font=('Arial', 11), show='*')
    confirm_password_signup.place(x=150, y=200)

    # Email
    email_label = Label(frame, text='Email', fg='white', bg='#189492', font=('Arial', 12, 'bold'))
    email_label.place(x=50, y=250)
    email_signup = Entry(frame, width=30, fg='black', border=2, bg='#DDFFFE', font=('Arial', 11))
    email_signup.place(x=150, y=250)

    # Signup Button
    signup_button = Button(frame, width=25, pady=7, text='Sign up', bg='#50b8b5', fg='black', cursor='hand2', border=1, font=('Helvetica', 10, "bold"))
    signup_button.place(x=150, y=300)

    # Back to login
    back_to_login = Button(frame, width=6, text='Back', border=0, bg='#189492', cursor='hand2', fg='white', command=show_login_form)
    back_to_login.place(x=210, y=350)
    canvas = tk.Canvas(frame, bg='white')
    canvas.place(x=211, y=366, width=46, height=1)

window = tk.Tk()
window.title("Login System")

# background image

# frame
frame = Frame(window, width=300, height=370, bg='#189492')
frame.place(x=590, y=140)

# Show the login form by default
show_login_form()

window.geometry("1091x540")
window.mainloop()