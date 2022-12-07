# Requires the requests module to be installed.
import requests

# The parameters needed to retrieve 10 boolean questions from the tech category.
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

# Retrieves the data from the open trivia database and stores it in a json file.
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

# Retrieves the required information and stores it as a variable.
question_data = data["results"]
