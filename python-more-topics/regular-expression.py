import re

result = dir(re)

# regular expression

str = "Klaus Schmidt, the German archaeologist who led the excavations starting in the 1990s, described Göbekli Tepe as “the world’s first temple” due to its religious significance."

# 1
# result = re.findall("Klaus Schmidt", str)
# print(len(result))
# 2
# result = re.split(" ", str)
# 3 (\s means space " ")
# result = re.sub("\s", ",", str)
# 4
# result = re.search("world", str)
# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()  # shows search keyword
# 5
# result = re.findall("[kls]", str)
# result = re.findall("[b-f]", str)
# result = re.findall("[...]", str)
# result = re.findall("[d...]", str)
# result = re.findall("^p", str) #starts with p
# result = re.findall("t$", str)  # ends with d

# there are dozens of different methods for different situations.
print(result)
