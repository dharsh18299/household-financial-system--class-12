from tkinter import messagebox
from database import connection
from datetime import datetime

def do_transaction(username,member,reason,amount):
    if member=="" or reason=="" or amount=="":
        messagebox.showerror("Error","Fill All Fields")
        return False
    try:
        amount=float(amount)
    except:
        messagebox.showerror("Error","Enter Valid Amount")
        return False
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT financial_limit FROM users
                WHERE username=%s''',(username,))
    limit=cur.fetchone()[0]
    cur.execute('''SELECT IFNULL(SUM(amount),0)
                FROM transactions
                WHERE username=%s''',(username,))
    spent=cur.fetchone()[0]
    if spent+amount>limit:
        con.close()
        messagebox.showerror("Error","Insufficient Balance")
        return False
    if ((spent+amount)/limit)*100>=80:
        messagebox.showwarning("Warning",
                               "You have used 80% of your Financial Limit")
    balance=limit-(spent+amount)
    now=datetime.now()
    d=now.strftime("%Y-%m-%d")
    t=now.strftime("%H:%M:%S")
    cur.execute('''INSERT INTO transactions(username,member,
                reason,amount,balance_left,date1,time1)
                VALUES(%s,%s,%s,%s,%s,%s,%s)''',
                (username,member,reason,amount,balance,d,t))
    con.commit()
    con.close()
    messagebox.showinfo("Success","Transaction Added Successfully")
    return True

def show_transactions(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT id,member,reason,amount,
                balance_left,date1,time1 FROM transactions
                WHERE username=%s ORDER BY id''',(username,))
    rows=cur.fetchall()
    con.close()
    return rows

def delete_transaction(id):
    con=connection()
    cur=con.cursor()
    cur.execute("DELETE FROM transactions WHERE id=%s",(id,))
    con.commit()
    con.close()
    messagebox.showinfo("Success","Transaction Deleted Successfully")

def total_spent(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT IFNULL(SUM(amount),0)
                FROM transactions WHERE username=%s''',(username,))
    amount=cur.fetchone()[0]
    con.close()
    return amount

def remaining_balance(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT financial_limit FROM users
                WHERE username=%s''',(username,))
    limit=cur.fetchone()[0]
    cur.execute('''SELECT IFNULL(SUM(amount),0)
                FROM transactions WHERE username=%s''',(username,))
    spent=cur.fetchone()[0]
    con.close()
    return limit-spent

def transaction_count(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT COUNT(*) FROM transactions
                WHERE username=%s''',(username,))
    count=cur.fetchone()[0]
    con.close()
    return count
def remaining_balance(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT financial_limit
                FROM users WHERE username=%s''',(username,))
    limit=cur.fetchone()[0]
    cur.execute('''SELECT IFNULL(SUM(amount),0) FROM
                transactions WHERE username=%s''',(username,))
    spent=cur.fetchone()[0]
    con.close()
    return limit-spent

def total_transactions(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT COUNT(*) FROM transactions
                WHERE username=%s''',(username,))
    count=cur.fetchone()[0]
    con.close()
    return count

def total_expense(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT IFNULL(SUM(amount),0) FROM
                transactions WHERE username=%s''',(username,))
    amount=cur.fetchone()[0]
    con.close()
    return amount
