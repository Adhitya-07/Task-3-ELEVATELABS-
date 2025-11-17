import requests
from bs4 import BeautifulSoup
from datetime import datetime

# ---------------------------
#  UNIQUE COLORED TITLE
# ---------------------------
print("\033[1;36m═══════════════════════════════════════")
print("     📰 NEWS HEADLINE SCRAPER - TASK 3")
print("═══════════════════════════════════════\033[0m")

# Target URL
url = "https://www.ndtv.com/latest"

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    # Finding headlines
    headlines = soup.find_all("h2", class_="newsHdng")

    cleaned_headlines = []
    for h in headlines[:10]:     # Get TOP 10
        text = h.text.strip()
        cleaned_headlines.append(text)

    # Create a text file to save headlines
    filename = "top_news_headlines.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("TOP NEWS HEADLINES\n")
        file.write(f"Scraped on: {datetime.now()}\n\n")
        for idx, h in enumerate(cleaned_headlines, 1):
            file.write(f"{idx}. {h}\n")

    # Success Output
    print("\033[1;32m✔ Headlines scraped successfully!")
    print(f"✔ Saved to file: {filename}\033[0m")

    # Display headlines in terminal
    print("\n\033[1;35m--- TOP HEADLINES ---\033[0m")
    for i, headline in enumerate(cleaned_headlines, 1):
        print(f"\033[38;5;208m{i}. {headline}\033[0m")

except Exception as e:
    print("\033[1;31m❌ ERROR:", e, "\033[0m")