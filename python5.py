import os
from time import gmtime, strftime

order = []
dic={"Tea":10,"coffee":20,"burger":40,"pizza":50}

while True :
    o=input("order : ")
    if o =="done":
        os.system("cls")
        print("your order is : ")
        total = 0
        for product in order :
            print(product+" : "+str(dic[product]))
            total+=dic[product]
        print(f"total : {total}")
        print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        with open("log.txt","a") as z:
            z.write(f"total : {total}")
            z.write("\n")
            z.write(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            z.write("\n")
            z.write("..................................................................")
            z.write("\n")
            z.close()
        break
    if o in dic :
        order.append(o)
        print("added")
    else :
        print("not available")
