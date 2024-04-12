#!/usr/bin/python3
"""Recursive call"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    
    headers = {'User-Agent': 'MyBot/1.0'}
    
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        
        after = data['data'].get('after')
        if after:
            # Recursive call to fetch next page
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
