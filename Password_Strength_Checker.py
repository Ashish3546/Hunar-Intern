import string
import tkinter as tk
from tkinter import font

# Function to check password strength
def check_pwd(password):
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count +=1
        else:
            special_count +=1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "Very Bad Password!!! Change ASAP"
    elif strength == 2:
        remarks = "Not A Good Password!!! Change ASAP"
    elif strength == 3:
        remarks = "It's a weak password, consider changing"
    elif strength == 4:
        remarks = "It's a hard password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"

    return strength, remarks, lower_count, upper_count, num_count, wspace_count, special_count

# Function to check password in the GUI
def check_password():
    password = entry.get()
    strength, remarks, lower_count, upper_count, num_count, wspace_count, special_count = check_pwd(password)
    result_label.config(text=f"Password Strength: {strength}\nHint: {remarks}\n\n"
                             f"Lowercase: {lower_count}, Uppercase: {upper_count}, "
                             f"Digits: {num_count}, Whitespaces: {wspace_count}, "
                             f"Special chars: {special_count}")

# GUI-specific functions for placeholder text
def on_entry_click(event):
    if entry.get() == "Enter your password":
        entry.delete(0, tk.END)  # Remove the placeholder text
        entry.config(fg='black', show='*')  # Change text color to black and hide input

def on_focusout(event):
    if entry.get() == "":
        entry.insert(0, "Enter your password")
        entry.config(fg='gray', show='')  # Change text color to gray and show placeholder

# Create the GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x300")
root.configure(bg="#f0f0f0")

# Custom Font
custom_font = font.Font(family="Arial", size=12)

# Title Label
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Instructions Label
instructions_label = tk.Label(root, text="Enter a password to check its strength:", font=custom_font, bg="#f0f0f0")
instructions_label.pack(pady=5)

# Password Entry
entry = tk.Entry(root, width=40, font=custom_font, fg='gray')
entry.insert(0, "Enter your password")
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focusout)
entry.pack(pady=10)

# Check Button
check_button = tk.Button(root, text="Check Strength", command=check_password, font=custom_font, bg="#4CAF50", fg="white", padx=10, pady=5)
check_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=custom_font, bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()
