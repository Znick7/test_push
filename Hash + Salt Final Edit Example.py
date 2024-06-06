
import getpass
import hashlib
import os
import getpass

# User prompt to enter info // signup
username = input("Enter your username: ")
passwords = getpass.getpass("Enter your password: ")

new_account = username
temp_password = passwords
#to confirm that real text is being salted and hashed
print(passwords)
# Set salt value
salt = os.urandom(16)

# Adding salt to password
salted_password = salt + temp_password.encode()

# Hashing salted password
hashed_password = hashlib.sha256(salted_password).hexdigest()

# Printing salt and hashed password
print(f"Salt: {salt.hex()}")
print(f"Hashed Password: {hashed_password}")
  

