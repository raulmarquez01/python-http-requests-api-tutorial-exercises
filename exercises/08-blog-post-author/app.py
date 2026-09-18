import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

data = response.json()

print(data["posts"][0]["author"]["name"])
