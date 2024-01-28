import pprint
message = 'It is a bright day and we are just starting up our work'
count = {}

for character in message.upper():
    count.setdefault(character,0)
    count[character] = count[character]+1

pprint.pprint(count)

