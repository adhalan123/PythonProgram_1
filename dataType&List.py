a, b, c = 5, "Aaru", 9

print(a, b)

print("{},{}".format(a, b))

print(type(a))
print(type(b))
print(type(c))
print(b, "Hi am println string", b)

value = [1, 3, 4, "dhalange"]

print(value)

print(value[3])

print(value[-1])
print(value[0])
# print value in one range last index value will exclude
print(value[1:3])
#to print value from one rage to end
print(value[1:])
#to print value with space instaed of comma

print(*value[1:])

# to print values in seperate line

for i in (value[1:]):
    print(i)

# inser values to list

#insert value at end of list

value.append("anil")

print(value)

#insert value after any specific index

value.insert(1, "Mahi")

print(value)

value[0]="janne"

print(value)

