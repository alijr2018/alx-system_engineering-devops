#!/usr/bin/python3
"""
a recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests
import sys


def count_words(subreddit, word_list, count_dict=None, after=None):
    if count_dict is None:
        count_dict = {}

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
                    title = post['data']['title'].lower()

                    words = title.split()
                    for word in words:
                        if word in word_list:
                            count_dict[word] = count_dict.get(word, 0) + 1

                after = data['data']['after']
                if after is not None:
                    return count_words(subreddit, word_list, count_dict, after)
                else:
                    y = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
                    for keyword, count in y:
                        print(f"{keyword}: {count}")
            else:
                return
        else:
            return
    except requests.exceptions.RequestException:
        return


if __name__ == "__main__":
    subreddit = sys.argv[1]
    word_list = [x.lower() for x in sys.argv[2].split()]
    count_words(subreddit, word_list)
