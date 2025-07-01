import tkinter as tk
from tkinter  import ttk,messagebox

class SimpleLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LF")

        #frame
        self.main_frame=tk.Frame(self,relief="groove",borderwidth=10)
        self.main_frame.pack(fill="both",expand=True)

        self.create_widget()
        #self.reset_form()

    def create_widget(self):
        #Have a title of the frame
        self.title_label=tk.Label(self.main_frame,text="Login Form",font=("Arial", 20))
        self.title_label.grid(row=0,column=0,columnspan=2,pady=10)


        #Lable the widgets
        tk.Label(self.main_frame,text="username").grid(row=1,column=0,sticky="w",padx=5,pady=5)
        tk.Label(self.main_frame,text="password").grid(row=2,column=0,sticky="w",padx=5,pady=5)



        # entry field
        self.entry_username=tk.Entry(self.main_frame,width=30)
        self.entry_username.grid(row=1,column=1,pady=5)
        self.entry_password=tk.Entry(self.main_frame,width=30,show="*")
        self.entry_password.grid(row=2,column=1,pady=5)

         #button login,reset and quit
        tk.Button(self.main_frame,text="Login",command=self.show_popup).grid(row=3,column=0,pady=10)
        tk.Button(self.main_frame,text="Reset",command=self.reset_form).grid(row=3,column=1,pady=10)
        tk.Button(self.main_frame,text="Quit",command=self.destroy).grid(row=4,column=0,columnspan=1,pady=10)

    def show_popup(self):
        #get values from entry
        username=self.entry_username.get()
        password=self.entry_password.get()

        #check cridentials
        if username == "admin" and password =="1234":
            return  messagebox.showinfo("Login Successful","Welcome admin")
        else:
            messagebox.showerror("Login Failed","Invalid username or password")

            #clear the entries
    def reset_form(self):
        self.entry_username.delete(0,tk.END)
        self.entry_password.delete(0,tk.END)

if __name__ == "__main__":
    app=SimpleLogin()
    app.mainloop()