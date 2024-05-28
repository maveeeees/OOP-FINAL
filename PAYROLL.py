
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from tkcalendar import DateEntry

# Create a connection to the SQLite database
con = sqlite3.connect("reg_db")
cursor = con.cursor()


def netIncome():
    paydate = paydate_entry.get_date()

    # Get the year from the selected date
    paydate = paydate.year

    gross = float(gross_entry.get())

    # SSS Contribution Computation
    sss_con, g_var = 180.00, gross
    while sss_con < 900.00 and g_var >= 4250:
        g_var -= 500.00
        sss_con += 22.50

    SSS_entry.config(state="normal")
    SSS_entry.delete(0, "end")
    SSS_entry.insert(0, f"{sss_con:.2f}")  # Format to two decimal places
    SSS_entry.config(state="readonly")

    # PhilHealth contribution
    s_co = paydate_entry.get().split("/")
    salary_cutoff_year = int(s_co[2])
    if salary_cutoff_year == 2019:
        premium_rate = 0.0275
        upper_value = 50000
    elif salary_cutoff_year == 2020:
        premium_rate = 0.03
        upper_value = 60000
    elif salary_cutoff_year == 2021:
        premium_rate = 0.035
        upper_value = 70000
    elif salary_cutoff_year == 2022:
        premium_rate = 0.04
        upper_value = 80000
    elif salary_cutoff_year == 2023:
        premium_rate = 0.045
        upper_value = 90000
    else:  # for years 2024-2025
        premium_rate = 0.05
        upper_value = 100000

    if gross <= 10000:
        philhealth_con = 10000 * premium_rate
    elif 10000 > gross > upper_value:
        philhealth_con = gross * premium_rate
    else:
        philhealth_con = upper_value * premium_rate

    phil1.config(state="normal")
    phil1.delete(0, "end")
    phil1.insert(0, f"{philhealth_con:.2f}")  # Format to two decimal places
    phil1.config(state="readonly")

    # ----------Withholding Tax ---------- #
    if 0.00 < gross <= 10417.00:
        withholding_tax = 0
    elif 10417.00 < gross <= 16666.00:
        over = gross - 10417.00
        withholding_tax = 0 + (over * 0.15)
    elif 16666.00 < gross <= 33332.00:
        over = gross - 16667.00
        withholding_tax = 937.50 + (over * 0.2)
    elif 33332.00 < gross <= 83332.00:
        over = gross - 33333.00
        withholding_tax = 4270.70 + (over * 0.25)
    elif 83332.00 < gross <= 333332.00:
        over = gross - 83333.00
        withholding_tax = 16770.70 + (over * 0.3)
    else:  # for gross pay equal to 333,333 and above
        over = gross - 333333.00
        withholding_tax = 91770.70 + (over * 0.35)

    income_tax = round(withholding_tax, 2)  # Round to two decimal places
    inctax.config(state="normal")
    inctax.delete(0, "end")
    inctax.insert(0, f"{income_tax:.2f}")  # Format to two decimal places
    inctax.config(state="readonly")

    pagibigcontri.config(state="normal")
    pagibigcontri.delete(0, "end")
    pagibigcontri.insert(0, "100")
    pagibigcontri.config(state="readonly")

    deduction = sss_con + philhealth_con + withholding_tax + 100 \
                + float(sssloan.get()) \
                + float(pagibigloan.get()) \
                + float(facultyloan.get()) \
                + float(facultydep.get()) \
                + float(salaryloan.get()) \
                + float(otherloan.get())

    total.config(state="normal")
    total.delete(0, "end")
    total.insert(0, f"{deduction:.2f}")  # Format to two decimal places
    total.config(state="readonly")

    net_income = gross - deduction
    net.config(state="normal")
    net.delete(0, "end")
    net.insert(0, f"{net_income:.2f}")  # Format to two decimal places
    net.config(state="readonly")


def grossIncome():
    basic_inc = float(rph0.get()) * float(hrcutoff0.get())
    honorarium_inc = float(rph.get()) * float(hrcutoff1.get())
    other_inc = float(rph2.get()) * float(hrcutoff.get())
    gross = basic_inc + honorarium_inc + other_inc
    gross_entry.insert(0, f"{gross:.2f}")  # Format to two decimal places

    inccutoff0.insert(0, f"{basic_inc:.2f}")  # Format to two decimal places
    inccutoff1.insert(0, f"{honorarium_inc:.2f}")  # Format to two decimal places
    inccutoff.insert(0, f"{other_inc:.2f}")  # Format to two decimal places
def search_employee():
    # Get employee number from the GUI
    employee_number = empnum.get()

    # Search for data in the database based on employee number
    query = "SELECT * FROM emp_tbl WHERE employee_number=?"
    cursor.execute(query, (employee_number,))
    result = cursor.fetchone()

    # Display the search result in the entry fields
    if result:
        # Update entry fields with search results
        firstname.delete(0, 'end')
        firstname.insert('end', result[0])  # First Name
        midname.delete(0, 'end')
        midname.insert('end', result[1])  # Middle Name
        surname.delete(0, 'end')
        surname.insert('end', result[2])  # Last Name
        civil.delete(0, 'end')
        civil.insert('end', result[7])  # Civil Status
        depstat.delete(0, 'end')
        depstat.insert('end', result[10])  # Qualified Dep. Status
        empstat.delete(0, 'end')
        empstat.insert('end', result[11])  # Employee Status
        designation.delete(0, 'end')
        designation.insert('end', result[9])  # Designation
        dept.delete(0, 'end')
        dept.insert('end', result[8])  # Department
    else:
        # Display a message if no matching record is found
        messagebox.showinfo("Search", "No record found")


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

empnum = Label(window, text="Employee Number:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
empnum.place(relx=.12, rely=.40)
empnum = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
empnum.place(relx=.22, rely=.40)

searchemp = Label(window, text="Search Employee:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
searchemp.place(relx=.12, rely=.44)
search = Button(window, text="Search", width=10, bg="red", fg="floral white", cursor='hand2', command=search_employee)
search.place(relx=.22, rely=.44)

dept = Label(window, text="Department:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
dept.place(relx=.12, rely=.48)
dept = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
dept.place(relx=.22, rely=.48)

firstname = Label(window, text="First Name:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
firstname.place(relx=.40, rely=.20)
firstname = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
firstname.place(relx=.50, rely=.20)

midname = Label(window, text="Middle Name:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
midname.place(relx=.40, rely=.24)
midname = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
midname.place(relx=.50, rely=.24)

surname = Label(window, text="Surname:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
surname.place(relx=.40, rely=.28)
surname = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
surname.place(relx=.50, rely=.28)

civil = Label(window, text="Civil Status:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
civil.place(relx=.40, rely=.32)
civil = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
civil.place(relx=.50, rely=.32)

depstat = Label(window, text="Qualified Dependent\nStatus:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
depstat.place(relx=.40, rely=.35)
depstat = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
depstat.place(relx=.50, rely=.36)

paydate = Label(window, text="Paydate:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
paydate.place(relx=.40, rely=.40)
paydate_entry = DateEntry(window, bg="light gray", width=27, borderwidth=5, font=("Helvetica", 10))
paydate_entry.place(relx=.50, rely=.40)
paydate_entry._set_text("mm/dd/yy")

empstat = Label(window, text="Employee Status:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
empstat.place(relx=.40, rely=.44)
empstat = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
empstat.place(relx=.50, rely=.44)

designation = Label(window, text="Designation:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
designation.place(relx=.40, rely=.48)
designation = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
designation.place(relx=.50, rely=.48)

label = Label(window, text="BASIC INCOME:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.12, rely=.56, anchor=W)

rph0 = Label(window, text="Rate/Hour:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
rph0.place(relx=.12, rely=.60)
rph0 = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
rph0.place(relx=.22, rely=.60)

hrcutoff0 = Label(window, text="No. of Hours/ Cut Off:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
hrcutoff0.place(relx=.12, rely=.64)
hrcutoff0 = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
hrcutoff0.place(relx=.22, rely=.64)

inccutoff0 = Label(window, text="Income/ Cut Off:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
inccutoff0.place(relx=.12, rely=.68)
inccutoff0 = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
inccutoff0.place(relx=.22, rely=.68)

label = Label(window, text="OTHER INCOME:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.12, rely=.76, anchor=W)

rph2 = Label(window, text="Rate/Hour:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
rph2.place(relx=.12, rely=.80)
rph2 = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
rph2.place(relx=.22, rely=.80)

hrcutoff1 = Label(window, text="No. of Hours/ Cut Off:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
hrcutoff1.place(relx=.12, rely=.84)
hrcutoff1 = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
hrcutoff1.place(relx=.22, rely=.84)

inccutoff1 = Label(window, text="Income/ Cut Off:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
inccutoff1.place(relx=.12, rely=.88)
inccutoff1= Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
inccutoff1.place(relx=.22, rely=.88)


label = Label(window, text="SUMMARY INCOME:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.40, rely=.56, anchor=W)

gross = Label(window, text="Gross Income:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
gross.place(relx=.40, rely=.60)
gross_entry = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
gross_entry.place(relx=.50, rely=.60)

net = Label(window, text="Net Income:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
net.place(relx=.40, rely=.64)
net = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
net.place(relx=.50, rely=.64)

label = Label(window, text="REGULAR DEDUCTIONS:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.40, rely=.72, anchor=W)

ssscontri = Label(window, text="SSS Contribution:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
ssscontri.place(relx=.40, rely=.76)
SSS_entry = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
SSS_entry.place(relx=.50, rely=.76)

phil = Label(window, text="PhilHealth Contribution:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
phil.place(relx=.40, rely=.80)
phil1 = Entry(window, bg="light gray", width=26, font=('Helvetica', 10))
phil1.place(relx=.52, rely=.80)

pagibigcontri = Label(window, text="Pagibig Contribution:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
pagibigcontri.place(relx=.40, rely=.84)
pagibigcontri = Entry(window, bg="light gray", width=28, font=('Helvetica', 10))
pagibigcontri.place(relx=.51, rely=.84)

inctax = Label(window, text="Income Tax\nContribution:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
inctax.place(relx=.40, rely=.88)
inctax = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
inctax.place(relx=.50, rely=.88)

label = Label(window, text="HONORARIUM INCOME:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.70, rely=.18, anchor=W)

rph = Label(window, text="Rate/Hour:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
rph.place(relx=.70, rely=.22)
rph = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
rph.place(relx=.80, rely=.22)

hrcutoff = Label(window, text="No. of Hours/ Cut Off:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
hrcutoff.place(relx=.70, rely=.26)
hrcutoff = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
hrcutoff.place(relx=.80, rely=.26)

inccutoff = Label(window, text="Income/ Cut Off:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
inccutoff.place(relx=.70, rely=.30)
inccutoff = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
inccutoff.place(relx=.80, rely=.30)

label = Label(window, text="OTHER DEDUCTIONS:", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.70, rely=.36, anchor=W)

sssloan = Label(window, text="SSS Loan:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
sssloan.place(relx=.70, rely=.40)
sssloan = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
sssloan.place(relx=.80, rely=.40)

pagibigloan = Label(window, text="Pagibig Loan:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
pagibigloan.place(relx=.70, rely=.44)
pagibigloan = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
pagibigloan.place(relx=.80, rely=.44)

facultydep = Label(window, text="Faculty Savings\nDeposit:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
facultydep.place(relx=.70, rely=.48)
facultydep = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
facultydep.place(relx=.80, rely=.48)

facultyloan = Label(window, text="Faculty Savings Loan:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
facultyloan.place(relx=.70, rely=.53)
facultyloan = Entry(window, bg="light gray", width=28, font=('Helvetica', 10))
facultyloan.place(relx=.81, rely=.53)

salaryloan = Label(window, text="Salary Loan:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
salaryloan.place(relx=.70, rely=.57)
salaryloan = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
salaryloan.place(relx=.80, rely=.57)

otherloan = Label(window, text="Other Loans:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
otherloan.place(relx=.70, rely=.61)
otherloan = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
otherloan.place(relx=.80, rely=.61)

label = Label(window, text="DEDUCTION SUMMARY :", font=('Helvetica', 11, 'bold'), bg="#FFFFFF")
label.place(relx=.70, rely=.66, anchor=W)

total = Label(window, text="Total Deductions:", font=('Helvetica', 10, 'bold'), bg="#FFFFFF" )
total.place(relx=.70, rely=.68)
total = Entry(window, bg="light gray", width=30, font=('Helvetica', 10))
total.place(relx=.80, rely=.68)

# Buttons
gross_btn = Button(window, text="Gross Income", width=14, bg="green", fg="floral white", cursor='hand2', command=grossIncome)
gross_btn.place(relx=.70, rely=.76)


net_btn = Button(window, text="Net Income", width=14, bg="blue", fg="floral white", cursor='hand2', command=netIncome)
net_btn.place(relx=.78, rely=.76)


save = Button(window, text="Save", width=14, bg="teal", fg="floral white", cursor='hand2')
save.place(relx=.86, rely=.76)


update = Button(window, text="Update", width=14, bg="indigo", fg="floral white", cursor='hand2')
update.place(relx=.74, rely=.80)

new = Button(window, text="New", width=14, bg="red", fg="floral white", cursor='hand2')
new.place(relx=.82, rely=.80)

window.mainloop()
