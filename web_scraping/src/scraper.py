import pandas as pd  # análise de dados e manipulação
import requests as requests  # conexões de rede
from bs4 import BeautifulSoup  # extrair os dados de documentos HTML e XML


def fetchPageFromUrl(url: str):
    response = requests.get(url)

    return response


page = fetchPageFromUrl(
    "https://raw.githubusercontent.com/ranielcsar/hotline-pix/master/src/utils/formatPhoneNumber.js?token=GHSAT0AAAAAACHQZ4IASU2CT6GKUTQKTOLSZJEP44Q"
)
beautifulsoup = BeautifulSoup(page.text, "html.parser")
skills = []

for skill in beautifulsoup.find_all("section", {"class": "skills"}):
    skills.append(skill.text)

raw_data = {"skills": skills}

dataframe = pd.DataFrame(raw_data, columns=["skills"])
dataframe.to_csv("raw_data.csv", index=False)
print(dataframe)
