#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords"""

import requests


def count_words(subreddit, word_list, counts=None, after=None):
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    headers = {'User-Agent': 'MyBot/1.0'}

    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for post in data['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0)\
                        + title.count(word.lower())

        after = data['data'].get('after')
        if after:
            return count_words(subreddit, word_list, counts, after)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return
