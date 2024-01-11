import json
import requests
import pprint
request = requests.get("https://opentdb.com/api.php?amount=1")
response = request.status_code
Text = request.text
Header = request.headers
read = json.loads(request.text)
pprint.pprint(read)
type(read)
print(read['results'][0]['correct_answer'])