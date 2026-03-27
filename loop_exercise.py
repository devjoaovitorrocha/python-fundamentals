largest = None
smallest = None
numbers = []

while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        numbers.append(int(num))
    except ValueError:
        print("Invalid input")
        continue

for n in numbers:
    if largest is None or n > largest:
        largest = n
    if smallest is None or n < smallest:
        smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)
