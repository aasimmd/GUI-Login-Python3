#import modules
 
from tkinter import *
import csv

d={}
csvfile0=open('data.csv','r', newline='')
obj0=csv.reader(csvfile0)
for row in obj0:
    if row:
        d[row[0]]=0
print(d)

#Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x350")
 
    global username
    global password
    global email
    global phone
    global dob

    global email_entry
    global phone_entry
    global dob_entry
    global username_entry
    global password_entry

    email = StringVar()
    phone = StringVar()
    dob = StringVar()
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    
    username_label = Label(register_screen, text="Username * ")
    username_label.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    
    password_label = Label(register_screen, text="Password * ")
    password_label.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    
    email_label = Label(register_screen, text="Email * ")
    email_label.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()
    
    phone_label = Label(register_screen, text="Phone number * ")
    phone_label.pack()
    phone_entry = Entry(register_screen, textvariable=phone)
    phone_entry.pack()
    
    dob_label = Label(register_screen, text="Date of birth * ")
    dob_label.pack()
    dob_entry = Entry(register_screen, textvariable=dob)
    dob_entry.pack()
    
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    email_info=email.get()
    phone_info=phone.get()
    dob_info=dob.get()

    data=(username_info, password_info, email_info, phone_info, dob_info)
    
    csvfile=open('data.csv','a', newline='')
    obj=csv.writer(csvfile)

    csvfile3=open('data.csv','r', newline='')
    obj3=csv.reader(csvfile3)
    ds0=[]
    for i in obj3:
        ds0.append(i)
    
    y=0
    if '' in data or ' ' in data:
        empty_fields()
        y=2
    else:
        for row in ds0:
            if username_info in row:
                y=1
                break;
        if(y==1):
            username_exists()
        else:
            d[username_info]=0
            obj.writerow(data)
            
    csvfile.close()
    csvfile3.close()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)
    dob_entry.delete(0, END)

    if(y==0):
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    else:
        Label(register_screen, text="Registration Failed", fg="red", font=("calibri", 11)).pack()

 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    csvfile2=open('data.csv','r', newline='')
    obj2=csv.reader(csvfile2)
    ds=[]
    for i in obj2:
        ds.append(i)
    csvfile2.close()
    
    chk=1
    for row in ds:
        if row:
            if username1 in row:
                chk=2
                if password1 in row:
                    chk=3

    if(chk==1):
        user_not_found()
    elif(chk==2):
        d[username1]+=1
        if d[username1]==3:
            d.pop(username1)
            del_user(username1)
        else:
            password_not_recognised()
    else:
        login_success()

# Designing popup for empty fields
 
def empty_fields():
    global empty_fields_screen
    empty_fields_screen = Toplevel(register_screen)
    empty_fields_screen.title("Success")
    empty_fields_screen.geometry("150x100")
    Label(empty_fields_screen, text="All fields are mandatory").pack()
    Button(empty_fields_screen, text="OK", command=delete_empty_fields).pack()

# Designing popup for existing username
 
def username_exists():
    global username_exists_screen
    username_exists_screen = Toplevel(register_screen)
    username_exists_screen.title("Success")
    username_exists_screen.geometry("150x100")
    Label(username_exists_screen, text="Username already exists").pack()
    Button(username_exists_screen, text="OK", command=delete_username_exists).pack()
 
# Designing popup for 3 tries of login attempt
 
def del_user(usr):
    msg="Deleted user '"+usr+"' for multiple login attemps with wrong password\nPress ok to go to registeration screen"

    csvfile4=open('data.csv','r', newline='')
    obj4=csv.reader(csvfile4)
    ds4=[]
    for i in obj4:
        if usr not in i:
            ds4.append(tuple(i))
    csvfile4.close()
    
    csvfile5=open('data.csv','w', newline='')
    obj5=csv.writer(csvfile5)
    for i in ds4:
        obj5.writerow(i)
    
    global del_user_screen
    del_user_screen = Toplevel(login_screen)
    del_user_screen.title("Success")
    del_user_screen.geometry("400x100")
    Label(del_user_screen, text=msg).pack()
    Button(del_user_screen, text="OK", command=delete_del_user).pack()
 
# Designing popup for login success
 
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups

def delete_del_user():
    del_user_screen.destroy()
    login_screen.destroy()
    register()
    
def delete_empty_fields():
    empty_fields_screen.destroy()
    
def delete_username_exists():
    username_exists_screen.destroy()
    
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x200")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
