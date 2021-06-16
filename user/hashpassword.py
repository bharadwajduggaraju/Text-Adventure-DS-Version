import argon2
import requests
from user.config.floo import slt
#import os

##__util__ to hash the password using argon
def hash_password(plaintext):
  #salt = os.environ['TOKEN_SECRET']
  return argon2.argon2_hash(plaintext, slt)




