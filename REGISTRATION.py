import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import sqlite3

# CONNECTING TO DATABASE
con = sqlite3.connect("reg_db")


class EmployeeRegistration:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1330x800")
        self.window.title("Employee Registration")
        self.window.config(bg="#FFFFFF")

        self.first_name = ""
        self.middle_name = ""
        self.last_name = ""
        self.suffix = ""
        self.bday = ""
        self.gender = ""
        self.nationality = ""
        self.civil_status = ""
        self.department = ""
        self.designation = ""
        self.qualified_dep_status = ""
        self.employee_status = ""
        self.pay_date = ""
        self.employee_number = ""
        self.contact_number = ""
        self.email = ""
        self.social_media = ""
        self.social_media_id = ""
        self.address_line1 = ""
        self.address_line2 = ""
        self.city = ""
        self.state = ""
        self.country = ""
        self.zip_code = ""
        self.picture_path = ""

        self.load_image()
        self.create_widgets()
        self.get_info()
        self.get_dept()
        self.get_contact_info()
        self.get_address()
        self.get_picture_path()

        self.window.mainloop()

    def load_image(self):
        self.image2 = Image.open(r'C:\Users\LENOVO\PycharmProjects\GUI\images\whitee.jpg')
        self.bck_pic = ImageTk.PhotoImage(self.image2.resize((1366, 768)))
        self.lbl = Label(self.window, image=self.bck_pic)
        self.lbl.place(x=0, y=0)

    def create_widgets(self):
        self.label = Label(self.window, text="SE-RI's Employee Personal Information", font=('Helvetica', 20, 'bold'))
        self.label.place(relx=.5, rely=.05, anchor=N)

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("Selected file:", file_path)
            self.picpath_entry.insert(0, file_path)

    def choose_button(self):
        button = tk.Button(self.window, text="Choose Photo", highlightthickness=1, highlightbackground="#808080",
                           bg="#DCDCDC", command=self.choose_file)
        button.place(relx=0.11, rely=0.18)

    def get_info(self):
        # Entry widgets for first name, middle name, last name, and suffix
        self.first_name = Label(self.window, text="First Name", font=(9))
        self.first_name.place(relx=.19, rely=.13)
        self.first_name_entry = Entry(self.window, bg="#DCDCDC", width=25, highlightthickness=1)
        self.first_name_entry.place(relx=.19, rely=.17)

        self.middle_name = Label(self.window, text="Middle Name", font=(9))
        self.middle_name.place(relx=.33, rely=.13)
        self.middle_name_entry = Entry(self.window, bg="#DCDCDC", width=25, highlightthickness=1)
        self.middle_name_entry.place(relx=.33, rely=.17)

        self.last_name = Label(self.window, text="Last Name", font=(9))
        self.last_name.place(relx=.47, rely=.13)
        self.last_name_entry = Entry(self.window, bg="#DCDCDC", width=25, highlightthickness=1)
        self.last_name_entry.place(relx=.47, rely=.17)

        self.suffix = Label(self.window, text="Suffix", font=(9))
        self.suffix.place(relx=.61, rely=.13)
        self.suffix_entry = Entry(self.window, bg="#DCDCDC", width=33, highlightthickness=1)
        self.suffix_entry.place(relx=.61, rely=.17)

        # Label and DateEntry widget for date of birth
        self.bday = Label(self.window, text="Date of Birth", font=(11))
        self.bday.place(relx=.19, rely=.21)
        self.bday_entry = DateEntry(self.window, bg="#DCDCDC", width=20, borderwidth=2, font=("Helvetica", 11))
        self.bday_entry.place(relx=.19, rely=.25)
        self.bday_entry._set_text("mm/dd/yy")

        # Combobox widget for gender
        options = ["Male", "Female"]
        self.combo1 = Label(self.window, text="Gender", font=(9))
        self.combo1.place(relx=.33, rely=.21)
        self.combo1 = ttk.Combobox(self.window, values=options, cursor='hand2', state='readonly', font=("Helvetica", 11))
        self.combo1.place(relx=0.33, rely=0.25)
        self.combo1.set("--Select One--")

        # Entry widget for nationality
        options = ["Filipino"]
        self.combo2 = Label(self.window, text="Nationality", font=(9))
        self.combo2.place(relx=.47, rely=.21)
        self.combo2 = ttk.Combobox(self.window, values=options, cursor='hand2', state='readonly', font=("Helvetica", 11),
                                  width=18)
        self.combo2.place(relx=.47, rely=.25)
        self.combo2.set("Filipino")

        # Combobox widget for civil status
        options = ["Single", "Married", "Divorced", "Widowed"]
        self.combo3 = Label(self.window, text="Civil Status", font=(9))
        self.combo3.place(relx=.61, rely=.21)
        self.combo3 = ttk.Combobox(self.window, values=options, cursor='hand2', state='readonly', font=("Helvetica", 11),
                                  width=22)
        self.combo3.place(relx=0.61, rely=0.25)
        self.combo3.set("--Select One--")

    def get_dept(self):
        self.department = Label(self.window, text="Department", font=(9))
        self.department.place(relx=.19, rely=.29)
        self.department_entry = Entry(self.window, bg="#DCDCDC", width=40, highlightthickness=1,
                                      highlightbackground="#808080")
        self.department_entry.place(relx=.19, rely=.33)

        self.designation = Label(self.window, text="Designation", font=(9))
        self.designation.place(relx=.38, rely=.29)
        self.designation_entry = Entry(self.window, bg="#DCDCDC", width=32, highlightthickness=1,
                                       highlightbackground="#808080")
        self.designation_entry.place(relx=.38, rely=.33)

        options = ["Full Time", "Part Time", "Contractual"]
        self.combo4 = Label(self.window, text="Qualified Dep. Status", font=(9))
        self.combo4.place(relx=.535, rely=.29)
        self.combo4 = ttk.Combobox(self.window, values=options, cursor='hand2', state='readonly', font=("Helvetica", 11),
                                  width=34)
        self.combo4.place(relx=.535, rely=.33)
        self.combo4.set("--Select One--")

        # Entry widgets for employee status, pay date, and employee number
        self.empstat = Label(self.window, text="Employee Status", font=(9))
        self.empstat.place(relx=.19, rely=.37)
        self.empstat_entry = Entry(self.window, bg="#DCDCDC", width=45, highlightthickness=1,
                                   highlightbackground="#808080")
        self.empstat_entry.place(relx=.19, rely=.40)

        self.paydate = Label(self.window, text="Pay Date", font=(9))
        self.paydate.place(relx=.40, rely=.37)
        self.paydate_entry = DateEntry(self.window, bg="#DCDCDC", width=20, borderwidth=2, font=("Helvetica", 11))
        self.paydate_entry.place(relx=.40, rely=.40)
        self.paydate_entry._set_text("mm/dd/yy")

        self.empnum = Label(self.window, text="Employee Number", font=(9))
        self.empnum.place(relx=.55, rely=.37)
        self.empnum_entry = Entry(self.window, bg="#DCDCDC", width=45, highlightthickness=1,
                                  highlightbackground="#808080")
        self.empnum_entry.place(relx=.55, rely=.40)

    def get_contact_info(self):
        self.label = Label(self.window, text="Contact Info", font=('Helevetica', 14, 'bold'), bg='white')
        self.label.place(relx=.19, rely=.46, anchor=W)

        # Entry widgets for contact number, email, and social media
        self.contactno = Label(self.window, text="Contact No.", font=(9), bg='white')
        self.contactno.place(relx=.19, rely=.49)
        self.contactno_entry = Entry(self.window, bg="#DCDCDC", width=25, highlightthickness=1,
                                     highlightbackground="#808080")
        self.contactno_entry.place(relx=.19, rely=.52)

        self.email = Label(self.window, text="Email", font=(11), bg='white')
        self.email.place(relx=.315, rely=.49)
        self.email_entry = Entry(self.window, bg="#DCDCDC", width=30, highlightthickness=1,
                                 highlightbackground="#808080")
        self.email_entry.place(relx=.315, rely=.52)

        options = ["Facebook", "Instagram", "Viber"]
        self.combo5 = Label(self.window, text="Other (Social Media)", font=(9), bg='white')
        self.combo5.place(relx=.465, rely=.49)
        self.combo5 = ttk.Combobox(self.window, values=options, width=19, cursor='hand2', state='readonly',
                                  font=("Helvetica", 11))
        self.combo5.place(relx=0.465, rely=0.52)
        self.combo5.set("--Select One--")

        self.smedia = Label(self.window, text="Social Media ID/No.", font=(9))
        self.smedia.place(relx=.61, rely=.49)
        self.smedia_entry = Entry(self.window, bg="#DCDCDC", width=31, highlightthickness=1,
                                  highlightbackground="#808080")
        self.smedia_entry.place(relx=.61, rely=.52)

    def get_address(self):
        self.label = Label(self.window, text="Address", font=('Helvetica', 14, 'bold'), bg='white')
        self.label.place(relx=.19, rely=.58, anchor=W)

        # Entry widgets for address lines, city, state, country, and zip code
        self.add1 = Label(self.window, text="Address Line 1", font=(9), bg='white')
        self.add1.place(relx=.19, rely=.61)
        self.add1_entry = Entry(self.window, bg="#DCDCDC", width=45, highlightthickness=1,
                                highlightbackground="#808080")
        self.add1_entry.place(relx=.19, rely=.64)

        self.add2 = Label(self.window, text="Address Line 2", font=(9), bg='white')
        self.add2.place(relx=.40, rely=.61)
        self.add2_entry = Entry(self.window, bg="#DCDCDC", width=45, highlightthickness=1,
                                highlightbackground="#808080")
        self.add2_entry.place(relx=.40, rely=.64)

        self.city = Label(self.window, text="City/Municipality", font=(9), bg='white')
        self.city.place(relx=.61, rely=.61)
        self.city_entry = Entry(self.window, bg="#DCDCDC", width=31, highlightthickness=1,
                                highlightbackground="#808080")
        self.city_entry.place(relx=.61, rely=.64)

        self.state = Label(self.window, text="State/Province", font=(9), bg='white')
        self.state.place(relx=.19, rely=.67)
        self.state_entry = Entry(self.window, bg="#DCDCDC", width=45, highlightthickness=1,
                                 highlightbackground="#808080")
        self.state_entry.place(relx=.19, rely=.70)

        options = ["Philippines"]
        self.combo6 = Label(self.window, text="Country", font=(9), bg='white')
        self.combo6.place(relx=.40, rely=.67)
        self.combo6 = ttk.Combobox(self.window, values=options, width=26, cursor='hand2', state='readonly',
                                  font=("Helvetica", 11))
        self.combo6.place(relx=0.40, rely=0.70)
        self.combo6.set("--Select One--")

        self.zipcode = Label(self.window, text="Zip Code", font=(9), bg='white')
        self.zipcode.place(relx=.58, rely=.67)
        self.zipcode_entry = Entry(self.window, bg="#DCDCDC", width=38, highlightthickness=1,
                                   highlightbackground="#808080")
        self.zipcode_entry.place(relx=.58, rely=.70)

    def get_picture_path(self):
        self.picpath = Label(self.window, text="Picture Path", font=(9), bg='white')
        self.picpath.place(relx=.19, rely=.73)
        self.picpath_entry = Entry(self.window, bg="#DCDCDC", width=127, highlightthickness=1,
                                   highlightbackground="#808080")
        self.picpath_entry.place(relx=.19, rely=.76)

        # Buttons for save and cancel
        self.save = Button(self.window, text="SAVE", width=15, bg="blue", fg="floral white", cursor='hand2',
                           command=self.save_data)
        self.save.place(relx=.25, rely=.85)
        self.update = Button(self.window, text="UPDATE", width=15, bg="green", fg="floral white", cursor='hand2')
        self.update.place(relx=.35, rely=.85)
        self.search = Button(self.window, text="SEARCH", width=15, bg="magenta", fg="floral white", cursor='hand2')
        self.search.place(relx=.45, rely=.85)
        self.cancel = Button(self.window, text="CANCEL", width=15, bg="red", fg="floral white", cursor='hand2')
        self.cancel.place(relx=.55, rely=.85)
        self.choose_button()

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("Selected file:", file_path)
            self.picpath_entry.insert(0, file_path)


    def save_data(self):
        # Getting data from entry widgets
        self.first_name = self.first_name_entry.get()
        self.middle_name = self.middle_name_entry.get()
        self.last_name = self.last_name_entry.get()
        self.suffix = self.suffix_entry.get()
        self.bday = self.bday_entry.get()
        # Getting data from comboboxes
        self.gender = self.combo1.get()
        self.nationality = self.combo2.get()
        self.civil_status = self.combo3.get()
        # Getting data from other entry widgets
        self.department = self.department_entry.get()
        self.designation = self.designation_entry.get()
        self.qualified_dep_status = self.combo4.get()
        self.employee_status = self.empstat_entry.get()
        self.pay_date = self.paydate_entry.get()
        self.employee_number = self.empnum_entry.get()
        # Getting data from contact info entry widgets
        self.contact_number = self.contactno_entry.get()
        self.email = self.email_entry.get()
        self.social_media = self.combo5.get()
        self.social_media_id = self.smedia_entry.get()
        # Getting data from address entry widgets
        self.address_line1 = self.add1_entry.get()
        self.address_line2 = self.add2_entry.get()
        self.city = self.city_entry.get()
        self.state = self.state_entry.get()
        self.country = self.combo6.get()
        self.zip_code = self.zipcode_entry.get()
        # Getting picture path
        self.picture_path = self.picpath_entry.get()

        query = "INSERT INTO emp_tbl (first_name, middle_name, last_name, suffix, birthday, gender, nationality, civil_status, department, designation, qualified_dep_status, employee_status, pay_date, employee_number) VALUES ('" + self.first_name + "', '" + \
                self.middle_name + "', '" + self.last_name + "', '" + self.suffix + "','" + self.bday + "', '" + self.gender + "', '" + \
                self.nationality + "', '" + self.civil_status + "', '" + self.department + "', '" + self.designation + "', '" + self.qualified_dep_status + "', '" + \
                self.employee_status + "', '" + self.pay_date + "', '" + str(self.employee_number) + "')"

        query2 = "INSERT INTO emp_tbl2 (contact_number, email, social_media, social_media_id, address_line1, address_line2, city, state, country, zip_code, picture_path) VALUES ('" + str(
                self.contact_number) + "', '" + self.email + "', '" + self.social_media + "', '" + self.social_media_id + "', '" + self.address_line1 + "', '" + self.address_line2 + "', '" + self.city + "', '" + \
                 self.state + "', '" + self.country + "', '" + str(self.zip_code) + "', '" + self.picture_path +  "')"

        con.execute(query)
        con.execute(query2)
        con.commit()
        con.close()

        # Clearing entry fields after saving
        self.first_name_entry.delete(0, END)
        self.middle_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.suffix_entry.delete(0, END)
        self.bday_entry.delete(0, END)
        self.combo1.set("--Select One--")
        self.combo2.set("Filipino")
        self.combo3.set("--Select One--")
        self.department_entry.delete(0, END)
        self.designation_entry.delete(0, END)
        self.combo4.set("--Select One--")
        self.empstat_entry.delete(0, END)
        self.paydate_entry.delete(0, END)
        self.empnum_entry.delete(0, END)
        self.contactno_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.combo5.set("--Select One--")
        self.smedia_entry.delete(0, END)
        self.add1_entry.delete(0, END)
        self.add2_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.state_entry.delete(0, END)
        self.combo6.set("--Select One--")
        self.zipcode_entry.delete(0, END)
        self.picpath_entry.delete(0, END)


if __name__ == "__main__":
    EmployeeRegistration()
