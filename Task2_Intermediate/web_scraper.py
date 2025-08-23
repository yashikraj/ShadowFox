import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    movies = soup.select("li.ipc-metadata-list-summary-item")

    print("IMDB Top 250 Movies:\n")

    for rank, movie in enumerate(movies, start=1):
        title = movie.select_one("h3").get_text(strip=True)
        year = movie.select_one("span.cli-title-metadata-item").get_text(strip=True)
        rating = movie.select_one("span.ipc-rating-star--rating").get_text(strip=True)

        print(f"{rank}. {title} ({year}) - {rating}")
else:
    print("Failed to fetch data. Status code:", response.status_code)
