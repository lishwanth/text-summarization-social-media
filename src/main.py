from src.content_scraper import ContentScraper
from src.summarizer import Summarizer
from src.social_media_manager import SocialMediaManager
from src.logger import Logger

def main():
    url = 'https://example-blog.com/sample-article'
    
    # Scrape content
    scraper = ContentScraper(url)
    content = scraper.parse_content()

    # Summarize content
    summarizer = Summarizer()
    summary = summarizer.summarize(content)

    # Post summary to Twitter
    twitter_api_key = 'your_twitter_api_key'
    twitter_api_secret = 'your_twitter_api_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'

    social_media_manager = SocialMediaManager(twitter_api_key, twitter_api_secret, access_token, access_token_secret)
    social_media_manager.post_to_twitter(summary)

    # Log the post
    logger = Logger()
    logger.log("Twitter", summary)

if __name__ == "__main__":
    main()
