
import random

raju = random.randint(1,50)
user = None
reticle = 0
print(raju)
while user != raju :
    
    a = int(input("guess number : "))
    reticle += 1
    
    
    if raju < a :
        print("lower number please,Try again :)")
        
    elif raju > a :
        print("\nhigher number please,Try again :)")
        
    else :
        print("\ncorrect")
        break

print(f"You did it in {reticle} tries")