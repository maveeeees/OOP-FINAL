import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from tkcalendar import DateEntry

# Create a connection to the SQLite database
con = sqlite3.connect("reg_db")
cursor = con.cursor()

# Create the main window
window = tk.Tk()
window.geometry("1366x768")
window.title("Payroll Page")

frame = Frame(window, width=1366, height=768, bg="#FFFFFF")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Load background image
image2 = Image.open(r'C:\Users\LENOVO\PycharmProjects\GUI\images\white.jpg')
bck_pic = ImageTk.PhotoImage(image2.resize((1366, 768)))
lbl = Label(window, image=bck_pic)
lbl.place(x=0, y=0)

label = Label(window, text="SE-RI's CHOICE PAYROLL", font=('Helvetica', 20, 'bold'), bg="floral white")
label.place(relx=.50, rely=.08, anchor=N)

label = Label(window, text="EMPLOYEE BASIC INFO:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.12, rely=.17, anchor=W)

image1 = Image.open(r'C:\Users\LENOVO\PycharmProjects\GUI\images\pic.jpg')
user_pic = ImageTk.PhotoImage(image1.resize((130,130)))
lbl = Label(window, image=user_pic)
lbl.place(relx=.12, rely=.20)

empnum = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
empnum.place(relx=.22, rely=.40)

search = Button(window, text="Search", width=10, bg="red", fg="floral white", cursor='hand2', command=search_employee)
search.place(relx=.22, rely=.44)

dept = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
dept.place(relx=.22, rely=.48)

firstname = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
firstname.place(relx=.50, rely=.20)

midname = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
midname.place(relx=.50, rely=.24)

surname = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
surname.place(relx=.50, rely=.28)

civil = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
civil.place(relx=.50, rely=.32)

depstat = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
depstat.place(relx=.50, rely=.36)

paydate = DateEntry(window, bg="light gray", width=23, borderwidth=5, font=("Helvetica", 10))
paydate.place(relx=.50, rely=.40)
paydate._set_text("mm/dd/yy")

empstat = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
empstat.place(relx=.50, rely=.44)

designation = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
designation.place(relx=.50, rely=.48)

label = Label(window, text="BASIC INCOME:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.12, rely=.56, anchor=W)

rph = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
rph.place(relx=.22, rely=.60)

hrcutoff = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
hrcutoff.place(relx=.22, rely=.64)

inccutoff = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
inccutoff.place(relx=.22, rely=.68)

label = Label(window, text="OTHER INCOME:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.12, rely=.76, anchor=W)

rph2 = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
rph2.place(relx=.22, rely=.80)

hrcutoff1 = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
hrcutoff1.place(relx=.22, rely=.84)

inccutoff1 = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
inccutoff1.place(relx=.22, rely=.88)

label = Label(window, text="SUMMARY INCOME:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.40, rely=.56, anchor=W)

gross = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
gross.place(relx=.50, rely=.60)

net = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
net.place(relx=.50, rely=.64)

label = Label(window, text="REGULAR DEDUCTIONS:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.40, rely=.72, anchor=W)

ssscontri = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
ssscontri.place(relx=.50, rely=.76)

phil = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
phil.place(relx=.52, rely=.80)

pagibigcontri = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
pagibigcontri.place(relx=.51, rely=.84)

inctax = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
inctax.place(relx=.50, rely=.88)

label = Label(window, text="OTHER DEDUCTIONS:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.70, rely=.20, anchor=W)

sssloan = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
sssloan.place(relx=.80, rely=.24)

pagibigloan = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
pagibigloan.place(relx=.80, rely=.28)

facultydep = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
facultydep.place(relx=.80, rely=.32)

facultyloan = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
facultyloan.place(relx=.81, rely=.37)

salaryloan = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
salaryloan.place(relx=.80, rely=.41)

otherloan = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
otherloan.place(relx=.80, rely=.45)

label = Label(window, text="DEDUCTION SUMMARY :", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.70, rely=.53, anchor=W)

total = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
total.place(relx=.80, rely=.57)

# Buttons
gross_btn = Button(window, text="Gross Income", width=14, bg="green", fg="floral white", cursor='hand2')
gross_btn.place(relx=.70, rely=.62)

net_btn = Button(window, text="Net Income", width=14, bg="blue", fg="floral white", cursor='hand2')
net_btn.place(relx=.78, rely=.62)

save_btn = Button(window, text="Save", width=14, bg="purple", fg="floral white", cursor='hand2')
save_btn.place(relx=.86, rely=.62)

update_btn = Button(window, text="Update", width=14, bg="indigo", fg="floral white", cursor='hand2')
update_btn.place(relx=.74, rely=.66)

new_btn = Button(window, text="New", width=14, bg="teal", fg="floral white", cursor='hand2')
new_btn.place(relx=.82, rely=.66)

window.mainloop()
