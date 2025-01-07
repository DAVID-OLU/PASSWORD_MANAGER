from tkinter import messagebox
import json


def find_credentials(website_name_entry):
    website_name = website_name_entry.get().lower()

    # This if block regulates that the user input a website name in other to find credentials.
    if not website_name:
        messagebox.showinfo(title="Error", message="Enter a website name to find credential")
        return
    try:
        with open("info.json") as credential_file:
            info = json.load(credential_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website_name in info:
            email = info[website_name]["email"]
            password = info[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No data for {website_name} exists.")
