data = {
    "first_name": "Zachary",
    "last_name": "Mauldin",
    "email": "email",
    "address": "address",
    "city": "city",
    "state": "state",
    "zipcode": "zipcode",
}

first_names = ("John", "Andy", "Joe")
last_names = ("Johnson", "Smith", "Williams")
emails_suffix = (
    "@gmail.com",
    "@yahoo.com",
    "@heb.com",
)
addresses = ("1111 Buckies Road", "2222 Pioneer Rd.")
cities = ("San Antonio", "Austin", "Dallas")
states = ("Tx", "Ca", "Mn")
zipcodes = ("1111", "2222", "3333")


def generate_customer():
    import random

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = first_name[:-1] + last_name[:-2] + random.choice(emails_suffix)
    address = random.choice(addresses)
    city = random.choice(cities)
    state = random.choice(states)
    zipcode = random.choice(zipcodes)
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "address": address,
        "city": city,
        "state": state,
        "zipcode": zipcode,
    }


def create_customers(limit=40):
    from models import Customer

    customers = Customer.get_all()

    if len(customers) < limit:
        for _ in range(limit):
            Customer.create_customer(generate_customer())
