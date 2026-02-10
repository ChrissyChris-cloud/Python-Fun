import requests
from bs4 import BeautifulSoup

# URL to scrape (example: Wikipedia page)
url = "https://en.wikipedia.org/wiki/Web_scraping"

# 1. Fetch page
response = requests.get(url)

if response.status_code == 200:
    html = response.text

    # 2. Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # 3. Extract all headings (h2)
    headings = soup.find_all("h2")

    print("Headings found on the page:\n")
    for h in headings:
        text = h.get_text().replace("[edit]", "").strip()
        print("-", text)
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
