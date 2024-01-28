# Escape character example
print("Hello\nHow are you\ni'm fine")
# Hello
# How are you
# i'm fine

# Raw Strings
print(r'Hello\tHow are you\tiam fine')
# Hello\tHow are you\tiam fine

#Indices and slices
spam = 'Hello World!'
print (spam[0])
# H
print (spam[-1])
# !
print (spam[1:5])
# ello

# upper()
print (spam.upper())
# HELLO WORLD!

# lower()
print (spam.lower())
# hello world!

# isupper() - check if variable is in uppercase or not. returns bool true or false
print(spam.isupper())
# False

# is lower()
spam=spam.lower()
print (spam.islower())
# True

# startswith
print(spam.startswith('hello'))
# True

# endswith
print(spam.endswith('world!'))
# True

# Join method
animals = ['cat','bat','rat']
print (','.join(animals))
# cat,bat,rat
print ('-'.join(spam))
# h-e-l-l-o- -w-o-r-l-d-!

# split() method
print (spam.split())
# ['hello', 'world!']
print (spam.split('o'))
# ['hell', ' w', 'rld!']

# ljust(),rjust(),center
print (spam.ljust(20,'*'))
# hello world!********
print (spam.rjust(20,'-'))
# --------hello world!
print (spam.center(20,'*'))
# ****hello world!****

# strip() - strip whitespace(by default) from the string
print ('    Hello'.strip())
# Hello
print (spam.strip('he'))
# llo world!
print ('****Hello****'.lstrip('*'))
# Hello****
print ('****Hello****'.rstrip('*'))
# ****Hello

# replace()
print (spam.replace('world','universe'))
# hello universe!

# String Formatting
name = 'Alice'
place = 'Main Street'
time = '6pm'
food = 'turnips'
print ('Hello %s, You are invited to the party at %s at %s. Please bring %s.' %(name,place,time,food))
# Hello Alice, You are invited to the party at Main Street at 6pm. Please bring turnips.
