from tkinter import *
from tkinter import messagebox
from database import connection

def check_username(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT username FROM users
                WHERE username=%s''',(username,))
    data=cur.fetchone()
    con.close()
    if data:
        return True
    return False

def create_account(username,password,confirm
                   ,limit,work,movie,goal,goal_amount):
    if username=="" or password=="" or confirm=="" or limit=="" or work=="" or movie=="" or goal=="" or goal_amount=="":
        messagebox.showerror("Error","Fill All Fields")
        return False
    if check_username(username):
        messagebox.showerror("Error",
                             "Username Already Exists")
        return False
    if password!=confirm:
        messagebox.showerror("Error",
                             "Passwords Do Not Match")
        return False
    try:
        limit=float(limit)
        goal_amount=float(goal_amount)
    except:
        messagebox.showerror("Error","Enter Valid Amount")
        return False
    con=connection()
    cur=con.cursor()
    cur.execute('''INSERT INTO users(username,password,
                financial_limit,working_as,
                fav_movie,goal_name,goal_amount)
    VALUES(%s,%s,%s,%s,%s,%s,%s)''',(username,password,
    limit,work,movie,goal,goal_amount))
    con.commit()
    con.close()
    messagebox.showinfo("Success",
                        "Account Created Successfully")
    return True

def login(username,password):
    if username=="" or password=="":
        messagebox.showerror("Error",
                             "Enter Username And Password")
        return None
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT username FROM users
                WHERE username=%s AND password=%s''',
                (username,password))
    data=cur.fetchone()
    con.close()
    if data:
        return username
    messagebox.showerror("Error",
                         "Wrong Username Or Password")
    return None

def forgot_password(username,movie):
    if username=="" or movie=="":
        messagebox.showerror("Error","Fill All Fields")
        return
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT fav_movie,password
                FROM users WHERE username=%s''',(username,))
    data=cur.fetchone()
    con.close()
    if data==None:
        messagebox.showerror("Error","Username Not Found")
        return
    if movie.strip().lower()==data[0].strip().lower():
        messagebox.showinfo("Password","Your Password Is : "+data[1])
    else:
        messagebox.showerror("Error","Incorrect Favourite Movie")

def change_password(username,old_password,
                    new_password,confirm_password):
    if old_password=="" or new_password=="" or confirm_password=="":
        messagebox.showerror("Error","Fill All Fields")
        return False
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT password FROM users
                WHERE username=%s''',(username,))
    data=cur.fetchone()
    if data==None:
        con.close()
        messagebox.showerror("Error","User Not Found")
        return False
    if data[0]!=old_password:
        con.close()
        messagebox.showerror("Error",
                             "Old Password Incorrect")
        return False
    if new_password!=confirm_password:
        con.close()
        messagebox.showerror("Error",
                             "Passwords Do Not Match")
        return False
    cur.execute('''UPDATE users SET password=%s
                WHERE username=%s''',
                (new_password,username))
    con.commit()
    con.close()
    messagebox.showinfo("Success",
                        "Password Changed Successfully")
    return True
def get_user_details(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT financial_limit,goal_name,
                goal_amount FROM users
                WHERE username=%s''',(username,))
    data=cur.fetchone()
    con.close()
    return data

def get_financial_limit(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT financial_limit FROM
                users WHERE username=%s''',(username,))
    data=cur.fetchone()[0]
    con.close()
    return data
