# range() method can be used like for(int i = 0; i < 100; i++)
for item in range(10, 500, 30):  # starts in 10, keeps increasing until 500, it increases 30 by 30
    print(item)

# boom game (you will get boom if you say 5 or multiples of 5
for item in range(0, 100, 1):
    if item % 5:
        print(item)
    else:
        print('boom!')

# enumerate returns tuple that includes index and element at the same time
greeting = "Hello, My Friend!"
for index, letter in enumerate(greeting):  # works
    print(f"intex: {index}, letter: {letter}")

# zip combine different lists and make them like dictionary
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
listcombined = list(zip(list1, list2))  # casting to list!
print(listcombined)
list3 = [11, 22, 33, 44, 55]
for item in zip(listcombined, list3):
    print(item)
