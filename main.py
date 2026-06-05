import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

def organize_files(directory):
    # Categories defined in English
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Scripts': ['.py', '.js', '.html']
    }
    
    count = 0
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()
                for category, extensions in file_types.items():
                    if file_ext in extensions:
                        folder_path = os.path.join(directory, category)
                        os.makedirs(folder_path, exist_ok=True)
                        shutil.move(file_path, os.path.join(folder_path, filename))
                        count += 1
        
        messagebox.showinfo("Success", f"Successfully organized {count} files!")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_files(folder_selected)

# UI setup in English
root = tk.Tk()
root.title("File Organizer Tool")
root.geometry("300x150")

label = tk.Label(root, text="Organize your files with one click", pady=20)
label.pack()

btn = tk.Button(root, text="Select Folder and Start", command=browse_folder, bg="#2ecc71", fg="white", padx=10)
btn.pack()

root.mainloop()