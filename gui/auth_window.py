import customtkinter as ctk


class AuthWindow(ctk.CTkToplevel):
    def __init__(self, master, on_success):
        super().__init__(master)
        self.title("Authentication Required")
        self.geometry("300x200")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.on_success = on_success

        self.password_var = ctk.StringVar()

        self.label = ctk.CTkLabel(self, text="Enter Parent Password:", font=("Arial", 14, "bold"))
        self.label.pack(pady=(30, 10))

        self.password_entry = ctk.CTkEntry(self, textvariable=self.password_var, show="*")
        self.password_entry.pack(pady=10)

        self.submit_btn = ctk.CTkButton(self, text="Submit", command=self.verify_password)
        self.submit_btn.pack(pady=10)

        self.error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.error_label.pack()

    def verify_password(self):
        if self.password_var.get() == "admin123":
            self.on_success()
            self.destroy()
        else:
            self.error_label.configure(text="Incorrect Password")
