

import tkinter as tk
from tkinter import ttk,messagebox


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('My App')

        #Create frame
        self.main_frame=tk.Frame(self,relief='groove',borderwidth=5)
        self.main_frame.pack(fill="both",expand=True)

        #call function to add widgets
        self.create_widgets()
        # set form to initial state
        self.reset_form()

    def create_widgets(self):
        self.title_lable=tk.Label(self.main_frame,text="Data entry",font=("Arial",14))
        self.title_lable.grid(column=0,row=0,columnspan=3,pady=2)

            #Add all label
        tk.Label(self.main_frame,text="Full Name",).grid(row=1,column=0,sticky="w",padx=5)
        tk.Label(self.main_frame,text="Residency",).grid(row=2,column=0,sticky="w",padx=5)
        tk.Label(self.main_frame,text="Program",).grid(row=3,column=0,sticky="w",padx=5)
        tk.Label(self.main_frame,text="Courses",).grid(row=4,column=0,sticky="w",padx=5)

            #Entry for full name
        self.name_entry=tk.Entry(self.main_frame,width=30)
        self.name_entry.grid(row=1,column=1,pady=5)

            #Radio Button for residency
        self.residency_var=tk.StringVar(value="dom")
        tk.Radiobutton(self.main_frame,text="Domestic",variable=self.residency_var,value="dom").grid(column=1,row=2)
        tk.Radiobutton(self.main_frame,text="International",variable=self.residency_var,value="Intl").grid(column=2,row=2)

            #Combobox for program
        self.program_var=tk.StringVar()
        self.program_combobox=ttk.Combobox(self.main_frame,textvariable=self.program_var,state="readonly")
        self.program_combobox["values"] =["AI","Gaming","software","Health"]
        self.program_combobox.grid(column=1,row=3,pady=5,columnspan=2)

            #checkbox for courses
        self.course_var = {
            "Python":tk.StringVar(value=""),
            "C#":tk.StringVar(value=""),
            "Web Dev":tk.StringVar(value="")
        }
        tk.Checkbutton(self.main_frame,text="python",variable=self.course_var["Python"],onvalue="COMP100",offvalue="").grid(column=1,row=4,sticky="w")
        tk.Checkbutton(self.main_frame,text="c#",variable=self.course_var["C#"],onvalue="COMP101",offvalue="").grid(column=1,row=5,sticky="w")
        tk.Checkbutton(self.main_frame,text="Web dev",variable=self.course_var["Web Dev"],onvalue="COMP102",offvalue="").grid(column=1,row=6,sticky="w")

            #button
        tk.Button(self.main_frame,text="Reset",command=self.reset_form).grid(row=7,column=0,pady=10)
        tk.Button(self.main_frame,text="ok",command=self.show_popup).grid(row=7,column=1,pady=10)
        tk.Button(self.main_frame,text="exit",command=self.destroy).grid(row=7,column=2,pady=10)


    def reset_form(self):
        self.name_entry.delete(0,tk.END)
        self.name_entry.insert(0,"Jo Kin")
        self.residency_var.set("dom")
        self.program_combobox.set("AI")
        for var in self.course_var.values():
            var.set("")

    def show_popup(self):
        fullname=self.name_entry.get()
        residency= "Domestic" if self.residency_var.get() == "dom" else "International"
        program= self.program_var.get()
        courses=[key for key , var in self.course_var.items() if var.get()]

        courses_str= ",".join(courses) if courses else "None"

        messagebox.showinfo("Form Data",f"Full Name{fullname}\nresidency: {residency}\nprogram: {program}\ncourse: {courses_str}")

if __name__ == "__main__":
    app=MyApp()
    app.mainloop()




