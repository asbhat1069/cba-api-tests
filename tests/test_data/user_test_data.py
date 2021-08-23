import os
from faker import Faker

f = Faker()


users_data = [(f.name(), 0), (f.name(), 10)]

delete_key = os.getenv("DELETE_KEY")
