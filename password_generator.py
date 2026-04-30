import secrets
import string

num = 0
synum = ""
strandom = ""
passw = ""

def length(num):
    while True:
        try:   
            num = int(input("how long do you want your password to be: "))
            break
        except ValueError:
            print("enter an integer")
            continue
    return num
num = length(num)

def choice(synum):
    while synum not in ["yes" , "no"]:
        synum = input("do you want to include symbols: ").lower()
        if synum == "yes" or synum == "no":
            return synum
        else:
            print("choose from yes or no")
synum = choice(synum)

def result(strandom):
    if synum == "no":
        strandom = string.ascii_letters + string.digits
    else:
        strandom = string.ascii_letters + string.digits + string.punctuation
    return strandom
strandom = result(strandom)

passw += ''.join(secrets.choice(strandom) for i in range (num))
print(passw)
