import tkinter as tk
from tkinter import filedialog, messagebox
import os
from encryption_tool import generate_key, load_key, encrypt_file, decrypt_file

if not os.path.exists("secret.key"):
    generate_key()

key = load_key()

def select_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def encrypt_action():
    filepath = file_entry.get()
    if filepath:
        try:
            encrypt_file(filepath, key)
            messagebox.showinfo("Success", "File encrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {e}")

def decrypt_action():
    filepath = file_entry.get()
    if filepath:
        try:
            decrypt_file(filepath, key)
            messagebox.showinfo("Success", "File decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {e}")

root = tk.Tk()
root.title("🔐 Advanced Encryption Tool")

tk.Label(root, text="Select File:").pack(pady=5)
file_entry = tk.Entry(root, width=40)
file_entry.pack(padx=10)
tk.Button(root, text="Browse", command=select_file).pack(pady=5)

tk.Button(root, text="Encrypt File", bg="#90ee90", command=encrypt_action).pack(pady=5)
tk.Button(root, text="Decrypt File", bg="#ffcccb", command=decrypt_action).pack(pady=5)

root.mainloop()
