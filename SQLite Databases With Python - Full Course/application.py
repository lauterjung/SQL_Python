import database

database.show_all()

database.add_one("M", "B L", "mbl@email.com")
database.show_all()

database.delete_one("1")
database.show_all()

input_list = [
    ("M", "Lauter", "mlauter@email.com"),
    ("M", "Busarello", "mbusarello@email.com")
]

database.add_many(input_list)
database.show_all()

database.delete_one("2")
database.show_all()

database.email_lookup("mbl@email.com")