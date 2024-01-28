import re, pyperclip
# Create a regex for phone numbers
phoneregex = re.compile(r'''
# 415-555-0000. 555-0000. (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345                        
                        (((\d\d\d)|(\(\d\d\d\)))?      # area code(optional)
                        (\s|-)     # first seperator
                        \d\d\d    # first 3 digits
                        -          # seperator
                        \d\d\d\d # last 4 digits
                        \s?   # seperator
                        (((ext(\.)?\s)|x)  # extention word part(optional)
                        (\d{2,5}))?)    # extention number part(optional)
                        ''',re.VERBOSE)

# Create a regex for email addresses
# pattern will be something@something.com
emailregex = re.compile(r'''
                        [a-zA-Z0-9._+]+   #name
                        @  # @ symbol
                        [a-zA-Z0-9._+]+  # domain name part
                        ''',re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract email and phone number from this text
extractedPhone = phoneregex.findall(text)
extractedEmail = emailregex.findall(text)

allPhonenumbers = []
for phonenumber in extractedPhone:
    allPhonenumbers.append(phonenumber[0])

results = '\n'.join(allPhonenumbers) + '\n' + '\n'.join(extractedEmail)
print(results)
