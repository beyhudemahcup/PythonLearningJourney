import requests
import json

# gives response 200
result = requests.get("https://jsonplaceholder.typicode.com/todos")

# returns whole html code
resultText = result.text

result = json.loads(resultText)

# delectus aut autem
print(result[0]["title"])

# we can set our limitations while getting data from website
for i in result:
    if i["userId"] == 3:
        print(i)


