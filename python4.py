import os
import time
#make product dictionry
dic={"Tea":10,"coffee":20,"burger":40,"pizza":50}
#calculate function
def calc():
    c=input("Your order : ")
    h=input("How many : ")
    total = dic[c]*int(h)
    if total >= 100:
        print("you are a special customer")
        print(f"total : {total} + Small gift")
    else :
        print(f"total : {total}")
    time.sleep(5)
    os.system("cls")

while True :
    calc()