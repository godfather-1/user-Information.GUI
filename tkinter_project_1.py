#import tkinter
#from tkinter import *
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
root =tk.Tk()
root.title('GUI')

#create lable
name_label = ttk.Label(root, text='Enter your name :')
name_label.grid(row=0, column=0 , sticky=tk.W)

email_label = ttk.Label(root ,text='Enter your email :' )
email_label.grid(row=2 , column=0 , sticky=tk.W)

age_label = ttk.Label(root ,text='Enter your age :' )
age_label.grid(row=4, column=0 , sticky=tk.W)

gender_label = ttk.Label(root , text ='Select your gender :')
gender_label.grid(row=6 , column=0 , sticky=tk.W)

#create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(root , width=16 , textvariable = name_var)
name_entrybox.grid(row=0 , column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(root , width=16 , textvariable = email_var)
email_entrybox.grid(row=2 , column=1)



age_var = tk.StringVar()
age_entrybox = ttk.Entry(root , width=16 , textvariable = age_var)
age_entrybox.grid(row=4 , column=1)


#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root , width=13 , textvariable=gender_var, state ='readonly')
gender_combobox['value'] = ('Male' , 'Female' , 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=6 , column=1)

#radio button 
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(root , text='Student' , value='Student' , variable=usertype)
radiobtn1.grid(row=8 , column=0)
radiobtn2 = ttk.Radiobutton(root , text='Teacher' , value='Teacher' , variable=usertype)
radiobtn2.grid(row=8 , column=1)
#create button 

#check button 
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(root , text ='Check if you fill all the blanks' , variable=checkbtn_var)
checkbtn.grid(row=10 , columnspan=3)

def action():
    user_name = name_var.get()
    user_age = age_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        subscribed = 'NO'
    else:
        subscribed = 'YES'

    #write to csv file
    with open('file.csv' , 'a' ) as f:
        dict_wirter = DictWriter(f , fieldnames= ['Name' , 'Age' , 'Email Address' , 'Gender' , 'User Type' , 'Subcribed'])
        if os.stat('file.csv').st_size==0:
            dict_wirter.writeheader()
        dict_wirter.writerow({
            'Name': user_name,
            'Age' : user_age,
            'Email Address' : user_email,
            'Gender' : user_gender,
            'User Type' : user_type,
            'Subcribed' : subscribed
        })


    name_entrybox.delete(0 , tk.END)
    age_entrybox.delete(0 , tk.END)
    email_entrybox.delete(0 , tk.END)
    name_label.configure(foreground='blue')
    #submit_button.configure(foreground='blue')



submit_button = ttk.Button(root , text = 'Submit' , command=action)
submit_button.grid(row=20 , column=0)



root.mainloop()
