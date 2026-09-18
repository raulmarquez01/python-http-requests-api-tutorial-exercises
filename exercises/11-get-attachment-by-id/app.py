import requests

def get_attachment_by_id(attachment_id):
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    data = response.json()
    for post in data["posts"]:
        for attachment in post["attachments"]:
            if attachment["id"] == attachment_id:
                return attachment["title"]
    return None

print(get_attachment_by_id(137))
