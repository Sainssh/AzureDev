import tkinter as tk
from tkinter import ttk
import cv2

root=tk.Tk()
root.geometry('400x250')
userString=tk.StringVar(root)
passString=tk.StringVar(root)

def Login():
    label_1=tk.Label(root,text="Username").place(x = 60, y =50)
    inpUser=tk.Entry(root,width=30,textvariable=userString).place(x = 130, y = 50)

    label_2=tk.Label(root,text="Password").place(x = 60, y = 90)
    inpPass=tk.Entry(root,width=30,textvariable=passString,show="*").place(x = 130, y = 90)

    Button=tk.Button(root,text="Submit",command=getValues).place(x = 170, y = 120)

def getValues():
    userVal=userString.get()
    passVal=passString.get()

    if(userVal.rstrip()=='hello' and passVal.rstrip()=='world'):
        print("Login Sucess")

        for i in root.winfo_children():
            i.destroy()
    
        main_menu()
        
    else:
        print("Failed")

clicked = tk.StringVar()
button_var = tk.StringVar()
button_var.set("Disable")

def disable_func():
    if (str(button_var.get()) == 'Disable'):
        button_var.set("Enable")
    elif (str(button_var.get()) == 'Enable'):
        button_var.set("Disable")

def genrate_dataset():
    pass

def getvall():
    print(str(clicked.get()).split(' ')[0])
    

def main_menu():    
    # clicked.set('5 mins')
    
    label_1=tk.Label(root,text="Interval", anchor=tk.W).place(x = 20, y =20)
    options = ttk.Combobox(root, textvariable = clicked)
    options['values'] = tuple(f'{i} mins' for i in range(5, 30 + 1, 5))
    options['state'] = 'readonly'
    options.place(x = 80, y = 19)

    button=tk.Button(root,text="Select",command=getvall, width=10).place(x = 80, y = 45)


    label_2=tk.Label(root,text="Add user", anchor=tk.W).place(x = 20, y = 90)
    button=tk.Button(root,text="Add",command=genrate_dataset, width=10).place(x = 80, y = 90)

    disable=tk.Label(root,text="Disable IR", anchor=tk.W).place(x = 20, y = 130)
    disable_button=tk.Button(root,command=disable_func, textvariable=button_var, width=10).place(x = 80, y = 130)

Login()
root.mainloop()