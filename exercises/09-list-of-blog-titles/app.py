import requests

def get_titles():
    titles = []
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    data = response.json()
    for post in data["posts"]:
        titles.append(post["title"])
    return titles

print(get_titles())
