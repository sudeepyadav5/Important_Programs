import re


def is_Valid_Password(passwords):
    if not re.search('[A-Z]', passwords):
        return False
    if not re.search('[a-z]',passwords):
        return False
    if not re.search('[0-9]',passwords):
        return False
    if not re.search('[@#%&*?]',passwords):
        return False
    return True


pwd = input("Enter Your Password: ")
passwords = [pwd]
for password in passwords:
    if is_Valid_Password(password):
        print(f"{password} is Valid Password")
    else:
        print(f"{password} is InValid Password, Password must be 1 Capital latter, 1 small latter , 1 special and 1 "
              f"Numeric")

