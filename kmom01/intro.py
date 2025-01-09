import random
import time
value = random.randint(0,10)

print("Datorn har valt ett nummer mellan 1 och 10,")
time.sleep(1)
guess = input("Gissa nummret mellan 1 och 10\n")

#loop until correct
while(value != guess):
    print("Tyvärr, försök igen")
    guess = int(input())

#ran after loop
print ("Du har rätt!")
time.sleep(1)
print("Tack för att du spelade")
quit()