import tkinter as tk
from tkinter import filedialog
from RSA import encrypt_file, decrypt_file

# Define functions for GUI
def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

def browse_key_file():
    file_path = filedialog.askopenfilename()
    key_path_entry.delete(0, tk.END)
    key_path_entry.insert(0, file_path)

def encrypt_button_click():
    file_path = file_path_entry.get()
    key_file_path = key_path_entry.get()
    encrypt_file(file_path, key_file_path)

def decrypt_button_click():
    file_path = file_path_entry.get()
    key_file_path = key_path_entry.get()
    decrypt_file(file_path, key_file_path)

# Create GUI elements
root = tk.Tk()
root.title("File Encrypt/Decrypt")

file_label = tk.Label(root, text="Select file:")
file_label.grid(row=0, column=0, padx=5, pady=5)

file_path_entry = tk.Entry(root, width=50)
file_path_entry.grid(row=0, column=1, padx=5, pady=5)

file_browse_button = tk.Button(root, text="Browse", command=browse_file)
file_browse_button.grid(row=0, column=2, padx=5, pady=5)

key_path_label = tk.Label(root, text="Enter key file path:")
key_path_label.grid(row=1, column=0, padx=5, pady=5)

key_path_entry = tk.Entry(root, width=50)
key_path_entry.grid(row=1, column=1, padx=5, pady=5)

key_browse_button = tk.Button(root, text="Browse", command=browse_key_file)
key_browse_button.grid(row=1, column=2, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_button_click)
encrypt_button.grid(row=2, column=1, padx=5, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_button_click)
decrypt_button.grid(row=2, column=2, padx=5, pady=5)

root.mainloop()