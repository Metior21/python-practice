# Quick Quiz: Write a program to print yes when the 
# age entered by the user is greater than or equal to 18.
"""
age = int(input('your age\n'))
if (age >= 18) :
    print('yes 18+')
else :
    print('below 18')
"""

# Write a program to find the greatest of four numbers entered by the user.
"""
a= int(input('number'))
b= int(input('number'))
c= int(input('number'))
d= int(input('number'))

list = [(a), (b), (c), (d)]
maxi = max(list)

print(maxi)
"""


# Write a program to find out whether a student is pass or
# fail if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user.
"""
a= int(input('how many marks in English\n'))
b= int(input('how many marks in Devanagari\n'))
c= int(input('how many marks in hindi\n'))

dict = {
    'english' : (a),
    'devanagari' : (b),
    'hindi' : (c),
} 

calcu =(float(((a+b+c)/300)*100))


if(calcu > 40):
    print('Pass')
    print(calcu)
elif(a > 33) :
    print("English Pass")
elif(b > 33) :
    print("devanagari Pass")
elif(b > 33) :
    print("hindi Pass")
else :
    print('Fail')



a= int(input('how many marks in English\n'))
b= int(input('how many marks in Devanagari\n'))
c= int(input('how many marks in hindi\n'))



dict = {
    'english' : (a),
    'hindi' : (b),
    'maths' : (c)
}

print(str(float((a)+(b)+(c)/ (a+b+c)))+ " %")

"""
# if ((a)+(b)+(c)/len(dict)*100 >=33):
#     print("PASS")
# else :
#     print('FAIL')


# A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”.
#  Write a program to detect these spams.
"""
bilkhu = input("here text")

text = ("let us , “buy now”, “subscribe this”, “click this”")
dict = {
    'make a lot of money' : 'Spam',
    'buy now' : 'spam',
    'subscribe this' : 'spam',
    'click this' : 'spam'
    
}

if ('make a lot of money'in bilkhu):
    print('this si spam span')
"""
"""
elif('buy now' in dict):
    print('spam')
elif( 'subscribe this' in dict):
    print('spam')
elif('click this' in dict):
    print('spam')
else:
    print('no span')
"""




"""

mail = ['“make a lot of money”, “buy now”, “subscribe this”, “click this”']

a='“make a lot of money”'
b='buy now'
c="subscribe this"
d="click this"

if (mail == ({'buy now' : 'spam'}) ) :
    print('SPAM')
else:
    print('Safe')
"""
# Write a program to find whether a given
# username contains less than 10 characters or not.
"""
a = input('user Name\n')

set = set(a)
print(len(set))

if (len(set)<10):
    print('less')
else:
    print('more')
"""
"""
a = input('user Name\n')
print(len(a))

if (len(a)<10):
    print("less")
else:
    print("no way")
"""

# Write a program that finds out whether a 
# given name is present in a list or not.
"""
list = [1, 2, 'harry', 'Sidak']

a = input("username")

if (a in list):
    print("okboka")
else:
    print('not there')
"""
# Write a program to calculate the grade of a student
# from his marks from the following scheme:
# 90-100	Ex
# 80-90	A
# 70-80	B
# 60-70	C
# 50-60	D
# <50	F
"""
marks = int(input("how much marks\n"))

if(marks>=90 and marks<=100):
    print('A+')
elif(marks>=80 and marks<=90):
    print('A')
elif(marks>=70 and marks<=80):
    print('B')
elif(marks>=60 and marks<=70):
    print('C')
elif(marks>=50 and marks<=60):
    print('D')
elif(marks<50):
    print('F')
else :
    print('invalid input')
"""






# Write a program to find out whether a given post is talking about “Harry” or not.

post = ("talking about harry, harry, , harry puttar")
post=post.lower()

a= 'harry'
print ( post.count(a) )






