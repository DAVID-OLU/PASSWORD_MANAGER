from tkinter import *
from tkinter import messagebox
from update_password import update_password
from delete_password import delete_password
from save_credential import save_credential
from create_pass import create_pass
from find_credentials import find_credentials
import json


window = Tk()
window.title("Password Manager")
window.config(padx=45, pady=45)

canvas = Canvas(height=350, width=300)
my_image = PhotoImage(file="lock.png")
logo_image = my_image.subsample(2, 2)
canvas.create_image(150, 150, image=logo_image)
canvas.grid(row=0, column=1)

# Created my labels
website_name_label = Label(text="Website Name:")
website_name_label.grid(row=1, column=0)

email_label = Label(text="Username/Email:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Creating my Entries
website_name_entry = Entry(width=33)
website_name_entry.grid(row=1, column=1)
website_name_entry.focus()

email_info = Entry(width=33)
email_info.grid(row=2, column=1)

password_data = Entry(width=33)
password_data.grid(row=3, column=1)

# Creating Buttons
find_button = Button(text="Find", width=11, command=lambda: find_credentials(website_name_entry))
find_button.grid(row=1, column=2)
create_password = Button(text="Create Password", command=lambda: create_pass(password_data))
create_password.grid(row=3, column=2)

add_credentials = Button(window, text="Add Now", width=46, command=lambda: save_credential(website_name_entry, email_info, password_data))
add_credentials.grid(row=4, column=1, columnspan=2)

# -----------------
update_button = Button(text="Update", width=11,
                       command=lambda: update_password(website_name_entry.get(), email_info.get(),
                                                       password_data.get(), website_name_entry, email_info,
                                                       password_data))
update_button.grid(row=2, column=2)

# ---------------------
delete_button = Button(text='Delete', width=46, command=lambda: delete_password(website_name_entry.get(),
                                                                                website_name_entry))
delete_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
