x = 0

while x <= 100:
    if x % 2 == 1:
        print(f"{x} is a odd number!")
    else:
        print(f"{x} is a even number!")
    x += 1

name = ''  # False
while not name.strip(): # strip cuts empty lines
    name = input("please enter your name")
print(f"Hello {name}!")

y = 0
while y < 5:
    if y == 4:
        break  # It breaks when if case is true
    elif y == 2:
        y += 1
        continue  # it continues in if block
    print(y)
    y += 1

# sum all the numbers until it gets 100

i = 0
sumnumber = 0
while i <= 100:
    sumnumber += i
    i += 1
print(f"your summary is {sumnumber}")

