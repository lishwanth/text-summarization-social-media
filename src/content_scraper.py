import requests
from bs4 import BeautifulSoup

class ContentScraper:
    def __init__(self, url):
        self.url = url

    def fetch_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Failed to retrieve content")

    def parse_content(self):
        html = self.fetch_content()
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article')
        paragraphs = article.find_all('p')
        return "\n".join([p.get_text() for p in paragraphs])

# Example usage
if __name__ == "__main__":
    url = 'https://example-blog.com/sample-article'
    scraper = ContentScraper(url)
    content = scraper.parse_content()
    print(content)
