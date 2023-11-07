#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and,
returns a list containing the titles of all hot articles,
for a given subreddit else return None.
"""

import requests
import sys


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    headers = {"User-Agent": "MyRedditApp"}

    if after:
        url += f"&after={after}"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                for post in posts:
                    title = post['data']['title']
                    hot_list.append(title)

                after = data['data']['after']
                if after is not None:
                    return (recurse(subreddit, hot_list, after))
                else:
                    return (hot_list)
            else:
                return (None)
        else:
            return (None)
    except requests.exceptions.RequestException:
        return (None)


if __name__ == "__main__":
    subreddit = sys.argv[1]
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")
