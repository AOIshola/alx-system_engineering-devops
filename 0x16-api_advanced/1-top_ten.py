#!/usr/bin/python3

"""queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """retrieves the first 10 hot posts in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()

        for post in data['children']['data']:
            print(post['data']['title'])
    else:
        print(None)
