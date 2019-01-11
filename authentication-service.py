import bcrypt
import csv
import os.path as path
import getpass

def unique(uname):
    with open("user_store.store") as user_store:
        reader = csv.reader(user_store, delimiter=",")
        line_count = 0
        for line in reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                user_name_from_store = line[0]
                if user_name_from_store == uname:
                   return False
                line_count += 1
    return True

def add_user_to_store(uname, hashed_pword):
    if not path.exists("user_store.store"):
        with open("user_store.store", "a+") as f:
            f.write("uname,hashed_pword\n")
            f.write(f"{uname},{hashed_pword}\n")
            print ("User successfully added")
    if unique(uname):
        with open("user_store.store", "a+") as f:
            f.write(f"{uname},{hashed_pword}\n")
        print("User successfully added")
        return
    else:
        print("User already exists")
        return

def validate_login(uname, pword):
    hashed_pword = get_hash_from_store(uname)
    return True if hashed_pword == bcrypt.hashpw(pword.encode(), hashed_pword) else False

def get_hash_from_store(uname):
    with open("user_store.store") as user_store:
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
    user_pass = getpass.getpass().encode()
    return user_name, user_pass

def hash_pass(pword):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(pword, salt)
    hashed_pass = hashed_pass.decode()
    return hashed_pass
