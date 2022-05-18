import sqlite3

conn = sqlite3.connect(":memory:")
# conn = sqlite3.connect("custommer.db")

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

c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany()
# c.fetchall()
print(c.fetchall())

conn.close()
