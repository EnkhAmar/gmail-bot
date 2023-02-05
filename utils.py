import csv
import os
from itertools import islice

def save_as_csv(file:str, data:list):
    fnames = ["id", "first_name", "last_name", "dob", "sex", "country_code", "phone", "username", "password", "created_at"]
    if not os.path.isfile(file):
        with open(file, "w", newline="") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=fnames)
            writer.writeheader()
    with open(file, "a", newline="") as file:
        appender = csv.DictWriter(file, fieldnames=fnames)
        for item in data:
            appender.writerow(item)


if __name__ == "__main__":
    users = [
        { "id": 1, "first_name": "test1", "last_name": "test1", "dob": "1999-01-01", "sex": "M", "country_code": "976", "phone": "00000000", "username": "username", "password": "pwd" },
        { "id": 2, "first_name": "test2", "last_name": "test2", "dob": "2000-02-02", "sex": "M", "country_code": "976", "phone": "00000000", "username": "username", "password": "pwd" },
        { "id": 3, "first_name": "test3", "last_name": "test3", "dob": "2011-11-11", "sex": "M", "country_code": "976", "phone": "00000000", "username": "username", "password": "pwd" }
    ]
    save_as_csv("file.csv", users)