from database import connection

def monthly_report(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT financial_limit FROM users WHERE
                username=%s''',(username,))
    limit=cur.fetchone()[0]
    cur.execute('''SELECT IFNULL(SUM(amount),0) FROM transactions
                WHERE username=%s''',(username,))
    spent=cur.fetchone()[0]
    balance=limit-spent
    cur.execute('''SELECT COUNT(*) FROM transactions
                WHERE username=%s''',(username,))
    count=cur.fetchone()[0]
    con.close()
    return limit,spent,balance,count

def goal_progress(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT financial_limit,goal_name,goal_amount
                FROM users WHERE username=%s''',(username,))
    data=cur.fetchone()
    cur.execute('''SELECT IFNULL(SUM(amount),0) FROM
                transactions WHERE username=%s''',(username,))
    spent=cur.fetchone()[0]
    savings=data[0]-spent
    percent=0
    if data[2]>0:
        percent=(savings/data[2])*100
    if percent>100:
        percent=100
    if percent<0:
        percent=0
    con.close()
    return data[1],data[2],savings,round(percent,2)

def member_expense(username,member):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT IFNULL(SUM(amount),0) FROM
                transactions WHERE username=%s AND
                member=%s''',(username,member))
    total=cur.fetchone()[0]
    con.close()
    return total

def all_members(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT DISTINCT member FROM transactions
                WHERE username=%s ORDER BY member''',(username,))
    data=cur.fetchall()
    con.close()
    return [i[0] for i in data]

def expense_summary(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT member,IFNULL(SUM(amount),0)
                FROM transactions WHERE username=%s
                GROUP BY member ORDER BY member''',(username,))
    data=cur.fetchall()
    con.close()
    return data

def latest_transactions(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT member,reason,amount,date1,
                time1 FROMtransactions WHERE username=%s
                ORDER BY id DESC LIMIT 5''',(username,))
    data=cur.fetchall()
    con.close()
    return data

def highest_expense(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT reason,amount FROM transactions
                WHERE username=%s ORDER BY
                amount DESC LIMIT 1''',(username,))
    data=cur.fetchone()
    con.close()
    if data:
        return data
    return "No Data",0

def lowest_expense(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT reason,amount FROM transactions
                WHERE username=%s ORDER BY
                amount ASC LIMIT 1''',(username,))
    data=cur.fetchone()
    con.close()
    if data:
        return data
    return "No Data",0
def dashboard(username):
    con=connection()
    cur=con.cursor()
    cur.execute('''SELECT financial_limit,goal_name,goal_amount
                FROM users WHERE username=%s''',(username,))
    data=cur.fetchone()
    cur.execute('''SELECT IFNULL(SUM(amount),0) FROM
                transactions WHERE username=%s''',(username,))
    spent=cur.fetchone()[0]
    balance=data[0]-spent
    percent=0
    if data[2]>0:
        percent=(balance/data[2])*100
    if percent>100:
        percent=100
    if percent<0:
        percent=0
    con.close()
    return data[0],balance,data[1],round(percent,2)
