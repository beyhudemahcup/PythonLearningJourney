import requests

github_token = " "


class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = github_token
        self.json_payload = {
            "description": "This is my repository created with API",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }

    def getUser(self, username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()

    def getRepositories(self, username):
        response = requests.get(self.api_url + "/users/" + username + '/repos')
        return response.json()

    def createRepository(self, repo_name):
        #  I copied the JSON data to avoid changing the instance's data
        payload = self.json_payload.copy()
        payload["name"] = repo_name

        response = requests.post(self.api_url + '/user/repos?access_token=' + self.token, json=payload)
        return response.json()


github = Github()

while True:
    input_user = input(
        "\nPlease select an option by entering the corresponding number:\n\n1-Find User\n2-Get Repositories\n3-Create Repository\n4-Exit\n->")

    if input_user == '4':
        break

    else:
        if input_user == '1':
            username_input = input("username: ")
            result = github.getUser(username_input)
            print(
                f"name: {result['name']}, public repositories: {result['public_repos']}, followers: {result['followers']}, bio: {result['bio']}")

        elif input_user == '2':
            username_input = input("username: ")
            result = github.getRepositories(username_input)
            # orders alphabetically
            result.sort(key=lambda repo: repo['name'])

            for repo in result:
                print(repo['name'])

        elif input_user == '3':
            repository_input = input("repository name: ")
            result = github.createRepository(repository_input)
            print(result)
        else:
            print("Invalid entry!")
