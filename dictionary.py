mycat = {'size':'fat', 'color':'grey','disposition':'loud'}
print(mycat['size'])
# fat
print(mycat['disposition'])
# loud
print ('My Cat has ' + mycat['color'] + ' fur')
# My Cat has grey fur

#Keys Method
print(mycat.keys())
# dict_keys(['size', 'color', 'disposition'])
print(list(mycat.keys()))
# ['size', 'color', 'disposition']
print(list(mycat.values()))
# ['fat', 'grey', 'loud']
print(list(mycat.items()))
# [('size', 'fat'), ('color', 'grey'), ('disposition', 'loud')]

#for loop
for k in mycat.keys():
    print(k)
#size
#color
#disposition
    
for v in mycat.values():
    print(v)
#fat
#grey
#loud

for k,v in mycat.items():
    print(k,v)
# size fat
# color grey
# disposition loud
    
# get() method - Check if key exists, if key exists returns the value of the key, else return the second value(here 0)
print(mycat.get('color',0))
# grey
print(mycat.get('age',0))
# 0
print(mycat.get('age',''))
# <blank space>
print("My Cat's age is " + mycat.get('age','undefined'))
# My Cat's age is undefined

# Change the value of the key in dictionary
mycat['color'] = 'black'
print(mycat['color'])
#black

# setdefault() method - set default value to key if mentioned key doesnot exist on the dictionary
mycat.setdefault('age','2')
print(mycat['age'])

# Delete key-value 'age' from dictionary
del mycat['age']
print (mycat)
# {'size': 'fat', 'color': 'black', 'disposition': 'loud'}



