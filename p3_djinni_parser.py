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
base_url = "https://djinni.co"
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
for i in range(1,15):
    smart_sleep()
    url = f"https://djinni.co/jobs/?all_keywords=Data+Analyst&search_type=basic-search&page={i}"
    response = requests.get(url,headers=headers)

    soup = BeautifulSoup(response.text,"lxml")

    data = soup.find_all("div", class_="d-flex flex-column gap-1")

    for i in data:
        a = i.find("a")
        if a and a.get("href"):
            list_card_url.append(urljoin(base_url, a["href"]))
# print(data)
# print(response.status_code)
# print(response.text[:1000])


def djinni_parser():
    for card_url in list_card_url:

        smart_sleep()

        response = requests.get(card_url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("div", class_="wrapper")
        if data is None:
            continue
        name = data.find("h1", class_="m-0 mb-1 fs-2").text.strip()
        source = "Djinni"
        domain = data.find("h1", class_="m-0 mb-1 fs-2").text.strip()

        years_of_experience_text = data.find("strong", class_="font-weight-600 capitalize-first-letter")
        if years_of_experience_text:
            match = re.search(r"\d+", years_of_experience_text.text)
            if match:
                years_of_experience = int(match.group())
            else:
                years_of_experience = None  # або 0
        else:
            years_of_experience = None

        salary = "1000$"

        work_arrangement = data.find("strong", class_="d-block font-weight-600").text
        location = data.find("span", class_="location-text").text

        english_tag = data.find(
            lambda tag: tag.name == "strong"
                        and {"font-weight-600", "capitalize-first-letter"}.issubset(tag.get("class", []))
                        and "english" in tag.get_text(strip=True).lower()
        )
        english_level = english_tag.get_text(strip=True) if english_tag else ""

        skills_description = data.find("div", class_="mb-4 job-post__description")
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

        # print(name, source, years_of_experience, salary, work_arrangement, location, skills, job_url)
        yield name, source, years_of_experience, salary, work_arrangement, location, english_level, skills, job_url
