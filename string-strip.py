text = "    Python is awesome   "
stripped_text = text.strip()
print("Stripped text: ", stripped_text)
# Stripped text:  Python is awesome

new_text = "****Python is awesome*****"
new_stripped_text = new_text.lstrip('*')
print("Stripped text: ", new_stripped_text)
# Stripped text:  Python is awesome*****

right_stripped_text = new_text.rstrip('*')
print("Stripped text: ", right_stripped_text)
# Stripped text:  ****Python is awesome