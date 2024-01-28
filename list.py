spam = ['cat', 'bat', 'rat', 'elephant']
print (spam[1])
# bat
print (spam[-1])
# elephant
print (spam[1:3])
# ['bat', 'rat']
print (spam[:2])
# ['cat', 'bat']
print (spam[2:])
# ['rat', 'elephant']
spam[1] = 'dog'
print (spam)
# ['cat', 'dog', 'rat', 'elephant']

# List of Lists
animal = [['cat', 'bat'], ['rat', 'elephant']]
print (animal[0])
# ['cat', 'bat']
print ([animal[0][1]])
# ['bat']

# Delete value in a List
del spam[2]
print (spam)
# ['cat', 'dog', 'elephant']

# Length of the string
print (len(spam))
# 3

# Convert values to lists
print (list('Hello'))
# ['H', 'e', 'l', 'l', 'o']

print (list(range(0,10,2)))
# [0, 2, 4, 6, 8]

# For loop with lists
for i in (range(len(spam))):
    print (spam[i])
# cat
# dog
# elephant
    
# Multiple assignment
cat = ['fat', 'orange', 'loud']
size,color,disposition = cat
print (size)
print (color)
print (disposition)
# fat
# orange
# loud

size,color,disposition = 'skinny','black','quiet'
print (size)
print (color)
print (disposition)

# Augmented Operators
num = 42
num += 1
print (num)
# 43
num -= 1
print (num)
# 42
num %=1
print (num)
# 0

# List Methods
spam = ['cat', 'dog', 'elephant']
print (spam.index('dog'))
# 1
print (spam.index('elephant'))
# 2
# If there is duplicate value, index method will return the index of the first occurence of the value

# Append,Insert and Remove list methods
spam = ['cat', 'dog', 'elephant']
spam.append('moose')
print (spam)
# ['cat', 'dog', 'elephant', 'moose']
spam.insert(1,'chicken')
print (spam)
# ['cat', 'chicken', 'dog', 'elephant', 'moose']
spam.remove('chicken')
print (spam)
# ['cat', 'dog', 'elephant', 'moose']
# if there is duplicate value, remove method will remove only the first occurence of the value

# Sort Method
num = [2,5,3.14,1,-7]
num.sort()
print (num)
# [-7, 1, 2, 3.14, 5]

spam = ['cats', 'ants', 'elephents', 'badgers']
spam.sort()
print (spam)
# ['ants', 'badgers', 'cats', 'elephents']
spam.sort(reverse=True)
print (spam)
# ['elephents', 'cats', 'badgers', 'ants']
# When we have integer and string in the list, it wont sort the list

spam = ['a','z','A','Z']
spam.sort()
print (spam)
# ['A', 'Z', 'a', 'z']
# Sorting happens in ASCII-BETICAL order

# To sort normally
spam.sort(key=str.lower)
print (spam)
# ['A', 'a', 'Z', 'z']






