characters = str(input())

print(any(char.isalnum()  for char in characters))
print(any(char.isalpha() for char in characters))
print(any(char.isdigit() for char in characters))
print(any(char.islower() for char in characters))
print(any(char.isupper() for char in characters))

'''for char in characters'''
#for char in S:
#    print(char.isalnum())

'''any()'''
# The any() function returns True if at least one element in the input 
# iterable is True. Otherwise, it returns False.