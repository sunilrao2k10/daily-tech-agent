import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

load_dotenv()

auth = OAuth1(
        os.getenv("X_CONSUMER_KEY"),
        os.getenv("X_CONSUMER_SECRET"),
        os.getenv("X_ACCESS_TOKEN"),
        os.getenv("X_ACCESS_TOKEN_SECRET")
    )

def publish_to_x(post):
    url = "https://api.x.com/2/tweets"

    payload = {
        "text": post
    }

    response = requests.post(
        url,
        auth=auth,
        json=payload,
        timeout=10
    )
    
    print("Status:", response.status_code)
    print("Response:", response.text)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    post = "I am doing testing for an app"
    publish_to_x(post)    