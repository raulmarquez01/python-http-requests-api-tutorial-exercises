import requests

def get_post_tags(post_id):
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    data = response.json()
    for post in data["posts"]:
        if post["id"] == post_id:
            return post["tags"]
    return None

print(get_post_tags(146))
