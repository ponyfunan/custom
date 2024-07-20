names: list[str] = ['mamma', 'mia', '!!!']
print(names[0])
print(names[1])
#print(names[20]) doesn't work
print(names[-1])
print(names[-2])
#print(names[-1000]) doesn't work too, saaaad
print(names[0:1])
print(names[0:2])
print(names[0:3]) #right edge is not included

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
numbers.insert(0, 0)
print(numbers)
numbers.remove(3)
print(numbers)
print(1 in numbers)
numbers.clear()
print(numbers)
numbers = [1, 2, [1, 2, 3], 4, 5]
print(numbers)
print(len(numbers))
numbers.clear()

numbers = range(5, 10, 2) 
print(numbers)
for number in numbers:
    print(number) #5, 7, 9
for i in range(5,10,2):
    print(i)

lol = 'Hello'
print(lol[0:2]) #He