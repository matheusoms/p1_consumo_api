import requests

class Planeta:
    def __init__(self, nome, distancia_media_km):
        self.nome = nome
        self.distancia_media_km = distancia_media_km

    def calcular_distancia_em_dias(self):
        try:
            velocidade_luz_km_por_dia = 299792.458 * 86400  # velocidade da luz em km/dia
            distancia_dias = self.distancia_media_km / velocidade_luz_km_por_dia
            return distancia_dias
        except ValueError:
            print("Erro: a distância média deve ser um número.")
            return None
        
url = "https://api.le-systeme-solaire.net/rest/bodies/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    planetas_dict = {}
    for planeta_data in data["bodies"]:
        if "meanRadius" in planeta_data:  # Vamos usar o raio médio já que a API retorna a distância em km
            distancia_media_km = planeta_data["meanRadius"] * 2
            planeta = Planeta(planeta_data["englishName"], distancia_media_km)
            planetas_dict[planeta_data["englishName"].lower()] = planeta
        else:
            print(f"A distância média para {planeta_data['englishName']} não está disponível.")

    print("Opções de planetas e corpos celestes:")
    for nome in planetas_dict.keys():
        print(nome)
    print()

    while True:
        escolha = input("Digite o nome de um planeta (ou 'sair' para encerrar o programa): ").lower()
        if escolha == "sair":
            break
        elif escolha in planetas_dict:
            distancia_dias = planetas_dict[escolha].calcular_distancia_em_dias()
            if distancia_dias is not None:
                print(f"O movimento de translação da {escolha.capitalize()} em volta do sol dura: {distancia_dias:.10f} dias")
        else:
            print("Planeta ou corpo celeste não encontrado")

elif response.status_code == 404:
    print(f"API Not Found. Código de Status: {response.status_code}")

else:
    print(f"Erro ao acessar a API. Código de Status: {response.status_code}")