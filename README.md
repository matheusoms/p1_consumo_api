# Primeira Avaliação Dev Web III: Consumo de API

## Para esta avaliação, iremos realizar os seguintes requisitos:

```
  1. Realizar a conexão com uma API de acesso público.
  2. Realizar a configuração de retorno de possíveis erros desta conexão (ex: error 404, 402, 505, etc).
  3. Realizar consultas a partir de um endpoint disponibilizado pela api.
  4. Transformar os dados do retorno do endpoint em um .Json.
  5. Tratar os dados para trazer informações concisas e com nexo.
```

## A API que irei utilizar para este projeto é: Weatherstack API

Com ela poderemos realizar consultas de diferentes condições climáticas de diversos locais. Como por exemplo:

Retornando clima de São Paulo-SP:

```
"Nome da Cidade: São Paulo
País: Brazil
Hora Local: 2019-09-07 08:14
Temperatura Atual: 24
Descrição do Clima: Ensolarado
Humidade: 15
Visibilidade: 12"

```

Para acessar a página da API basta clicar em [Weatherstack](https://weatherstack.com/).
Para acessar a documentação da API acesse [Documentação WeatherStack](https://weatherstack.com/documentation).


# Seguem as instruções de como utilizar o código:

### Instalando o Python

  Primeiro, precisamos ter o Python instalado na máquina, basta acessar o link [Download Python](https://www.python.org/downloads/) e clicar no botão "Download Python 3.11.5" e seguir as instruções de instalação.

### Instalando o PIP

  Para instalar os pacotes necessários iremos utilizar o gerenciador de pacotes PIP, basta acessar o link [Instalando PIP](https://pip.pypa.io/en/stable/installation/) e seguir as instruções da página.

### Instalando o VENV

  Iremos consumir a API em um ambiente virtal utilizando o pacote venv do Python, para isso, batas acessar o link [Instalando VENV](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) e seguir as instruções da página.

### Iniciando o VENV

  Para iniciar, basta seguir as instruções de uso do venv no link [Ambiente Virtual em Python](https://www.alura.com.br/artigos/ambientes-virtuais-em-python?utm_term=&utm_campaign=%5BSearch%5D+%5BPerformance%5D+-+Dynamic+Search+Ads+-+Artigos+e+Conte%C3%BAdos&utm_source=adwords&utm_medium=ppc&hsa_acc=7964138385&hsa_cam=11384329873&hsa_grp=111087461203&hsa_ad=673330887061&hsa_src=g&hsa_tgt=aud-396128415587:dsa-843358956400&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAjwu4WoBhBkEiwAojNdXq-sTsmnqxAzWNy6lySFkyQOzMaKb2TlKNepAKjt9UbTzVdNphMRIRoCWBUQAvD_BwE)

## Pronto, usa máquina está configurada. Agora é só iniciar o script e visualizar o retorno das consultas.

> Os requisitos necessários para rodar os scripts estão no arquivo requirements.txt neste repositório
