import requests
from bs4 import BeautifulSoup
import  time
import random
from urllib.parse import urljoin
import xlsxwriter
import re
import json
import pandas as pd


session = requests.Session()
def smart_sleep():
    time.sleep(random.uniform(2.5, 4.0))

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
list_card_url = []
base_url = ""
SKILLS = {
    "Python": r"\bpython\s*\d*\b",
    "SQL": r"\b(sql|postgresql|mysql|t-sql|pl/sql)\b",
    "Power BI": r"power\s*bi",
    "Excel": r"\bexcel\b",
    "AWS": r"\baws\b|amazon web services",
    "AI": r"\b(ai|artificial intelligence|generative ai|genai|llm)\b",
    "A/B Testing": r"\ba/?b\s*test(ing)?\b|\bsplit\s*test(ing)?\b",
    "UX/UI": r"\b(ux/ui|ux|ui)\b",
    "Looker Studio": r"\blooker(\s*studio)?\b",
    "Microsoft Office": r"\bmicrosoft office\b|\bms office\b|\boffice 365\b",
    "Amplitude": r"\bamplitude\b",
    "Firebase": r"\bfirebase\b",
    "Power Query": r"power\s*query",
    "Pandas": r"\bpandas\b",
    "Jupyter": r"\bjupyter\b|\bjupyter notebook\b",
    "API": r"\bapi\b|\brest api\b|\bgraphql\b",
    "Google Sheets": r"google\s*sheets",
    "DAX": r"\bdax\b",
    "Tableau": r"\btableau\b",
    "LookML": r"\blookml\b",
    "BigQuery": r"\bbigquery\b|\bgoogle bigquery\b",
    "Snowflake": r"\bsnowflake\b",
    "Redshift": r"\bredshift\b",
    "ClickHouse": r"\bclickhouse\b",
    "Databricks": r"\bdatabricks\b",
    "NumPy": r"\bnumpy\b",
    "SciPy": r"\bscipy\b",
    "Matplotlib": r"\bmatplotlib\b",
    "Seaborn": r"\bseaborn\b",
    "Scikit-learn": r"\b(scikit-learn|sklearn)\b",
    "ETL": r"\betl\b",
    "ELT": r"\belt\b",
    "Git": r"\bgit\b",
    "GitHub": r"\bgithub\b",
    "GitLab": r"\bgitlab\b",
    "Apache Airflow": r"\bairflow\b|\bapache airflow\b",
    "Spark": r"\bapache spark\b|\bspark\b|\bpyspark\b",
    "PySpark": r"\bpyspark\b",
    "Docker": r"\bdocker\b",
    "KPI": r"\bkpi(s)?\b",
    "Google Analytics": r"\bgoogle analytics\b|\bga4\b",
    "Mixpanel": r"\bmixpanel\b",
    "Metabase": r"\bmetabase\b"
}

session = requests.Session()

session.headers.update(headers)

# for i in range(1,14):
#     smart_sleep()
url = "https://justjoin.it/job-offers/remote?keyword=Data+Analyst"

response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text,"lxml")

data = soup.find_all("div", class_="MuiBox-root mui-1srrdw5")

for i in data:
    a = i.find("a")
    if a and a.get("href"):
        list_card_url.append(urljoin(base_url, a["href"]))


# print(list_card_url)
# b = len(list_card_url)
# print(b)
# print(data)
# print(name)
# print(response.status_code)
# print(response.text[:1000])

def justjoin_1_parser():
    for card_url in list_card_url:

        smart_sleep()

        response = requests.get(card_url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("div", class_="MuiStack-root mui-io6pc6")
        if data is None:
            continue

        name = data.find("h1",
                         class_="mui-1w3djua").text.strip()

        source = "Justjoin.it"

        job_text = data.get_text(" ", strip=True)

        match_exp = re.search(
            r'(\d+)\s*\+?\s*years?',
            job_text,
            re.IGNORECASE
        )
        if match_exp:
            years_of_experience = int(match_exp.group(1))
        else:
            years_of_experience = None

        salary_tag = data.find(
            "div",
            class_="MuiTypography-root MuiTypography-h5 mui-1f21jp8"
        )

        if salary_tag:
            salary = salary_tag.text.strip()
        else:
            salary = None

        match_eng = re.search(r'\b(A1|A2|B1|B2|C1|C2)\b', job_text, re.IGNORECASE)

        if match_eng:
            english_level = match_eng.group(1).upper()
        else:
            english_level = None

        work_arrangement = "Remote"

        location = "Poland"


        skills_description = data.find(
            "div",
            class_="MuiBox-root mui-n1fnon"
        )
        if not skills_description:
            continue
        elements = skills_description.find_all(["p", "ul", "li"])
        if not elements:
            continue
        skill_description_text = " ".join(
            p.get_text(" ", strip=True)
            for p in elements
        )
        search_skills = set()
        for skill, pattern in SKILLS.items():
            if re.search(pattern, skill_description_text, re.IGNORECASE):
                search_skills.add(skill)
        skills = search_skills if search_skills else None

        job_url = card_url


        # print(name, source, years_of_experience, salary, work_arrangement, location, english_level, skills, job_url)
        yield name, source, years_of_experience, salary, work_arrangement, location, english_level, skills, job_url





