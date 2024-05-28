query = "INSERT INTO emp_tbl (first_name, middle_name, last_name, suffix, birthday, gender, nationality, civil_status, department, designation, qualified_dep_status, employee_status, pay_date, employee_number) VALUES ('" + self.first_name + "', '" + \
        self.middle_name + "', '" + self.last_name + "', '" + self.suffix + "','" + self.bday + "', '" + self.gender + "', '" + \
        self.nationality + "', '" + self.civil_status + "', '" + self.department + "', '" + self.designation + "', '" + self.qualified_dep_status + "', '" + \
        self.employee_status + "', '" + self.pay_date + "', '" + str(self.employee_number) + "')"


def save_data():
    pay_date = paydate_entry.get_date()
    gross_income = float(gross_entry.get())
    sss_contribution = float(SSS_entry.get())
    philhealth_contribution = float(phil1.get())
    pagibig_contribution = float(pagibigcontri.get())
    income_tax_contribution = float(inctax.get())
    totalded = float(total.get())
    net_income_val = float(net.get())

    # Insert data into the database
    query = "INSERT INTO emp_tbl VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, (pay_date, gross_income, sss_contribution, philhealth_contribution, pagibig_contribution, income_tax_contribution, net_income_val))

    # Commit the changes
    con.commit()

    # Display a message box confirming successful saving
    messagebox.showinfo("Save", "Data saved successfully")


# Modify the "Save" button to call the save_data function
save = Button(window, text="Save", width=14, bg="purple", fg="floral white", cursor='hand2', command=save_data)
save.place(relx=.86, rely=.76)
