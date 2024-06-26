import customtkinter as ctk
import ttkbootstrap as ttk
import tkinter
import jinja2
import pdfkit

ctk.set_appearance_mode("Dark")


class CvGenerator():
    def __init__(self, root):
        self.root = root
        self.root.title("CvGenerator")
        self.frame = ttk.Frame(root, bootstyle="dark")
        self.frame.pack()

        self.personalLabelFrame()
        self.workExperienceLabelFrame()
        self.skills()
        self.getting_all_values()
        self.button()

    def personalLabelFrame(self):
        # LabelFrame 
        self.personal_frame = ttk.LabelFrame(self.frame, text="Personal Details", bootstyle='primary')
        self.personal_frame.grid(row=0, column=0, padx=10, pady=10)
        # 1 label
        self.name_label = ttk.Label(self.personal_frame, text="Name", bootstyle='primary')
        self.name_label.grid(row=0, column=0)
        # 1  text
        self.name_text = ttk.Entry(self.personal_frame, bootstyle='primary')
        self.name_text.grid(row=0, column=1)
        # 2 label
        self.profession_label = ttk.Label(self.personal_frame, text="Profession", bootstyle='primary')
        self.profession_label.grid(row=0, column=3)
        # 2 text 
        self.profession_entry = ttk.Entry(self.personal_frame, bootstyle='primary')
        self.profession_entry.grid(row=0, column=4)
        # 3 label
        self.email_label = ttk.Label(self.personal_frame, text="Email",bootstyle='primary')
        self.email_label.grid(row=0, column=5)
        # 3 text 
        self.email_entry = ttk.Entry(self.personal_frame, bootstyle='primary')
        self.email_entry.grid(row=0, column=6)
        # 4 label
        self.phone_label = ttk.Label(self.personal_frame, text="Phone", bootstyle='primary')
        self.phone_label.grid(row=1, column=0)
        # 4 text 
        self.phone_entry = ttk.Entry(self.personal_frame, bootstyle='primary')
        self.phone_entry.grid(row=1, column=1)
        # 5 label
        self.social_label = ttk.Label(self.personal_frame, text="Social", bootstyle='primary')
        self.social_label.grid(row=1, column=2)
        # 5 text 
        self.social_entry = ttk.Entry(self.personal_frame, bootstyle='primary')
        self.social_entry.grid(row=1, column=3)
        # 6 label
        self.professionSummary_label = ttk.Label(self.personal_frame,  text="Profession Summary", bootstyle='primary')
        self.professionSummary_label.grid(row=2, column=0)
        # 6 text 
        self.professionSummary_entry = ttk.Entry(self.personal_frame, bootstyle='primary')
        self.professionSummary_entry.grid(row=2, column=1)
         # 7 label
        self.education_label = ttk.Label(self.personal_frame, text="Education", bootstyle='primary')
        self.education_label.grid(row=3, column=0)
        # 7 text 
        self.education_entry = ttk.Entry(self.personal_frame,   bootstyle='primary')
        self.education_entry.grid(row=3, column=1, sticky="w")
        
        for i in self.personal_frame.winfo_children():
            i.grid_configure(padx=7, pady=7)
            
    def workExperienceLabelFrame(self):
        # LabelFrame
        self.workLabelFrame = ttk.LabelFrame(self.frame, text="Work Experience", width=60, bootstyle="primary")
        self.workLabelFrame.grid(row=2, column=0, padx=20, pady=10) 
         # 1 label
        self.work1_label = ttk.Label(self.workLabelFrame, text="1st Work", bootstyle="primary")
        self.work1_label.grid(row=0, column=0)
        # 1 text 
        self.work1_entry = ttk.Entry(self.workLabelFrame,  bootstyle="primary")
        self.work1_entry.grid(row=0, column=1)
         # 2 label
        self.work1_companyD_label = ttk.Label(self.workLabelFrame, text="1st Work Company and Data", bootstyle="primary")
        self.work1_companyD_label.grid(row=0, column=2)
        # 2 text 
        self.work1_companyD_entry = ttk.Entry(self.workLabelFrame,  bootstyle="primary")
        self.work1_companyD_entry.grid(row=0, column=3)
        # 3 label
        self.work1_other_label1 = ttk.Label(self.workLabelFrame, text="Others Details", bootstyle="primary")
        self.work1_other_label1.grid(row=1, column=0)
        # 3 text 
        self.work1_other_entry1 = ttk.Entry(self.workLabelFrame,  background="Silver")
        self.work1_other_entry1.grid(row=1, column=1)
        # 4 label
        self.work1_other_label2 = ttk.Label(self.workLabelFrame, text="Others Details", bootstyle="primary")
        self.work1_other_label2.grid(row=1, column=2)
        # 4 text 
        self.work1_other_entry2 = ttk.Entry(self.workLabelFrame,  background="Silver")
        self.work1_other_entry2.grid(row=1, column=3)
        # 5 label
        self.work1_other_label3 = ttk.Label(self.workLabelFrame, text="Others Details", bootstyle="primary")
        self.work1_other_label3.grid(row=1, column=4)
        # 5 text
        self.work1_other_entry3 = ttk.Entry(self.workLabelFrame,  bootstyle="primary")
        self.work1_other_entry3.grid(row=1, column=5)
        # 6 label
        self.work2_label = ttk.Label(self.workLabelFrame, text="2nd Work", bootstyle="primary")
        self.work2_label.grid(row=2, column=0)
        # 6 text 
        self.work2_entry = ttk.Entry(self.workLabelFrame,  bootstyle="primary")
        self.work2_entry.grid(row=2, column=1)
         # 7 label
        self.work2_companyD_label = ttk.Label(self.workLabelFrame, text="2nd Work Company and Data", bootstyle="primary")
        self.work2_companyD_label.grid(row=2, column=2)
        # 7 text 
        self.work2_companyD_entry = ttk.Entry(self.workLabelFrame,  bootstyle="primary")
        self.work2_companyD_entry.grid(row=2, column=3)
        # 8 label
        self.work2_other_label1 = ttk.Label(self.workLabelFrame, text="Others Details",bootstyle="primary")
        self.work2_other_label1.grid(row=3, column=0)
        # 8 text 
        self.work2_other_entry1 = ttk.Entry(self.workLabelFrame,  bootstyle="primary")
        self.work2_other_entry1.grid(row=3, column=1)
        # 9 label
        self.work2_other_label2 = ttk.Label(self.workLabelFrame, text="Others Details", bootstyle="primary")
        self.work2_other_label2.grid(row=3, column=2)
        # 9 text 
        self.work2_other_entry2 = ttk.Entry(self.workLabelFrame,  bootstyle="primary")
        self.work2_other_entry2.grid(row=3, column=3)
        # 10 label
        self.work2_other_label3 = ttk.Label(self.workLabelFrame, text="Others Details", bootstyle="primary")
        self.work2_other_label3.grid(row=3, column=4)
        # 10 text 
        self.work2_other_entry3 = ttk.Entry(self.workLabelFrame,  bootstyle="primary")
        self.work2_other_entry3.grid(row=3, column=5)
        for i in self.workLabelFrame.winfo_children():
            i.grid_configure(padx=7, pady=7)

    def skills(self):
        # Labelframe
        self.skillsLabelFrame = ttk.LabelFrame(self.frame, text="Skills", bootstyle='primary')
        self.skillsLabelFrame.grid(row=3, column=0, padx=20, pady=10)
        # 1 label
        self.skill1_label = ttk.Label(self.skillsLabelFrame, text="●", bootstyle='primary')
        self.skill1_label.grid(row=0, column=0)
        # 1 Text 
        self.skill1_entry = ttk.Entry(self.skillsLabelFrame, bootstyle='primary')
        self.skill1_entry.grid(row=0, column=1)
        # 2 label
        self.skill2_label = ttk.Label(self.skillsLabelFrame, text="●", bootstyle='primary')
        self.skill2_label.grid(row=0, column=2)
        # 2 Text 
        self.skill2_entry = ttk.Entry(self.skillsLabelFrame, bootstyle='primary')
        self.skill2_entry.grid(row=0, column=3)
        # 3 label
        self.skill3_label = ttk.Label(self.skillsLabelFrame, text="●", bootstyle='primary')
        self.skill3_label.grid(row=0, column=4)
        # 3 Text 
        self.skill3_entry = ttk.Entry(self.skillsLabelFrame, bootstyle='primary')
        self.skill3_entry.grid(row=0, column=5)
        for i in self.skillsLabelFrame.winfo_children():
            i.grid_configure(padx=7, pady=7)
    
    def click_function(self):
        self.getting_all_values()
        self.allContents = {
            "name": self.name,
            "profession": self.profession,
            "email": self.email,
            "phone": self.phone,
            "social": self.social,
            "summary": self.summary,
            "education": self.education,
            "work1": self.work1,
            "company_and_date1": self.company_and_date1,
            "work1_detail_1": self.work1_detail_1,
            "work1_detail_2": self.work1_detail_2,
            "work1_detail_3": self.work1_detail_3,
            "work2": self.work2, 
            "company_and_date2": self.company_and_date2,
            "work2_detail_1": self.work2_detail_1,
            "work2_detail_2": self.work2_detail_2,
            "work2_detail_3": self.work2_detail_3, 
            "skill_1": self.skill1,
            "skill_2": self.skill2,
            "skill_3": self.skill3
        }

        self.template_loader = jinja2.FileSystemLoader(searchpath='D:\\Coding\\PythonVScode\\PythonGUI\\tkinter')
        self.template_env = jinja2.Environment(loader=self.template_loader)

        self.html_template = "cv.html"
        self.template = self.template_env.get_template(self.html_template)
        self.output_text = self.template.render(self.allContents)

        self.config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
        self.output_pdf = "pdf_generated.pdf"
        pdfkit.from_string(self.output_text, self.output_pdf, configuration=self.config,
                           css="D:\\Coding\\PythonVScode\\PythonGUI\\tkinter\\cv.css")

    def getting_all_values(self):
          # personal
          self.name = self.name_text.get()
          self.profession = self.profession_entry.get()
          self.email = self.email_entry.get()
          self.phone = self.phone_entry.get()
          self.social = self.social_entry.get()
          # education
          self.summary = self.professionSummary_entry.get()
          self.education = self.education_entry.get()
          # work 1
          self.work1 = self.work1_entry.get()
          self.company_and_date1 = self.work1_companyD_entry.get()
          self.work1_detail_1 = self.work1_other_entry1.get()
          self.work1_detail_2 = self.work1_other_entry2.get()
          self.work1_detail_3 = self.work1_other_entry3.get()
          # work 2
          self.work2 = self.work2_entry.get()
          self.company_and_date2 = self.work2_companyD_entry.get()
          self.work2_detail_1 = self.work2_other_entry1.get()
          self.work2_detail_2 = self.work2_other_entry2.get()
          self.work2_detail_3 = self.work2_other_entry3.get()
          # skills
          self.skill1 = self.skill1_entry.get()
          self.skill2 = self.skill2_entry.get()
          self.skill3 = self.skill3_entry.get()
    
    def button(self):
        self.button = ttk.Button(self.frame, text="Submit and Download", command=self.click_function, bootstyle="primary, outline")
        self.button.grid(row=4, column=0, padx=7, pady=7)


def main():
    window = ctk.CTk()
    app = CvGenerator(window)
    window.mainloop()


if __name__ == "__main__":
    main()
