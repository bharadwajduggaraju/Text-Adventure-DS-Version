import argon2
import secrets

##__util__ to hash the password using argon
#Example repl: https://replit.com/@jasonthename/Argon2-Password-Hashing-in-Python

def hash_password(plaintext):
  random_string = secrets.token_hex(8)  
  return argon2.argon2_hash(plaintext, random_string)
