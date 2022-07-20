import random           

raju = random.randint(1,3)
# print(raju)
s = 'stone'
p = 'paper'
c = 'scissor'
if raju == 1 :
    c1 = ('s')
elif raju == 2:
    c1 = ('p')
elif raju == 3:
    c1 = ('c')

p1 = input("Player input Choose \nStone(s)\nPaper(p)\nScissor(c)\n")
print(f"Comp choose {c1}")
print(f"You choose {p1}")
def game():
 if c1 == p1 :
    print("Tie")
 elif c1 == ('s') and p1 == ('p'):
    print("You won")
 elif c1 == ('s') and p1 == ('c'):
    print("You loose")
 elif c1 == ('p') and p1 == ('s'):
    print("You loose")
 elif c1 == ('p') and p1 == ('c'):
    print("You won")
 elif c1 == ('c') and p1 == ('s'):
    print("You won")
 elif c1 == ('c') and p1 == ('p'):
    print("You loose")

