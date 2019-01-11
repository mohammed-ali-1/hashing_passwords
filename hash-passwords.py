import bcrypt
import csv
import os.path as path
import getpass

def get_user_creds():
    user_name = input("Your user name: ")
    user_pass = getpass.getpass().encode()
    return user_name, user_pass

def hash_pass(pword):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(user_pass, salt)
    hashed_pass = hashed_pass.decode()
    return hashed_pass

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

user_name, user_pass = get_user_creds()
hashed_pword = hash_pass(user_pass)
add_user_to_store(user_name, hashed_pword)
