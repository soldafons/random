import random
import string

strandom = ""
passw = ""
synum = ""
num = 0

while True:
    try:
        num = int(input("how long do you want your password to be"))
        break
    except ValueError:
        print("enter an integer")
        continue
while synum not in ["yes", "no"]:
        synum = input("do you want to include symbols?").lower()
        print("choose from yes or no")

if synum == "no":
    strandom = string.ascii_letters + string.digits
elif synum == "yes":
    strandom = string.ascii_letters + string.digits + string.punctuation

for i in range(1, num+1):
    passw += random.choice(strandom)
print(passw)