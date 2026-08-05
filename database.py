import mysql.connector

def connection():
    return mysql.connector.connect(host="localhost",
                                   user="root",password="12345678",
                                   database="household_finance")

def create_database():
    con=mysql.connector.connect(host="localhost",
                                user="root",password="12345678")
    cur=con.cursor()
    cur.execute('''CREATE DATABASE IF NOT EXISTS
                household_finance''')
    cur.execute("USE household_finance")
    cur.execute('''CREATE TABLE IF NOT EXISTSusers
                (username VARCHAR(30) PRIMARY KEY,
                 password VARCHAR(50),financial_limit FLOAT,
                 working_as VARCHAR(50),fav_movie VARCHAR(50),
                 goal_name VARCHAR(100),goal_amount FLOAT)''')


    cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                (id INT AUTO_INCREMENT PRIMARY KEY,
                 username VARCHAR(30),member VARCHAR(30),
                 reason VARCHAR(50),amount FLOAT,balance_left FLOAT,
                 date1 DATE,time1 TIME)''')
    con.commit()
    con.close()
