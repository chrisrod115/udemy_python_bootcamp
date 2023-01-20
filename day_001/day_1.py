"""print("hello world")
"""

a = input("a: ")
b = input("b: ")

a_storage = a
a = b 
b = a_storage

print("a = " + a)
print("b = " + b)