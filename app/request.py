import requests


response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")

console.log(response.status_code)