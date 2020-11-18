import requests
import json


# https://api.nasa.gov/
# https://api.nasa.gov/insight_weather/?api_key=aOEcG6KeOBOiVl1tgZ8QUmOosyASerPMcZVTb50y&feedtype=json&ver=1.0
# https://api.nasa.gov/assets/insight/InSight%20Weather%20API%20Documentation.pdf
url = 'http://api.citybik.es/v2/networks?fields=stations'
response = requests.get(url)
data = response.json()

print(data)