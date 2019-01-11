import bcrypt
import csv

def validate_login(uname, pword):
    hashed_pword = get_hash_from_store(uname)
    return True if hashed_pword == bcrypt.hashpw(pword, hashed_pword) else False

def get_hash_from_store(uname):
    with open("user_store.store") as user_store
        reader = csv.reader(user_store, delimiter=",")
        line_count = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                user_name_from_store = line[0]
                hash_from_store = line[1]
                if user_name_from_store == uname:
                   return hash_from_store.encode()
                line_count += 1

def get_user_creds():
    user_name = input("Your username: ")
    user_password = input("Your password: ").encode()

    return user_name, user_password
