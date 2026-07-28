import requests

url = "https://viacep.com.br/ws/53401435/json/"

resposta = requests.get(url, timeout=10)
print("status:", resposta.status_code)
print("json", resposta.json())

url = "https://viacep.com.br/ws/00000000/json/"

resposta = requests.get(url, timeout=10)
print("status:", resposta.status_code)
print("json", resposta.json())

url = "https://viacep.com.br/ws/abc/json/"

resposta = requests.get(url, timeout=10)
print("status:", resposta.status_code)
print("texto da resposta:", resposta.text)

import requests

def consultar_cep(cep: str) -> dict | None:
"""Consulta um CEP no ViaCEP. Devolve dict, ou None se falhar."""
url = f"https://viacep.com.br/ws/{cep}/json/"
try:
resposta = requests.get(url, timeout=10)      # cinto 1
resposta.raise_for_status()         
          # 
except requests.exceptions.Timeout:               
cinto 2
# cinto 3...
print(f"[erro] ViaCEP demorou demais (cep={cep})")
return None
except requests.exceptions.ConnectionError:
print("[erro] Sem conexao ou servidor fora do ar")
return None
except requests.exceptions.HTTPError as erro:
print(f"[erro] HTTP {resposta.status_code}: {erro}")
return None
dados = resposta.json()
if dados.get("erro"):        
# a pegadinha do 200!
print(f"[aviso] CEP {cep} nao existe")
return None
return dados
if __name__ == "__main__":
for cep in ["52050480", "00000000", "01310100"]:
endereco = consultar_cep(cep)
if endereco:
print(cep, endereco["logradouro"], endereco["bairro"])