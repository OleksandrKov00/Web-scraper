
📌 Custom Web Scraper

Here are Python scripts designed to parse html code of job-posting websites & write down data in xlsx file.

.py files like Builtin_parser, djinni_parser, justjoin.it_parser use such libraries as requests, BeautifulSoup, time... to extract the job vacancy data I was interested in for further analysis

.py file xlsx_write combines all those parsers and writes down all the data into xlsx table, ending up with dataset describing up to 1k job vacancies from popular job-posting websites

The resulting dataset is further explored using such libraries as Pandas, Numpy, Matplotlib, etc.
