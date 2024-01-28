count = {}
user_resp = input("Enter the value(top-L/top-M/top-R/M-L/M-M/M-R/B-L/B-M/B-R)")
count.setdefault(user_resp,'0')
print (count)
print(type(count))