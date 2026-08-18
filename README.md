
📌 Custom Web Scraper

Python web scraper designed to collect and structure Data Analyst job postings from multiple job boards for further analysis.

The scraper extracts key job-market information such as salary, required experience, skills, work arrangement, location, etc. and combines the results into a single dataset.

🌐 Data Sources

The project currently includes parsers for:

Builtin │ Djinni │ JustJoin.it

⚙️ How It Works

Job Boards

    │
    
    ├── Builtin parser
    
    ├── Djinni parser
    
    └── JustJoin.it parser
    
            │
            
            ▼
            
      Data Extraction
      
            │
            
            ▼
            
       XLSX Writer
       
            │
            
            ▼
            
      Combined Dataset
      
            │
            
            ▼
            
       EDA & Analysis


📊 Data Aggregation

xlsx_writer.py combines the output from all parsers and exports the collected data into an XLSX dataset.

The resulting dataset contains up to 1,000 Data Analyst vacancies from job boards covering markets such as:

🇺🇦 Ukraine          🇵🇱 Poland

🇺🇸 United States    🇩🇪 Germany

📦 Collected Data

Depending on the source, the scraper collects information including:

Job title
Salary range
Average salary
Years of experience
Required skills
Work arrangement
Location
Region
English level
Job posting URL

🛠️ Technologies
Python
Requests — HTTP requests
BeautifulSoup — HTML parsing
Pandas — data processing
OpenPyXL — XLSX generation
Time — request timing and scraping control
📈 Further Analysis

The generated dataset is used as the foundation for a separate Exploratory Data Analysis (EDA) project using:

Pandas
NumPy
Matplotlib
Seaborn
SciPy

The analysis e
