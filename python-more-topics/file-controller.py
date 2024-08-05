"""
for opening a file: open()
writing on a file: write()
append a file: append()
create a file: create()
read: read()
"""

file = open("newfile.txt", "w", encoding='utf-8')  # it will create a text file
# file = open("newfile.txt", "w", encoding='utf-8')  # "w" creates this file for every execution from base
# open("newfile.txt", "r")
file.write("Hello world!\n")
file.close()

file = open("newfile.txt", "r", encoding='utf-8')
# we can read the file with for loop
for i in file:
    print(i, end=" ")

file.close()

print("*" * 30)

#  don't need to file.close() at the end of line.(works like a method and close file itself)
with open("newfile.txt", "r", encoding='utf-8') as file:
    contentInFile = file.read()
    print(contentInFile)
    print(file.tell())  # gives cursor's current stream position as int
    # print(file.readline())
    file.seek(3)  # starts from 3 and prints rest of the text out
    content2 = file.read()
    print(content2)

    print("*" * 30)

#  'r+' gives a permission for reading and writing
with open("newfile.txt", "r+", encoding='utf-8') as file:
    print(file.read())
    file.write("Hello everyone!")
    file.seek(0)
    content = file.read()
    print(content)

print("*" * 30)

# updating at the end of the page
with open("newfile.txt", "a", encoding='utf-8') as file:
    file.write("\nImportant Infos")

with open("newfile.txt", "r", encoding='utf-8') as file:
    print(file.read())

print("*" * 30)

# updating at the start of the page
with open("newfile.txt", "r+", encoding='utf-8') as file:
    content3 = file.read()
    content3 = "I want to say Hello\n" + content3
    file.seek(0)
    file.write(content3)

with open("newfile.txt", "r", encoding='utf-8') as file:
    print(file.read())

print("*" * 30)

# updating at the middle of the page
with open("newfile.txt", "r+", encoding='utf-8') as file:
    listFile = file.readlines()
    listFile.insert(2, "Inserting is happening right now..\n")
    file.seek(0)
    file.writelines(listFile)

with open("newfile.txt", "r", encoding='utf-8') as file:
    print(file.read())




