import tkinter as tk
from tkinter import ttk,messagebox
from database import create_database
from account import *
from transaction import *
from reports import *
current_user=""

main_font=("Book Antiqua",12,"bold italic")
title_font=("Book Antiqua",22,"bold italic")
menu_font=("Book Antiqua",13,"bold italic")

root=tk.Tk()
root.title("Household Finance Manager")
root.geometry("1200x700")
root.state("zoomed")
root.configure(bg="#EAF6F6")
root.resizable(True,True)

title=tk.Label(root,text="HOUSEHOLD FINANCE MANAGER",
               font=title_font,bg="#EAF6F6",fg="darkblue")
title.pack(pady=10)

main_frame=tk.Frame(root,bg="#EAF6F6")
main_frame.pack(fill="both",expand=True,
                padx=10,pady=10)

main_frame.grid_rowconfigure(0,weight=1)
main_frame.grid_columnconfigure(0,weight=3)
main_frame.grid_columnconfigure(1,weight=1)

content_frame=tk.Frame(main_frame,bg="#EAF6F6",
                       bd=2,relief="groove")
content_frame.grid(row=0,column=0,sticky="nsew",
                   padx=10)

menu_frame=tk.Frame(main_frame,bg="#EAF6F6",
                    bd=2,relief="groove")
menu_frame.grid(row=0,column=1,sticky="nsew",
                padx=10)

# LOGIN

login_frame=tk.LabelFrame(content_frame,text="LOGIN",
                          font=menu_font,bg="#EAF6F6")
login_frame.pack(fill="x",padx=20,pady=10)

tk.Label(login_frame,text="Username",font=main_font,
         bg="#EAF6F6").grid(row=0,column=0,padx=10,pady=8)

username_entry=tk.Entry(login_frame,width=35,font=main_font)
username_entry.grid(row=0,column=1,padx=10)

tk.Label(login_frame,text="Password",font=main_font,
         bg="#EAF6F6").grid(row=1,column=0,padx=10,pady=8)

password_entry=tk.Entry(login_frame,width=35,
                        show="*",font=main_font)
password_entry.grid(row=1,column=1,padx=10)

# DASHBOARD

dashboard_frame=tk.LabelFrame(content_frame,
                              text="DASHBOARD",font=menu_font,
                              bg="#EAF6F6")
dashboard_frame.pack(fill="x",padx=20,pady=10)

welcome_var=tk.StringVar(value="Welcome :")
limit_var=tk.StringVar(value="Financial Limit :")
balance_var=tk.StringVar(value="Remaining Balance :")
goal_var=tk.StringVar(value="Savings Goal :")
progress_var=tk.StringVar(value="Goal Progress :")

tk.Label(dashboard_frame,textvariable=welcome_var,
         font=main_font,bg="#EAF6F6").grid(row=0,
                                           column=0,sticky="w",padx=10,pady=5)
tk.Label(dashboard_frame,textvariable=limit_var,
         font=main_font,bg="#EAF6F6").grid(row=1,
                                           column=0,sticky="w",padx=10,pady=5)
tk.Label(dashboard_frame,textvariable=balance_var,
         font=main_font,bg="#EAF6F6").grid(row=2,
                                           column=0,sticky="w",padx=10,pady=5)
tk.Label(dashboard_frame,textvariable=goal_var,
         font=main_font,bg="#EAF6F6").grid(row=3,
                                           column=0,sticky="w",padx=10,pady=5)
tk.Label(dashboard_frame,textvariable=progress_var,
         font=main_font,bg="#EAF6F6").grid(row=4,
                                           column=0,sticky="w",padx=10,pady=5)

# ADD TRANSACTION

transaction_frame=tk.LabelFrame(content_frame,
                                text="ADD TRANSACTION",font=menu_font,
                                bg="#EAF6F6")
transaction_frame.pack(fill="x",padx=20,pady=10)

tk.Label(transaction_frame,text="Member",font=main_font,
         bg="#EAF6F6").grid(row=0,column=0,padx=10,pady=8)

member_combo=ttk.Combobox(transaction_frame,
                          width=30,state="readonly")
member_combo["values"]=("Father","Mother","Son","Daughter","Other")
member_combo.current(0)
member_combo.grid(row=0,column=1,padx=10)

tk.Label(transaction_frame,text="Reason",font=main_font,
         bg="#EAF6F6").grid(row=1,column=0,padx=10,pady=8)

reason_entry=tk.Entry(transaction_frame,width=32,font=main_font)
reason_entry.grid(row=1,column=1,padx=10)

tk.Label(transaction_frame,text="Amount",font=main_font,
         bg="#EAF6F6").grid(row=2,column=0,padx=10,pady=8)

amount_entry=tk.Entry(transaction_frame,width=32,font=main_font)
amount_entry.grid(row=2,column=1,padx=10)

def update_dashboard():
    if current_user=="":
        return
    data=dashboard(current_user)
    welcome_var.set("Welcome : "+current_user)
    limit_var.set("Financial Limit : ₹"+str(data[0]))
    balance_var.set("Remaining Balance : ₹"+str(data[1]))
    goal_var.set("Savings Goal : "+str(data[2]))
    progress_var.set("Goal Progress : "+str(data[3])+" %")
    # MENU BUTTONS

button_frame=tk.LabelFrame(menu_frame,text="MENU",
                           font=menu_font,bg="#EAF6F6")
button_frame.pack(fill="both",expand=True,padx=10,pady=10)

def login_gui():
    global current_user
    username=username_entry.get()
    password=password_entry.get()
    user=login(username,password)
    if user:
        current_user=user
        update_dashboard()
        transaction_btn.config(state="normal")
        show_btn.config(state="normal")
        report_btn.config(state="normal")
        goal_btn.config(state="normal")
        member_btn.config(state="normal")
        logout_btn.config(state="normal")
        change_btn.config(state="normal")
        username_entry.config(state="disabled")
        password_entry.config(state="disabled")

def logout_gui():
    global current_user
    current_user=""
    username_entry.config(state="normal")
    password_entry.config(state="normal")
    username_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
    welcome_var.set("Welcome :")
    limit_var.set("Financial Limit :")
    balance_var.set("Remaining Balance :")
    goal_var.set("Savings Goal :")
    progress_var.set("Goal Progress :")

database_btn=tk.Button(button_frame,
                       text="Create Database",width=22,
                       font=main_font,bg="yellow",
                       command=create_database)
database_btn.pack(pady=5)

login_btn=tk.Button(button_frame,
                    text="Login",width=22,
                    font=main_font,bg="lightgreen",
                    command=login_gui)
login_btn.pack(pady=5)

transaction_btn=tk.Button(button_frame,
                          text="Add Transaction",width=22,
                          font=main_font,bg="cyan",
                          state="disabled")
transaction_btn.pack(pady=5)

logout_btn=tk.Button(button_frame,
                     text="Logout",width=22,
                     font=main_font,bg="orange",
                     state="disabled",command=logout_gui)
logout_btn.pack(pady=5)

show_btn=tk.Button(button_frame,
                   text="Show Transactions",
                   width=22,font=main_font,
                   bg="gold",state="disabled")
show_btn.pack(pady=5)

report_btn=tk.Button(button_frame,
                     text="Monthly Report",
                     width=22,font=main_font,
                     bg="lightblue",state="disabled")
report_btn.pack(pady=5)

goal_btn=tk.Button(button_frame,
                   text="Goal Progress",width=22,
                   font=main_font,bg="violet",
                   state="disabled")
goal_btn.pack(pady=5)

member_btn=tk.Button(button_frame,
                     text="Member Expense",width=22,
                     font=main_font,bg="pink",
                     state="disabled")
member_btn.pack(pady=5)

change_btn=tk.Button(button_frame,
                     text="Change Password",
                     width=22,font=main_font,
                     bg="white",state="disabled")
change_btn.pack(pady=5)

create_btn=tk.Button(button_frame,
                     text="Create Account",width=22,
                     font=main_font,bg="lightgray")
create_btn.pack(pady=5)

forgot_btn=tk.Button(button_frame,
                     text="Forgot Password",
                     width=22,font=main_font,
                     bg="khaki")
forgot_btn.pack(pady=5)

exit_btn=tk.Button(button_frame,
                   text="Exit",width=22,font=main_font,
                   bg="tomato",command=root.destroy)
exit_btn.pack(pady=5)


# ADD TRANSACTION FUNCTION

def transaction_gui():
    if current_user=="":
        messagebox.showwarning("Warning","Please Login First")
        return
    member=member_combo.get()
    reason=reason_entry.get().strip()
    amount=amount_entry.get().strip()
    if do_transaction(current_user,member,reason,amount):
        reason_entry.delete(0,tk.END)
        amount_entry.delete(0,tk.END)
        member_combo.current(0)
        update_dashboard()

transaction_btn.config(command=transaction_gui)
# CREATE ACCOUNT

def create_account_window():
    win=tk.Toplevel(root)
    win.title("Create Account")
    win.geometry("500x550")
    win.configure(bg="#EAF6F6")
    labels=["Username","Password","Confirm Password",
            "Financial Limit","Working As","Favourite Movie",
            "Savings Goal","Goal Amount"]
    entries=[]
    for text in labels:
        tk.Label(win,text=text,font=main_font,
                 bg="#EAF6F6").pack(pady=4)
        e=tk.Entry(win,width=30,font=main_font)
        if "Password" in text:
            e.config(show="*")
        e.pack()
        entries.append(e)
    def save():
        if create_account(entries[0].get(),entries[1].get(),
                          entries[2].get(),entries[3].get(),entries[4].get(),
                          entries[5].get(),entries[6].get(),entries[7].get()):
            win.destroy()
    tk.Button(win,text="Create Account",font=main_font,
              bg="lightgreen",command=save).pack(pady=15)

create_btn.config(command=create_account_window)


# FORGOT PASSWORD

def forgot_password_window():
    win=tk.Toplevel(root)
    win.title("Forgot Password")
    win.geometry("400x220")
    win.configure(bg="#EAF6F6")
    tk.Label(win,text="Username",font=main_font,
             bg="#EAF6F6").pack(pady=5)
    u=tk.Entry(win,width=30,font=main_font)
    u.pack()
    tk.Label(win,text="Favourite Movie",font=main_font,
             bg="#EAF6F6").pack(pady=5)
    m=tk.Entry(win,width=30,font=main_font)
    m.pack()
    tk.Button(win,text="Show Password",font=main_font,
              bg="orange",command=lambda:forgot_password(u.get(),
                                                         m.get())).pack(pady=15)

forgot_btn.config(command=forgot_password_window)


# CHANGE PASSWORD

def change_password_window():
    if current_user=="":
        messagebox.showwarning("Warning","Please Login First")
        return
    win=tk.Toplevel(root)
    win.title("Change Password")
    win.geometry("400x300")
    win.configure(bg="#EAF6F6")
    old=tk.Entry(win,width=30,show="*",font=main_font)
    new=tk.Entry(win,width=30,show="*",font=main_font)
    confirm=tk.Entry(win,width=30,show="*",font=main_font)
    for text,e in [("Old Password",old),("New Password",new),
                   ("Confirm Password",confirm)]:
        tk.Label(win,text=text,font=main_font,
                 bg="#EAF6F6").pack(pady=5)
        e.pack()
    def save():
        if change_password(current_user,old.get(),
                           new.get(),confirm.get()):
            win.destroy()
    tk.Button(win,text="Change Password",font=main_font,
              bg="lightgreen",command=save).pack(pady=15)

change_btn.config(command=change_password_window)


# SHOW TRANSACTIONS

def show_transactions_window():
    if current_user=="":
        messagebox.showwarning("Warning","Please Login First")
        return
    win=tk.Toplevel(root)
    win.title("Transactions")
    win.geometry("900x450")
    tree=ttk.Treeview(win,columns=("ID","Member","Reason",
                                   "Amount","Balance","Date","Time"),
                      show="headings")
    for col in ("ID","Member","Reason","Amount",
                "Balance","Date","Time"):
        tree.heading(col,text=col)
        tree.column(col,width=120)
    tree.pack(fill="both",expand=True)
    rows=show_transactions(current_user)
    for row in rows:
        tree.insert("",tk.END,values=row)

show_btn.config(command=show_transactions_window)


# MONTHLY REPORT

def monthly_report_window():
    limit,spent,balance,count=monthly_report(current_user)
    win=tk.Toplevel(root)
    win.title("Monthly Report")
    win.geometry("400x250")
    win.configure(bg="#EAF6F6")
    data=["Financial Limit : ₹"+str(limit),
          "Total Expense : ₹"+str(spent),"Remaining Balance : ₹"+str(balance),
          "Total Transactions : "+str(count)]
    for x in data:
        tk.Label(win,text=x,font=main_font,
                 bg="#EAF6F6").pack(pady=8)

report_btn.config(command=monthly_report_window)


# GOAL PROGRESS

def goal_progress_window():
    goal,target,saving,percent=goal_progress(current_user)
    win=tk.Toplevel(root)
    win.title("Goal Progress")
    win.geometry("400x250")
    win.configure(bg="#EAF6F6")
    data=["Goal : "+str(goal),"Goal Amount : ₹"+str(target),
          "Current Savings : ₹"+str(saving),
          "Completed : "+str(percent)+" %"]
    for x in data:
        tk.Label(win,text=x,font=main_font,
                 bg="#EAF6F6").pack(pady=8)

goal_btn.config(command=goal_progress_window)

# MEMBER EXPENSE

def member_expense_window():
    if current_user=="":
        messagebox.showwarning("Warning","Please Login First")
        return

    win=tk.Toplevel(root)
    win.title("Member Expense")
    win.geometry("600x400")
    win.configure(bg="#EAF6F6")

    tree=ttk.Treeview(win,columns=("Member","Total Expense"),
                      show="headings")

    tree.heading("Member",text="Member")
    tree.heading("Total Expense",text="Total Expense")

    tree.column("Member",width=200)
    tree.column("Total Expense",width=200)

    tree.pack(fill="both",expand=True,padx=20,pady=20)

    data=member_expense(current_user)

    for row in data:
        tree.insert("",tk.END,values=row)


member_btn.config(command=member_expense_window)
