import requests


base_url = 'http://localhost:8000'
end_url = '/api/search/'

endpoint = base_url + end_url #+ "?q=phone/"

req = requests.get(endpoint, params={'q': 'phone'})

print(req.status_code, req.json())