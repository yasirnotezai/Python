import tkinter
import customtkinter as ct
from tkinter import ttk, messagebox
import os
import openpyxl

class DataEntryForm:
    def __init__(self, master):
        self.master = master
        master.title("Data Entry Form")

        self.frame = ct.CTkFrame(master)
        self.frame.pack()

        self.create_user_info_frame()
        self.create_courses_frame()
        self.create_terms_frame()
        self.create_button()

    def create_user_info_frame(self):
        self.user_info_frame = tkinter.LabelFrame(self.frame, text="User Information")
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        self.first_name_label = tkinter.Label(self.user_info_frame, text="First Name")
        self.first_name_label.grid(row=0, column=0)
        self.last_name_label = tkinter.Label(self.user_info_frame, text="Last Name")
        self.last_name_label.grid(row=0, column=1)

        self.first_name_entry = tkinter.Entry(self.user_info_frame)
        self.last_name_entry = tkinter.Entry(self.user_info_frame)
        self.first_name_entry.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)

        self.title_label = tkinter.Label(self.user_info_frame, text="Title")
        self.title_combobox = ttk.Combobox(self.user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
        self.title_label.grid(row=0, column=2)
        self.title_combobox.grid(row=1, column=2)

        self.age_label = tkinter.Label(self.user_info_frame, text="Age")
        self.age_spinbox = tkinter.Spinbox(self.user_info_frame, from_=18, to=110)
        self.age_label.grid(row=2, column=0)
        self.age_spinbox.grid(row=3, column=0)

        self.nationality_label = tkinter.Label(self.user_info_frame, text="Nationality")
        self.nationality_combobox = ttk.Combobox(self.user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
        self.nationality_label.grid(row=2, column=1)
        self.nationality_combobox.grid(row=3, column=1)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def create_courses_frame(self):
        self.courses_frame = tkinter.LabelFrame(self.frame)
        self.courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        self.registered_label = tkinter.Label(self.courses_frame, text="Registration Status")
        self.reg_status_var = tkinter.StringVar(value="Not Registered")
        self.registered_check = tkinter.Checkbutton(self.courses_frame, text="Currently Registered",
                                                    variable=self.reg_status_var, onvalue="Registered", offvalue="Not registered")
        self.registered_label.grid(row=0, column=0)
        self.registered_check.grid(row=1, column=0)

        self.numcourses_label = tkinter.Label(self.courses_frame, text= " Completed Courses")
        self.numcourses_spinbox = tkinter.Spinbox(self.courses_frame, from_=0, to='infinity')
        self.numcourses_label.grid(row=0, column=1)
        self.numcourses_spinbox.grid(row=1, column=1)

        self.numsemesters_label = tkinter.Label(self.courses_frame, text=" Semesters")
        self.numsemesters_spinbox = tkinter.Spinbox(self.courses_frame, from_=0, to="infinity")
        self.numsemesters_label.grid(row=0, column=2)
        self.numsemesters_spinbox.grid(row=1, column=2)

        for widget in self.courses_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def create_terms_frame(self):
        self.terms_frame = tkinter.LabelFrame(self.frame, text="Terms & Conditions")
        self.terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        self.accept_var = tkinter.StringVar(value="Not Accepted")
        self.terms_check = tkinter.Checkbutton(self.terms_frame, text= "I accept the terms and conditions.",
                                               variable=self.accept_var, onvalue="Accepted", offvalue="Not Accepted")
        self.terms_check.grid(row=0, column=0)

    def create_button(self):
        self.button = ct.CTkButton(self.frame, text="Enter data", command=self.enter_data)
        self.button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    def enter_data(self):
        accepted = self.accept_var.get()

        if accepted == "Accepted":
            # User info
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()

            if firstname and lastname:
                title = self.title_combobox.get()
                age = self.age_spinbox.get()
                nationality = self.nationality_combobox.get()

                # Course info
                registration_status = self.reg_status_var.get()
                numcourses = self.numcourses_spinbox.get()
                numsemesters = self.numsemesters_spinbox.get()

                print("First name: ", firstname, "Last name: ", lastname)
                print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
                print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
                print("Registration status", registration_status)
                print("------------------------------------------")

                filepath = "D:\Coding\PythonVScode\tkinter\projects\data.xlsx"

                if not os.path.exists(filepath):
                    workbook = openpyxl.Workbook()
                    sheet = workbook.active
                    heading = ["First Name", "Last Name", "Title", "Age", "Nationality",
                               "Courses", "Semesters", "Registration status"]
                    sheet.append(heading)
                    workbook.save(filepath)
                workbook = openpyxl.load_workbook(filepath)
                sheet = workbook.active
                sheet.append([firstname, lastname, title, age, nationality, numcourses,
                              numsemesters, registration_status])
                workbook.save(filepath)

            else:
                messagebox.showwarning(title="Error", message="First name and last name are required.")
        else:
            messagebox.showwarning(title= "Error", message="You have not accepted the terms")

def main():
    window = ct.CTk()
    app = DataEntryForm(window)
    window.mainloop()

if __name__ == "__main__":
    main()
