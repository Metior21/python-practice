# Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up!\

dictionary = { 
            'aaam' : 'mango',
            'paani' :'water',
            'aaram' : 'rest'
}

print(dictionary.keys())
a = input ('the hindi word :')
print('the meaning of your word in english is :', dictionary[a])

# Write a program to input eight numbers from the user and display all the unique numbers (once).
"""
a =input('Number 1 :') 
b =input('Number 2 :') 
c =input('Number 3 :') 
d =input('Number 4 :') 
f =input('Number 5 :') 
g =input('Number 6 :') 
h =input('Number 7 :') 
i =input('Number 8 :') 

sewt = {(a),(b),(c),(d),(f),(g),(h),(i)}


print(sewt)
"""

# Can we have a set with 18(int) and “18”(str) as a value in it?
"""
sewt = {1, 2, 18, '18'}
print(sewt)
"""


# What will be the length of the following set S:
# S = Set()
# S.add(20)
# S.add(20.0)
# S.add(“20”)
# What will be the length of S after the above operations?
"""
s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s))

"""

# S = {}, what is the type of S?
"""
2
"""

# Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.
"""
a = input ('Name :')
b = input ('Name 2 :')
mydict = { (a) : 'english',
           (b) : 'spanish'

}

print(mydict)
"""
"""
mydict = {}
a = input ("raju's favorite language :")
b = input ("boni's favorite language :")
c = input ("hulu's favorite language :")
d = input ("kuku's favorite language :")

mydict.update ({'raju' : (a)})
mydict.update ({'boni' : (b)})
mydict.update ({'hulu' : (c)})
mydict.update ({'kuku' : (d)})

print(mydict)
"""

# If the names of 2 friends are the same; what will happen to the program in Program 6?

"""
it will overrite the value of the  key or the name of the student
"""
# If the languages of two friends are the same; what will happen to the program in Program 6?
"""
it will not ovweridw but the values will be stored under the key

mydict = {}
a = input ("raju's favorite language :")
b = input ("boni's favorite language :")
c = input ("hulu's favorite language :")
d = input ("kuku's favorite language :")

mydict.update ({'raju' : (a)})
mydict.update ({'boni' : (a)})
mydict.update ({'hulu' : (c)})
mydict.update ({'kuku' : (d)})

print(mydict)
"""
# Can you change the values inside a list which is contained in set S
# S = {8, 7, 12, “Harry”, [1, 2]}
"""
NO

list = [1,2]
S = {8, 7, 12, 'Harry', [1, 2]}
"""


