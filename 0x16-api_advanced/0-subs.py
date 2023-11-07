#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number,
of subscribers else return 0.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "MyRedditApp"}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return (subscribers)
        else:
            return (0)
    except requests.exceptions.RequestException:
        return 0


if __name__ == "__main__":
    subreddit = sys.argv[1]
    num_subscribers = number_of_subscribers(subreddit)
    print(num_subscribers)
