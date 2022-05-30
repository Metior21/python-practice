# Write a Python program to display a user-entered name followed 
# by Good Afternoon using input() function.
"""
a = input("Name")
print ('Good Afternoon', (a))
"""
# Write a program to fill in a letter template given below with name and date.
# letter = ‘’’ Dear <|NAME|>,
#              You are selected!

#                 <|DATE|>
"""
import datetime

x = datetime.datetime.now()

a = input('Name')


print ('Dear',(a),'\nYou are Selected\n',(x))
"""
# Write a program to detect double spaces in a string.
"""
name = 'Sidak'
sl = name[0::2]
print(sl)

non
"""
"""
check_db_sp = "Si  dak  no  no karta hai  lekin is agoodboy"
  
# printing original string 
print("The original string is : " + check_db_sp)
  
# Using in operator
# Check for spaces 
res = " " in check_db_sp

# printing result 
print("Does string contain spaces ? " + str(res))

"""
# Replace the double spaces from problem 3 with single spaces.
"""
def remove(string):
    return string.replace("  ", " ")
      
# Driver Program
string = 'Si  dak  no  no karta hai  lekin is agoodboy  '
print(remove(string))
"""
"""
string = 'i  dak  no  no karta hai  lekin is agoodboy  '
print(string.replace('  ',' '))
"""

# Write a program to format the following letter using escape sequence characters.
# letter = “Dear Harry, This Python course in nice. Thanks!!”

a = "Dear Harry, \nThis \tPython course in nice. \n\\Thank\'s!!"
print(a)