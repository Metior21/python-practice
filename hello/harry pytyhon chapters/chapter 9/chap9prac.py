"""
f = open('bilt.txt', 'a')
f.write('babbool ki fasal')
f.close()
"""

# Write a program to read the text from a given file, “poems.txt”
# and find out whether it contains the word ‘twinkle’.
"""
with open('poems.txt', 'r') as f:
    l = f.read()
if 'twinkle' in l:
    print('yeh boy')
else:
    print('raja babau')
    print(l)
"""


# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file “Hiscore.txt” which is either 
# blank or contains the previous Hi-score. You need to write a program to update 
#  Hi-score whenever game() breaks the Hi-Score.
"""
    
import random

def game():
    raju = random.randint(1,100)
    return raju
var=game()
print(var)

with open ('highscore.txt', 'r') as f:
         v = f.read()

print(v)

if var >= int(v):
    with open ('highscore.txt', 'w') as j:
        h = j.write(str(var))
    with open ('highscore.txt', 'r') as f:
         v = f.read()
    print(v)
elif var <= int(v):
    print("score better and try again")
""" 



# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13- year old boy.

"""
with open ("table.txt", "w") as f:
    f.write("new")
"""

# # def multi():
# m = int(input("Multiplication of ?")) 
# for x in range(1,10):
#     k = x*m
#     print (k)      

# if m <= 5 :
#     with open ("table1.txt, w") as f:
#         z = f.write(k)

# print(multi())
"""
for m in range(2,21):
    with open (f"table1.txt{m}", "w") as f:
            for x in range(1,11):
                f.write(f"{m} X {x} = {m*x}\n")
"""        


# A file contains the word “Donkey” multiple times. You need to write a program which 
# replaces this word with ###### by updating the same file.
"""
with open("table.txt","r") as f:
    m = f.read()
    m = m.replace("Donkey","######")
    with open("table.txt","w") as j:
        j.write(m)
"""

# Repeat program 4 for a list of such words to be censored.
words = ["donkey","jagdish","raju","hulla"]
for word in words:
    with open("Newtable.txt","r") as f:
     m = f.read()
     m = m.replace(word,"######")
    with open("Newtable.txt","w") as j:
        j.write(m)

# Write a program to mine a log file and find out whether it contains ‘python’.



# Write a program to find out the line number where python is present from question 6.



# Write a program to make a copy of a text file “this.txt.”



# Write a program to find out whether a file is identical and matches the content
#  of another file.



# Write a program to wipe out the contents of a file using python.



# Write a python program to rename a file to “renamed_by_python.txt.”

