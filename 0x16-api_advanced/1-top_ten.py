#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles,
of the first 10 hot posts listed for a given subreddit.
"""
import requests
import sys


def top_ten(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {"User-Agent": "MyRedditApp"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                for post in posts:
                    title = post['data']['title']
                    print(title)
            else:
                print(None)
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)


if __name__ == "__main__":
    subreddit = sys.argv[1]
    top_ten(subreddit)
