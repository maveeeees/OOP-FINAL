import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

def clear_inputs():
    get_first_name.delete(0, END)
    get_middle_name.delete(0, END)
    get_last_name.delete(0, END)
    get_Suffix.delete(0, END)
    get_department.delete(0, END)
    get_designation.delete(0, END)
    get_username.delete(0, END)
    get_password.delete(0, END)
    get_confirm_password.delete(0, END)
    get_user_type.delete(0, END)
    get_user_status.delete(0, END)
    get_emp_num.delete(0, END)

def save_data_entry():
    first_name = get_first_name.get()
    middle_name = get_middle_name.get()
    last_name = get_last_name.get()
    Suffix = get_Suffix.get()
    department = get_department.get()
    designation = get_designation.get()
    username = get_username.get()
    password = get_password.get()
    confirm_password = get_confirm_password.get()
    user_type = get_user_type.get()
    user_status = get_user_status.get()
    emp_num = get_emp_num.get()

    con = sqlite3.connect("reg_db")
    save_data_query = """
    INSERT INTO personal_infotbl (first_name, middle_name, last_name, Suffix, department, designation, username, password, confirm_password, user_type, user_status, emp_num) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    con.execute(save_data_query, (first_name, middle_name, last_name, Suffix, department, designation, username,password, confirm_password, user_type, user_status, emp_num))
    con.commit()
    con.close()
    tk.messagebox.showinfo("Data Updated", "Data has been updated to the database")

def exit_program():
    main.destroy()
    tk.messagebox.showinfo("Process cancelled", "The program has been cancelled.")

main = tk.Tk()
main.title("Personal Info")

detail_frame = (tk.Frame(main, width=870, height=300, bg='light gray').place(relx=.13, rely=.230))

# ----------------- FRAME 1 ------------------------------------------------

image = Image.open(r'C:\Users\LENOVO\PycharmProjects\GUI\images\kk.jpg')
image = image.resize((130, 130))
pic = ImageTk.PhotoImage(image)
image_label = tk.Label(main, image=pic)
image_label.place(relx=.135, rely=.100)

#           -- First Name --
first_name = tk.Label(main, text="First Name", bg='light gray')
first_name.place( relx=.260, rely=.280)
get_first_name = tk.Entry(main)
get_first_name.place( height=27, relx=.260, rely=.330)

#         --- Middle Name ---
middle_name = tk.Label(main, text="Middle Name", bg='light gray')
middle_name.place( relx=.370, rely=.280)
get_middle_name = tk.Entry(main)
get_middle_name.place( height=27, relx=.370, rely=.330)

#         --- Last Name ---
last_name = tk.Label(main, text="Last Name", bg='light gray')
last_name.place( relx=.480, rely=.280)
get_last_name = tk.Entry(main)
get_last_name.place( height=27, relx=.480, rely=.330)

#            --- Suffix ---
Suffix = tk.Label(main, text="Suffix", bg='light grey')
Suffix.place( relx=.590, rely=.280)
get_Suffix = tk.Entry(main)
get_Suffix.place(height=27, relx=.590, rely=.330)

#               --- department ---
department = tk.Label(main, text="Department", bg='light grey')
department.place( relx=.700, rely=.280)
get_department = tk.Entry(main)
get_department.place(height=27, relx=.700, rely=.330)

#                --- designation ---
designation = tk.Label(main, text="Designation", bg='light grey')
designation.place( relx=.14, rely=.430)
get_designation = tk.Entry(main)
get_designation.place(height=27, width=250, relx=.14 ,rely=.480)

#                --- Username ---

username = tk.Label(main, text="Username", bg='light grey')
username.place( relx=.370, rely=.430)
get_username = tk.Entry(main)
get_username.place(height=27, width=180, relx=.360, rely=.480)

#                --- Password ---

password = tk.Label(main, text="Password", bg='light grey')
password.place( relx=.520, rely=.430)
get_password = tk.Entry(main)
get_password.place(height=27, width=340,relx=.520, rely=.480)

#                --- Confirm Password ---

confirm_password = tk.Label(main, text="Confirm Password", bg='light grey')
confirm_password.place( relx=.14, rely=.570)
get_confirm_password = tk.Entry(main)
get_confirm_password.place(height=27, width=250,relx=.14, rely=.630)

#                --- User Type ---

user_type = tk.Label(main, text="User Type", bg='light grey')
user_type.place( relx=.370, rely=.570)
get_user_type = tk.Entry(main)
get_user_type.place(height=27, width=180, relx=.360, rely=.630)

#                --- User Status ---

user_status = tk.Label(main, text="User Status", bg='light grey')
user_status.place( relx=.520, rely=.570)
get_user_status = tk.Entry(main)
get_user_status.place(height=27, width=180, relx=.520, rely=.630)

#                --- Employee Number ---

emp_num = tk.Label(main, text="Employee Number", bg='light grey')
emp_num.place( relx=.680, rely=.570)
get_emp_num = tk.Entry(main)
get_emp_num.place(height=27, width=180, relx=.680, rely=.630)

#                --- Buttons ---

update = tk.Button(main, text="Update", bg="blue", fg='white', width=10,command= save_data_entry)
update.place( width=100,relx=.25, rely=.730)

delete = tk.Button(main, text="Delete", bg="#EEC900", fg='black', width=10, command=clear_inputs)
delete.place( width=100,relx=.34, rely=.730)

cancel = tk.Button(main, text="Cancel", bg="light gray", fg='black', width=10, command=exit_program)
cancel.place( width=100,relx=.43, rely=.730)

main.geometry('1200x500')
main.mainloop()
