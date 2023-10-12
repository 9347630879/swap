# swap 2 numbers  without temp variables

a = 4
b = 6
a =  a + b
b = a - b
a = a- b
print(a,b)

a = 4
b = 6
a =  a * b
b = a + b
a = a- b
print(a,b)

a = 4
b = 6
a =  a + b
b = a / b
a = a- b
print(a,b)


# swap 2 numbers  with temp variables

a = 5
b = 3
temp = a
a = b
b = temp
print(a,b)

#fibonacci  series

n = 100
a = 0
b = 1
i = 2
while i < n:
    print(b)
    a = a + b
    b = a - b
    i = i + 1
