import os
import tweepy
import requests

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Replace with your Bearer Token
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

if not BEARER_TOKEN:
    raise ValueError("Bearer Token not found. Please set the BEARER_TOKEN environment variable.")

# Initialize the Twitter API client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Search for recent tweets
def search_tweets(query, max_results=12):
    response = client.search_recent_tweets(query=query, max_results=max_results)
    if response.data:
        for tweet in response.data:
            print(f"Tweet ID: {tweet.id} | Text: {tweet.text}")
    else:
        print("No tweets found or insufficient access.")

# Check rate limit status
def check_rate_limit():
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    params = {
        "query": "test",  # Dummy query to make the request valid
        "max_results": 10  # Minimal valid results to avoid hitting the rate limit
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        rate_limit_status = {
            "x-rate-limit-limit": response.headers.get("x-rate-limit-limit"),
            "x-rate-limit-remaining": response.headers.get("x-rate-limit-remaining"),
            "x-rate-limit-reset": response.headers.get("x-rate-limit-reset")
        }
        print(f"Rate Limit Status: {rate_limit_status}")
    else:
        print(f"Failed to fetch rate limit status: {response.status_code}, {response.text}")

# Example usage
check_rate_limit()
# search_tweets("Python programming", max_results=10)