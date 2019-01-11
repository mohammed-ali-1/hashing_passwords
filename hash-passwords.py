import bcrypt
import os.path as path

def get_user_creds():
    user_name = input("Your user name: ")
    user_pass = input("Your password: ").encode()
    return user_name, user_pass

def hash_pass(pword):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(user_pass, salt)
    hashed_pass = hashed_pass.decode()
    return hashed_pass

def add_user_to_store(uname, hashed_pword):
    if not path.exists("user_store"):
        with open("user_store", "a+") as f:
            f.write("uname,hashed_pword\n")
    with open("user_store", "a+") as f:
        f.write(f"{uname},{hashed_pword}\n")

    print("User successfully added")

user_name, user_pass = get_user_creds()
hashed_pword = hash_pass(user_pass)
add_user_to_store(user_name, hashed_pword)
