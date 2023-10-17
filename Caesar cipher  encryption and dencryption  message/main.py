import tkinter as tk  # We're import the python library for Caesar cipher  encryption and dencryption  message

# We're setting aside a spot to remember the last message we encrypted.
last_encrypted_text = "" 
# This line initializes the variable last_encrypted_text as an empty string.
# This variable will be used to store the last message that was encrypted.

# This is a special set of steps (a function) to change a message using the Caesar Cipher method.
def encrypt(text, shift):
    global last_encrypted_text  # We're telling the computer we want to use our special remembered spot.
    result = ""  # Start with an empty result.
    # For every letter or symbol in the message:
    for char in text:
        # If it's a capital letter:
        if char.isupper():
            # Change the letter by the shift amount and add to the result.
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # If it's a small letter:
        elif char.islower():
            # Change the letter by the shift amount and add to the result.
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        # If it's not a letter:
        else:
            # Just add it to the result without changing.
            result += char
    # Remember the changed message in our special spot.
    last_encrypted_text = result
    # Give back the changed message.
    return result

# This function changes the encrypted message back to the original.
def decrypt(text, shift):
    return encrypt(text, -shift)  # Use our previous function but in reverse.

# When the "Encrypt Text" button is pressed, do these steps:
def on_encrypt_button():
    # Get the message and how much to shift from the boxes.
    text = entry_text.get()
    shift = int(entry_shift.get())
    # Change the message using our encrypt function.
    encrypted_text = encrypt(text, shift)
    # Show the changed message in the window.
    result_label.config(text=f"Encrypted Text: {encrypted_text}") # 

# When the "Decrypt Text" button is pressed, do these steps:
def decrypt_last_encrypted(): # This line starts defining a function that will decrypt the previously encrypted text in Python.

    global last_encrypted_text  # Use our special remembered spot.
    shift = int(entry_shift.get())  # Get how much to shift back from the box.
    # Change the message back using our decrypt function.
    decrypted_text = decrypt(last_encrypted_text, shift) # This line of code decrypts the last_encrypted_text using a certain shift and stores the result in decrypted_text.

    # Show the original message in the window.
    result_label.config(text=f"Decrypted Text: {decrypted_text}") # It sets the text of a label in a user interface to display the decrypted version of some text.

# This part sets up the main window.
root = tk.Tk() # root = tk.Tk() creates the main window for a graphical app in Python using the tkinter library.

root.title("Caesar Cipher GUI")  # The title of the window is "Caesar Cipher GUI".

# Add pieces (widgets) to the window:
label_text = tk.Label(root, text="Enter text: ")
label_text.pack(pady=10) # In Python's GUI tool, `pady=10` adds 10 units of vertical space around an item, making it look spaced out. The number "10" tells how much space to add.

entry_text = tk.Entry(root, width=40)
entry_text.pack(pady=10) # In Python's GUI tool, `pady=10` adds 10 units of vertical space around an item, making it look spaced out. The number "10" tells how much space to add.

label_shift = tk.Label(root, text="Enter shift (number): ")
label_shift.pack(pady=10) # In Python's GUI tool, `pady=10` adds 10 units of vertical space around an item, making it look spaced out. The number "10" tells how much space to add.

entry_shift = tk.Entry(root, width=40)
entry_shift.pack(pady=10) # In Python's GUI tool, `pady=10` adds 10 units of vertical space around an item, making it look spaced out. The number "10" tells how much space to add.

# A button to change the message:
button_encrypt = tk.Button(root, text="Encrypt Text", command=on_encrypt_button) # It creates a button in a program that, when clicked, will run a function to encrypt text.

button_encrypt.pack(pady=10) # In Python's GUI tool, `pady=10` adds 10 units of vertical space around an item, making it look spaced out. The number "10" tells how much space to add.

# A button to change the message back:
button_decrypt_last = tk.Button(root, text="Decrypt Text", # button_decrypt_last = tk.Button(root, text="Decrypt Text", # 
                                command=decrypt_last_encrypted) # It's a command to decrypt (unscramble) the last thing that was encrypted (scrambled) in a program. 

button_decrypt_last.pack(pady=10) # In Python's GUI tool, `pady=10` adds 10 units of vertical space around an item, making it look spaced out. The number "10" tells how much space to add.

# A spot to show the changed or original message:
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=20) # pady=20 in Python adds 20 units of space vertically around a widget in a graphical interface. The number 10 wasn't mentioned in your question.

# This line keeps our window running until we close it.

root.mainloop() # root.mainloop() in Python keeps a window open and waits for user actions, like clicks or key presses.