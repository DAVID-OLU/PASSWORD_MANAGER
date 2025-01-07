from tkinter import *
from tkinter import messagebox
import json


def update_password(website_name, new_email, new_password, website_name_entry, email_info, password_data):
    website_name = website_name_entry.get().lower()
    new_email = email_info.get().lower()

    ####

    # Making sure no fields are empty
    if not new_email or not new_password:
        messagebox.showinfo(title="Error", message="Cant leave any field empty")
        return

    try:
        with open("info.json", "r") as credential_file:
            info = json.load(credential_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
        return

    if website_name in info:
        confirm = messagebox.askyesno(title="Confirm Update",
                                      message=f"You already have data for {website_name}. DO you want to update?")

        if confirm:
            info[website_name]["email"] = new_email
            info[website_name]["password"] = new_password

            with open("info.json", "w") as credential_file:
                json.dump(info, credential_file, indent=4)

            messagebox.showinfo(title="Success", message="Password updated successfully")

            # Clear the input fields after successful edit
            website_name_entry.delete(0, END)
            email_info.delete(0, END)
            password_data.delete(0, END)

        else:
            messagebox.showinfo(title="Cancelled", message="Update Cancelled")
    else:
        messagebox.showinfo(title="Error", message="Website not found.")
