import os
import tweepy

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Replace with your Bearer Token
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Initialize the Twitter API client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Search for recent tweets
def search_tweets(query, max_results=20):
    response = client.search_recent_tweets(query=query, max_results=max_results)
    if response.data:
        for tweet in response.data:
            print(f"Tweet ID: {tweet.id} | Text: {tweet.text}")
    else:
        print("No tweets found or insufficient access.")

# Example usage
search_tweets("Python programming", max_results=5)

# Test