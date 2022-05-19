import sqlite3

# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("custommer.db")

c = conn.cursor()

c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
)""")

# DATATYPES
# NULL
# INTERGER
# REAL
# TEXT
# BLOB - as is

conn.commit()

c.execute(
    "INSERT INTO customers VALUES ('Miguel', 'Busarello Lauterjung', 'mbl@email.com')")
conn.commit()

many_customers = [("Miguel", "Busarello", "mb@email.com"),
                  ("Miguel", "Lauterjung", "ml@email.com"),
                  ("A", "B C", "abc@email.com")]
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
conn.commit()

# c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany()
# c.fetchall()
# print(c.fetchall())

# c.execute("SELECT rowid, * FROM customers")
# print(c.fetchall())

# c.execute("SELECT * FROM customers WHERE first_name = 'Miguel'")
# print(c.fetchall())

# c.execute("SELECT * FROM customers WHERE email LIKE '%.com'")
# print(c.fetchall())

# c.execute(
#     """UPDATE customers SET first_name = 'Larissa' WHERE last_name = 'Lauterjung'""")
# conn.commit()
# c.execute("SELECT rowid, * FROM customers")
# print(c.fetchall())

# c.execute(
#     """UPDATE customers SET first_name = 'Miguel' WHERE rowid = 3""")
# conn.commit()
# c.execute("SELECT rowid, * FROM customers")
# print(c.fetchall())

# c.execute("DELETE from customers WHERE rowid = 3")
# conn.commit()
# c.execute("SELECT rowid, * FROM customers")
# print(c.fetchall())

# c.execute("SELECT * from customers ORDER BY last_name DESC, first_name")
# conn.commit()
# print(c.fetchall())

# c.execute("SELECT * from customers WHERE rowid = 3 OR rowid = 1")
# conn.commit()
# print(c.fetchall())

# c.execute("SELECT * from customers LIMIT 2")
# conn.commit()
# print(c.fetchall())

# c.execute("DROP TABLE customers")
# conn.commit()

conn.close()
