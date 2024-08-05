import json

# describe as a dictionary but in a string expression ('')

# this is a dictionary
# person_dictionary = {"name": "Boo", "languages": ["English", "German"]}
# this is a json
person_string = '{"name": "Boo", "languages": ["English", "German"]}'
print(type(person_string))  # <class 'str'>

person_dict = {"name": "Jerry", "languages": ["English", "German"]}

# JSON string to Dict
result = json.loads(person_string)  # <class 'dict'>
print(type(result))
print(result["name"])
print(result["languages"])

print("*" * 30)
'''
#reading json data from .json file
with open("person.json") as f:
    data = json.load(f)
    print(data["name"])
    print(data["languages"])
'''

# convertion Dict to JSON
result1 = json.dumps(person_dict)
print(result1)
print(type(result1))

with open("person.json", "w", encoding="utf-8") as file:
    json.dump(person_dict, file)

person_dict = json.loads(person_string)
result2 = json.dumps(person_dict, indent=5, sort_keys=True)
print(result2)  # prints json format on console
print(person_dict)
