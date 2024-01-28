# Regular expression to find the phone number from a message
import re
message = " Call me 415-555-1011 or at 565-788-9011 tomorrow"
phoneregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneregex.search(message)
print(mo.group())

#415-555-1011
#Above code displayed only the first occurence of the pattern
# If you want to match all the patterns, then findall() method should be used.

mo1 = phoneregex.findall(message)
print(mo1)
# ['415-555-1011', '565-788-9011']
# If we use groups in the regular expression pattern, findall() method will return the output in tuples.
regex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
matchobject = regex.findall(message)
print(matchobject)
# [('415-555-1011', '415', '555-1011'), ('565-788-9011', '565', '788-9011')]

#pipes
message1 = "Batmobile lost a wheel"
piperegex = re.compile(r'Bat(man|cat|dog|mobile)')
mo2 = piperegex.search(message1)
print(mo2.group())
# Batmobile
mo3 = piperegex.search("Bat motorcycle lost a wheel")
# Here mo3 value will be "None", as there is no matching pattern
print(mo3)
# None

# ? character - matches zero or 1 occurence
message2 = "The Adventures of Batman"
charregex = re.compile(r'Bat(wo)?man')
mo4 = charregex.search(message2)
print(mo4.group())
# Batman

message3 = "The Adventures of Batwowowoman"
charregex1 = re.compile(r'Bat(wo)?man')
mo5 = charregex1.search(message3)
print(mo5)
# None

message4 = "My phone number is 555-7777.Call me tomorrow"
phoneregex1 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo6 = phoneregex1.search(message4)
print(mo6.group())
# 555-7777

# If you want to search for a pattern 'dinner?', then use
# re.compile(r'dinner\?')

# * Character - Matches zero or more character
message5 = "The Adventures of Batmamamaman"
charregex2 = re.compile(r'Bat(ma|wo)*man')
mo7 = charregex2.search(message5)
print(mo7.group())
# Batmamamaman

# + Character - One or more character
message6 = "The Adventures of Batman"
charregex3 = re.compile(r'Bat(wo)+man')
mo8 = charregex3.search(message6)
print(mo8)
# None

# Escaping ?,*,+
# regex = re.compile(r'\?\*\+')

# {x} - Exact Matches
message7 = "He said hahahaha"
haregex = re.compile(r'(ha){2}')
mo9 = haregex.search(message7)
print(mo9.group())
# haha

message8 = "Call me on 415-515-1234,555-7777,238-453-5477,243-466-987"
phoneregex2 = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo10 = phoneregex2.search(message8)
print(mo10.group())
# 415-515-1234,555-7777,238-453-5477,

# {x,y} - Range of repetitions, Atleast x times, max y times
message9 = "He said hahahahahahaha"
haregex1 = re.compile(r'(ha){3,5}')
mo11 = haregex1.search(message9)
print(mo11.group())
# hahahahaha
# Here it displayed 'ha' 5 times, i.e the maximum value provided in the regex. This is called greedy matching.

# For non-greedy matching i.e to show only the minimum occurence as per the value provided in regex, check below code
message10 = "He said hahahahaha"
haregex2 = re.compile(r'(ha){3,5}?')
mo12 = haregex2.search(message10)
print(mo12.group())
# hahaha

# Character class
# \d --> digit
# \D --> Non numeric digit from 0 to 9
# \w --> Any letter, numeric digit or the underscore character
# \W --> Anything other than letter, numeric digit or underscore character
# \s --> Any space,tab or newline character
# \S --> Any character that is not a space,tab or newline

# Make your own character class
message11 = "Robocop eats baby food"
vowelregex = re.compile(r'[aeiouAEIOU]')
#you can also use re.compile(r'[aeiou]',re.I) # re.I --> Ignore case
mo13 = vowelregex.findall(message11)
print(mo13)
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']

doublevowelregex = re.compile(r'[aeiouAEIOU]{2}')
mo14 = doublevowelregex.findall(message11)
print(mo14)
# ['ea', 'oo']

# Negative character class - ^ prints everything other than what is in square brackets
consonantregex = re.compile(r'[^aeiouAEIOU]')
mo15 = consonantregex.findall(message11)
print(mo15)
# ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd']

# caret ^ can also be used to match the pattern at the start of the string
message12 = "Hello World!"
helloregex = re.compile(r'^Hello')
mo16 = helloregex.findall(message12)
print(mo16)
# ['Hello']

# Dollar $ can be used to match the pattern at the end of the string
endregex = re.compile(r'World!')
mo17 = endregex.findall(message12)
print(mo17)
# ['World!']

# Dot . character --> Matches any character except new line
message13 = "The cat in the hat sat on the flat mat"
dotregex = re.compile(r'.at')
mo18 = dotregex.findall(message13)
print(mo18)
# ['cat', 'hat', 'sat', 'lat', 'mat']
# Here it displayed words which have one character before 'at'

dotregex1 = re.compile(r'.{1,2}at')
mo19 = dotregex1.findall(message13)
print(mo19)
# [' cat', ' hat', ' sat', 'flat', ' mat']
# Here it displayed words which have 2 characters before 'at'

# .* --> Match anything
message14 = "Details of the employee,First Name: Sreejith,Last Name: Sreekumar"
dotstarregex = re.compile(r'First Name: (.*),Last Name: (.*)')
mo19 = dotstarregex.findall(message14)
print(mo19)

# .* always do greedy matches
# For non-greedy matches, see below code
message15 = "<To Serve humans> for dinner.>"
dotstarregex1 = re.compile(r'<(.*?)>')
mo20 = dotstarregex1.findall(message15)
print(mo20)
# ['To Serve humans']

# sub() method - Find and substitute
message16 = "Agent Alice gave the secret documents to Agent Bob"
namesregex = re.compile(r'Agent \w+')
mo21 = namesregex.sub('REDACTED',message16)
print(mo21)
# REDACTED gave the secret documents to REDACTED

names1regex = re.compile(r'Agent (\w)\w*')
mo22 = names1regex.findall(message16)
print(mo22)
mo23 = names1regex.sub(r'Agent \1****',message16)
print(mo23)
#Agent A**** gave the secret documents to Agent B****

# Verbose mode - Make the regular expression in a readable format
message17 = " Call me 415-555-1011 or at 565-788-9011 tomorrow"
phoneregex3 = re.compile(r'''
                         \d\d\d
                         -\d\d\d
                         -\d\d\d\d''',re.VERBOSE)
mo = phoneregex3.search(message17)
print(mo.group())
#415-555-1011







