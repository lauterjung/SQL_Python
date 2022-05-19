import sqlite3


def show_all():
    conn = sqlite3.connect("custommer.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.close()


def add_one(first_name: str, last_name: str, email: str):
    conn = sqlite3.connect("custommer.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO customers VALUES (?,?,?)", (first_name, last_name, email))
    conn.commit()
    conn.close()


def delete_one(id: str):
    conn = sqlite3.connect("custommer.db")
    c = conn.cursor()
    c.execute(
        "DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


def add_many(input_list: list):
    conn = sqlite3.connect("custommer.db")
    c = conn.cursor()
    c.executemany(
        "INSERT INTO customers VALUES (?,?,?)", input_list)
    conn.commit()
    conn.close()


def email_lookup(email):
    conn = sqlite3.connect("custommer.db")
    c = conn.cursor()
    c.execute(
        "SELECT * from customers WHERE email = (?)", (email,))
    items = c.fetchall()
    
    for item in items:
        print(item)

    conn.close()
