import pandas as pd  # análise de dados e manipulação
import requests as requests  # conexões de rede
from bs4 import BeautifulSoup  # extrair os dados de documentos HTML e XML


def fetch_page_from_url(url: str):
    response = requests.get(url)

    return response


page = fetch_page_from_url(
    "https://ranielcsar.github.io/"
)
beautifulsoup = BeautifulSoup(page.text, "html.parser")
skills = []

for skill in beautifulsoup.find_all("section", {"class": "skills"}):
    skills.append(skill.text)

raw_data = {"skills": skills}

dataframe = pd.DataFrame(raw_data, columns=["skills"])
dataframe.to_csv("raw_data.csv", index=False)
print(dataframe)
