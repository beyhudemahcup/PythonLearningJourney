website = "https://www.google.com"
course = "Google: A search engine for everyone"
name, surname, age, job = 'Dummy', 'Stunt', 35, 'actor'

'''
1- how many characters in 'course'
2- take www characters in 'website'
3- take com characters in 'website'
4- take first and last 15 characters in 'course'
5- print starts with the last character and end with the first characters in 'course'
6- my name is Dummy Stunt, I am 35 and I am an actor
7- change w with the W in a sentence of 'Hello world!'
8- print abc together for three times
'''
# 1
print(len(course))
# 2
print(website[8:11])
# 3
print(website[len(website)-3:len(website)])
# 4
first15 = course[:15]
last15 = course[15:]
print(first15)
print(last15)
# 5
print(course[::-1])
# 6
print(f"my name is {name} {surname}, I am {age} and I am an {job}")
# 7
text = "Hello world!"
print(text.replace('w', 'W'))
# 8
abc = 'abc'
print(abc * 3)

