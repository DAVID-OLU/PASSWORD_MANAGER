from tkinter import *
from tkinter import messagebox
import json


def delete_password(website_name, website_name_entry):
    website_name = website_name_entry.get().lower()
    # Make sure website field is not empty
    if not website_name:
        messagebox.showinfo(title="Error", message="Cant leave any field empty. Please enter your website name")
        return

    try:
        with open("info.json", "r") as credential_file:
            info = json.load(credential_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
        return

    if website_name in info:
        confirm = messagebox.askyesno(title="Confirm Delete",
                                      message=f"Are you sure you want to delete the credentials "
                                              f"for {website_name}?")
        if confirm:
            # Removing entry for that website name
            del info[website_name]

            with open("info.json", "w") as credential_file:
                json.dump(info, credential_file, indent=4)

            messagebox.showinfo(title="Success", message="Successfully deleted credentials.")

            website_name_entry.delete(0, END)
        else:
            messagebox.showinfo(title="Cancelled", message="Deleting process cancelled.")
    else:
        messagebox.showinfo(title="Error", message="Cant find website name.")