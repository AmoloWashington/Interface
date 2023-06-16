import tkinter as tk
from tkinter import messagebox

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
window = tk.Tk()
window.title("Login Page")

# Create labels and entries for username and password
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create a login button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()

# Run the application
window.mainloop()
