#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit"""

import requests
import requests.auth

def number_of_subscribers(subreddit):
    """retrieves the number of subscribers in a subreddit"""

    base_url = 'https://www.reddit.com/'
    data = {'grant_type': 'password', 'username': 'AOIshola', 'password': 'fatimah5'}
    auth = requests.auth.HTTPBasicAuth('9baZynf4FmoBRMSjRJgd6A', '3maT1a4fbesYqv8ibXQEmCzttbdEtQ')
    res = requests.post(base_url + 'api/v1/access_token', data=data,
                        headers={'user-agent': 'alx-task by AOIshola'}, auth=auth)

    data = res.json()
    token = 'bearer ' + data['access_token']

    api_url = 'https://oauth.reddit.com'
    headers = {'Authorization': token, 'user-agent': 'alx-task by AOIshola'}
    response = requests.get(api_url + f'/r/{subreddit}/about', headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        return (response.json()['data']['subscribers'])
    else:
        return 0
#     headers = {"User-Agent": "MyTask/1.0"}

#     response = requests.get(url, headers=headers, allow_redirects=False)
#     if response.status_code == 200:
#         data = response.json()

#         return data['data']['subscribers']
#     else:
#         return 0

# using praw
    # import praw

    # r = praw.Reddit(client_id = 'ci3jQyOGUKErBgwpDcizOQ',
    #             client_secret = 'IBqtBoBvaX_UD-FUTtP9Kn1vjE7X2A',
    #             user_agent = 'Alx-task by Electrical_Flow_417')

    # print(r.subreddit('programming'))
