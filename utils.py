import csv
import os
from itertools import islice

def save_as_csv(file:str, data:list):
    fnames = ["id", "first_name", "last_name", "dob", "sex", "country_code", "phone", "username", "password"]
    if not os.path.isfile(file):
        with open(file, "w", newline="") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=fnames)
            writer.writeheader()
    with open(file, "a", newline="") as file:
        appender = csv.DictWriter(file, fieldnames=fnames)
        for item in data:
            appender.writerow(item)

users = [
    { "id": 1, "first_name": "test", "last_name": "test", "dob": "", "sex": "M", "country_code": "976", "phone": "00000000", "username": "username", "password": "pwd" }
]

save_as_csv("file.csv", users)