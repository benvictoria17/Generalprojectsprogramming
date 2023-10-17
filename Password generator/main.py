# password generator python library
import tkinter as tk
import random
import string

def generate_password():
    # get the password length from the length_entry input field
    # and convert it to an int
    password_length = int(length_entry.get())

    # characters is one big string of letters + digits + punctuation
    # each password character must be chosen from these characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate the password by doing password_length loops
    # and in each loop get a random choice from characters
    password = ""
    for i in range(password_length):
        password += random.choice(characters)

    result_label.config(text=password)  # put the password in the result_label

# The gui for the password generator with tkinter
window = tk.Tk()  # create the main GUI window
window.title("Password Generator")  # set the title of the GUI window

# create label to show instructions to the user
instructions_label = tk.Label(
    window,
    text="Enter the password length (1 to 12):")
instructions_label.pack()  # add the instructions label to the GUI


length_entry = tk.Entry(window)  # create the entry field for the password length
length_entry.pack() # add the entry field to the GUI


# create a button to generate the password
generate_button = tk.Button(
    window, text="Generate Password", 
    command=generate_password)
generate_button.pack() # add the button to the GUI


result_label = tk.Label(window, text="") # label that holds the generated password
result_label.pack()  # add the label to the GUI

window.mainloop() # start the GUI