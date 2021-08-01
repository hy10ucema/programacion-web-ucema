a = "Hello"
print(a)

# Strings son Arrays

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

# Concatenación
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Métodos
# https://www.w3schools.com/python/python_strings_methods.asp

a = "Hello, World!"
print(len(a))

a = "Hello, World!"
print(a.upper())

# Método Format 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

