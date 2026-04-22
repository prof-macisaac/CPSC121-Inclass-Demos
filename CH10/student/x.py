y = ["1", "two", "3"]

total = 0

for item in y:
    try:
        total += float(item)
    except ValueError:
        print("error")

print(total)