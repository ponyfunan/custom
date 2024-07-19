students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"

choice = input("Input here the magic word... ")
if (choice == "Duck"):
    print("Quack! Quack!")
elif (not choice):
    print("Empty.....meh...")
else:
    print("It's True!!! Congrats!")

bullshit = "one" if (rating > 4.5) else "zero"
print(bullshit)


#exercise
first_name = "John"
last_name = "Smith"
age = 20
is_new = True
print("Hello " + first_name + " " + last_name)


#2
first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Sum: " + str(sum))

#testing some cool stuff
course = "Python for Beginners"
print(course.upper())
print(course)
print(course.lower())
print(course)
print(course.find('y'))
print(course.replace('for', '4'))
print('Python' in course)

del bullshit
assert course is not None, f"{course} doesn't exist!"
current_list = [1,2,3,4,5]
print(list(map(lambda x: x * x, current_list)))

try:
    result: float = 1_000_000 / 0
except ZeroDivisionError:
    print('Go home Bob, you\'re drunk...')

weather: tuple[str, int] = 'rain', 6

match weather:
    case 'rain', severity if severity > 5:
        print(f"Very hard rain! ({severity})")
    case 'cloud', severity:
        print(f"CloudCream, anyone? ({severity})")
    case _:
        print("Unknown weather, damn you global warming!")

type LoL = str | int
var: LoL = 10
