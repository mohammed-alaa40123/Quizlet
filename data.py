import requests
from home import Home

home = Home()
category = home.category

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": category
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
