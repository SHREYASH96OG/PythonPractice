import hashlib
ip=input("enter plan text ,output is:-")
hash_object = hashlib.sha1(b'ip')
hex_dig = hash_object.hexdigest()
print(hex_dig) 
