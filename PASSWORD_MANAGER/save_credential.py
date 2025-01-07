from tkinter import *
from tkinter import messagebox
import json


def save_credential(website_name_entry, email_info, password_data):
    website_name = website_name_entry.get().lower()
    email = email_info.get().lower()
    password = password_data.get()

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oh oh", message="Please do not leave any fields empty.")
        return

    new_info = {
        website_name: {
            "email": email,
            "password": password
        }
    }

    try:

        with open("info.json", "r") as credential_file:
            info = json.load(credential_file)

    except FileNotFoundError:

        with open("info.json", "w") as credential_file:
            json.dump(new_info, credential_file, indent=4)
        messagebox.showinfo(title="Success", message="Credentials saved successfully.")
        website_name_entry.delete(0, END)
        email_info.delete(0, END)
        password_data.delete(0, END)
        return

    # here I am checking if the website already exists in the loaded data
    if website_name in info:
        messagebox.showinfo(title="Error",
                            message=f"Saved details already exist for {website_name}. Use the update button "
                                    "to update your credentials.")
        return

    confirm = messagebox.askyesno(title="Confirm Save",
                                  message=f"Is this okay?\n\nWebsite: "
                                          f"{website_name}\nEmail: {email}\nPassword: {password}")
    if confirm:
        info.update(new_info)

        with open("info.json", "w") as credential_file:
            json.dump(info, credential_file, indent=4)

        # input fields is being clear
        website_name_entry.delete(0, END)
        email_info.delete(0, END)
        password_data.delete(0, END)
        messagebox.showinfo(title="Success", message="Credentials saved successfully.")
