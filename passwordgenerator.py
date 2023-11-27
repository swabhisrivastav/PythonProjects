import secrets
import string
import tkinter as tk
from tkinter import Label, Entry, Button

special_chars = string.punctuation
digits = string.digits
letters = string.ascii_letters

selection_list = special_chars + digits + letters

def generate_password():
    password_len = length_entry.get()
    try:
        password_len = int(password_len)
        if password_len >= 12:
            password = ''
            for i in range(password_len):
                password += ''.join(secrets.choice(selection_list))

            if (any(char in special_chars for char in password) and
                    any(char in digits for char in password) and
                    any(char.upper() in letters for char in password) and
                    any(char.lower() in letters for char in password)):

                result_label.config(text=f"Generated Password: {password}")
            else:
                result_label.config(text="Generated password doesn't meet the criteria.")
        else:
            result_label.config(text="Password length is less than 12.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

window = tk.Tk()
window.title("Password Generator")

length_label = Label(window, text="Enter the length of the password (at least 12 characters):")
length_label.pack(pady=10)

length_entry = Entry(window)
length_entry.pack(pady=10)

generate_button = Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = Label(window, text="")
result_label.pack(pady=10)

window.mainloop()