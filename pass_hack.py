import time
import os

password_attempts = [
    "admin",
    "password",
    "123456",
    "letmein",
    "welcome",
    "qwerty",
    "abc123",
     "admin",
    "password",
    "123456",
    "letmein",
    "welcome",
    "qwerty",
    "abc123",
    "Abc$123"
]

real_password = "Abc$123"

print("\nInitializing brute force attack...\n")
time.sleep(0.2)

for guess in password_attempts:

    os.system("cls")

    print("HACKING SYSTEM...\n")
    print("Trying password:", guess)

    time.sleep(0.1)

    if guess == real_password:
        print("\nPASSWORD FOUND:", guess)
        print("ACCESS GRANTED")
        break