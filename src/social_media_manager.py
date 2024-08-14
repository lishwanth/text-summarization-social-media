import tweepy

class SocialMediaManager:
    def __init__(self, twitter_api_key, twitter_api_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuth1UserHandler(twitter_api_key, twitter_api_secret, access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def post_to_twitter(self, message):
        self.api.update_status(message)
        print("Posted to Twitter:", message)

# Example usage
if __name__ == "__main__":
    twitter_api_key = 'your_twitter_api_key'
    twitter_api_secret = 'your_twitter_api_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'

    manager = SocialMediaManager(twitter_api_key, twitter_api_secret, access_token, access_token_secret)
    manager.post_to_twitter("This is a test summary!")
