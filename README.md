
📌 Custom Web Scraper

Here are Python scripts designed to parse html code of job-posting websites & write down data, ending up with dataset describing Data Analyst vacancies: salary range, years of experience, skills required, work arrangement, etc.

.py files Builtin_parser, djinni_parser, justjoin.it_parser use such libraries as requests, BeautifulSoup, time, etc. to extract relevant data from Data Analyst job postings for further analysis

.py file xlsx_writer combines all those parsers and writes down all the data into xlsx table, ending up with dataset describing up to 1k Data Analyst job vacancies from popular job-posting websites

The resulting dataset is further explored using such libraries as Pandas, Numpy, Matplotlib, etc.
