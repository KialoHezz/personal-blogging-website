import requests
from .models import Qoutes
import json


response = requests.get("http://quotes.stormconsultancy.co.uk/random.json")

print(response.json())