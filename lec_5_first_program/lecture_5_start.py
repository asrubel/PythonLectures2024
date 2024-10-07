a = 10240000000000000000
b = 10240000000000000000

print(a)
print(type(a))
print(id(a))

print(b)
print(type(b))
print(id(b))

a = 1000
print(a)
print(id(a))

a = a + 1000
print(a)
print(id(a))

a = True
print(a)
print(id(a))

my_str = "Python"
another_str = "Python"
print(id(my_str))
print(id(another_str))

my_str = my_str + " 3.11"
print(id(my_str))

print(my_str[3])
# Error with immutable string
# my_str[3] = "$"

# a = 40
a = int(input("Enter the number: "))
b = 2

if a <= 10:
    a = a + 100
    if b > 3:
        a += b
        # a = a + b

elif a <= 20:
    a += 200

elif a <= 30:
    a += 300

else:
    a -= 1000
    if b < 3:
        a *= b


print(a)
print(b)
