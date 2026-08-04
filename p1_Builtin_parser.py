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
base_url = "https://builtin.com/"
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

for i in range(1,5):
    smart_sleep()
    url = f"https://builtin.com/jobs?search=Data+Analyst&country=POL&allLocations=true&page={i}"
    # url = f"https://builtin.com/jobs?search=Data+Analyst&country=USA&allLocations=true&page={i}"
    # url = f"https://builtin.com/jobs/remote/hybrid/office?search=Data+Analyst&country=DEU&allLocations=true&page={i}"

    response = requests.get(url,headers=headers)

    soup = BeautifulSoup(response.text,"lxml")

    # data = soup.find_all("div", class_="page-section")
    # data = soup.find_all("h2", class_="font-normal text-base md:text-lg mr-2 mt-0")
    data = soup.find_all("div", class_="row")

    for i in data:
        for a in i.find_all("a", href=True):
            href = a["href"]
            if "/job/" in href.lower():
                list_card_url.append(urljoin(base_url, href))
# b = len(list_card_url)
# print(b)
# print(list_card_url)
# print(data)
# print(response.status_code)
# print(response.text[:1000])


def Builtin_parser():
    for card_url in list_card_url:

        smart_sleep()

        response = requests.get(card_url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("div", class_="job-post-item bg-gray-01")
        if data is None:
            continue

        name = data.find("h1",
                         class_="fw-extrabold fs-xl mb-sm").text.strip()

        source = "Builtin"

        job_text = data.get_text(" ", strip=True)

        match = re.search(
            r'(\d+)\s*\+?\s*years?',
            job_text,
            re.IGNORECASE
        )
        if match:
            years_of_experience = int(match.group(1))
        else:
            years_of_experience = None

        salary_tag = data.find("span", class_="font-barlow text-gray-03", string=lambda text: text and "K" in text)
        if salary_tag:
            salary = salary_tag.text.strip()
        else:
            salary_match = re.search(
                r'([$€£]|USD|EUR|PLN)\s*[\d\s,]+(?:\s*[-–]\s*(?:[$€£]|USD|EUR|PLN)?\s*[\d\s,]+)?',
                job_text,
                re.IGNORECASE
            )
            if salary_match:
                salary = salary_match.group(0)
            else:
                salary = None

        work_blocks = data.find_all("div", class_="d-flex align-items-start gap-sm")
        if len(work_blocks) > 1:
            work_arrangement = work_blocks[1].get_text(strip=True)
        else:
            work_arrangement = None

        location = "Poland"
        # location = "US"
        # location = "Germany"

        job_text_eng = data.get_text(" ", strip=True)

        match_eng = re.search(r'\b(A1|A2|B1|B2|C1|C2)\b', job_text_eng, re.IGNORECASE)
        if match_eng:
            english_level = match_eng.group(1).upper()
        else:
            english_level = None

        if not data:
            continue
        elements = data.find_all(["p", "ul", "li"])
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


        # print(name, years_of_experience,salary, work_arrangement, location,english_level, skills, job_url)
        yield name, source, years_of_experience, salary, work_arrangement, location, english_level, skills, job_url

