import requests

class Planeta:
    def __init__(self, nome, distancia_media):
        self.nome = nome
        self.distancia_media = distancia_media

    def calcular_distancia_em_dias(self):
        try:
            distancia_km = float(
                self.distancia_media) * 149597870.7  # 1 UA = 149.597.870,7 km
            velocidade_luz_km_dia = 299792458 / 86400
            distancia_dias = distancia_km / velocidade_luz_km_dia / 365
            return distancia_dias
        except ValueError:
            print(
                "Erro: a distância média deve ser um número com separador decimal ',' ou '.'")
            return None


url = "https://api.le-systeme-solaire.net/rest/bodies/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    planetas = []
    for planeta in data["bodies"]:
        if "semimajorAxis" in planeta:
            planetas.append(
                Planeta(planeta["name"], planeta["semimajorAxis"]))
        else:
            print(
                f"A distância média para {planeta['name']} não está disponível.")
    print("Lista de planetas:")
    for planeta in planetas:
        print(planeta.nome)
    while True:
        escolha = input(
            "Digite o nome de um planeta (ou 'sair' para encerrar o programa): ")
        if escolha.lower() == "sair":
            break
        planeta_encontrado = False
        for planeta in planetas:
            if escolha.lower() == planeta.nome.lower():
                distancia_dias = planeta.calcular_distancia_em_dias()
                if distancia_dias is not None:
                    print(
                        f"Distância da Terra para {planeta.nome}: {distancia_dias:.2f} dias")
                planeta_encontrado = True
                break
        if not planeta_encontrado:
            print("Planeta não encontrado")
else:
    print("Erro ao acessar a API")

print("Opções de planetas:")
for i, planeta in enumerate(data["bodies"]):
    if "name" in planeta:
        print(f"{i+1}. {planeta['name']}")
print()