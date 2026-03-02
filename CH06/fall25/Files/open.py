file = open(r"Files/names.txt", "r")

# text = file.read()
# print(text)

file_2 = open("dog_names.txt", "a")

for line in file:
    file_2.write(line.rstrip() + "!" + "\n")