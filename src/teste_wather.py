import requests

url = "https://api.openweathermap.org/data/2.5/weather"
resposta = requests.get(url, params={"q": "Recife,BR"}, timeout=10)
print(resposta.status_code)   # 401!
print(resposta.text)