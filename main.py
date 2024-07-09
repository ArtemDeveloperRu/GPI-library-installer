from tkinter import*
import os
from tkinter import messagebox
import webbrowser

def install_library():
    library_name = libory.get()
    if not library_name:
        messagebox.showerror("Error", "Please enter a library name.")
        return
    try:
        os.system(f"pip install {library_name}")
        messagebox.showinfo("Success", f"Library '{library_name}' installed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to install library '{library_name}'.\n{str(e)}")

def uninstall_library():
    library_name = libory.get()
    if not library_name:
        messagebox.showerror("Error", "Please enter a library name.")
        return
    try:
        os.system(f"pip uninstall {library_name}")
        messagebox.showinfo("Success", f"Library '{library_name}' uninstalled successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to uninstall library '{library_name}'.\n{str(e)}")

def lists_libory():
    os.system(f"pip list")
    messagebox.showinfo("Success", "Library lists displayed.")

def reference():
    webbrowser.open("https://github.com/ArtemDeveloperRu/install-libory-GPU/blob/main/README.md", new=2)

windows = Tk()
windows.geometry("250x250")
windows.title("Library installer from Python")

canvas = Canvas(windows, width=250, height=250)
label = Label(windows, text="Enter library name:")
libory = Entry()

button_install = Button(windows, text="Install", command=install_library) 
button_uninstall = Button(windows, text="Uninstall", command=uninstall_library)
button_list_libory = Button(windows, text="Library lists", command=lists_libory)
button_referencebtn = Button(windows, text="Reference", command=reference)

canvas.pack()
label.place(relx=0.5, rely=0.1, anchor=CENTER)
libory.place(relx=0.5, rely=0.19, anchor=CENTER) 
button_install.place(relx=0.5, rely=0.3, anchor=CENTER)
button_list_libory.place(relx=0.5, rely=0.4, anchor=CENTER)
button_uninstall.place(relx=0.5, rely=0.5, anchor=CENTER)
button_referencebtn.place(relx=0.5, rely=0.6, anchor=CENTER)

windows.bind("<F1>", lambda event: reference())

windows.resizable(False, False)
windows.mainloop()