# Hockey Teams Scraper - Python

A web scraper built with Python that extracts NHL Hockey
team statistics from scrapethissite.com across multiple pages.

## What it Does
- Scrapes 24 pages of hockey team data automatically
- Extracts team name, year, wins, losses, OT losses,
  win percentage, goals for, goals against and +/- diff
- Saves all data into a clean teams.json file

## Libraries Used
- requests
- beautifulsoup4
- json

## How to Run
1. Install libraries:
   pip install requests beautifulsoup4

2. Run the scraper:
   python hockey.py

3. Output will be saved in teams.json

## Output Format
```json
{
    "name": "Boston Bruins",
    "Year": "1990",
    "wins": "44",
    "Loses": "24",
    "Ot Loses": "",
    "Win %": "0.55",
    "Goal For": "299",
    "Goal Against": "264",
    "+/-": "35"
}
```

## Concepts Used
- HTTP requests with requests library
- HTML table parsing with BeautifulSoup
- Multi-page scraping with pagination
- Nested HTML element navigation
- JSON data storage
- Loops and functions

## Author
BSIT Student | Aspiring Python Developer
University of Education
