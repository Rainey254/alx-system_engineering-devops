#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit.

    If not a valid subreddit, print None.
    Invalid subreddits may return a redirect to search results. Ensure
    that you are not following redirects.

    Args:
        subreddit (str): subreddit

    Returns:
        str: titles of the first 10 hot posts
    """
    base_url = 'https://www.reddit.com'
    sort = 'top'
    limit = 10
    url = '{}/r/{}/.json?sort={}&limit={}'.format(
        base_url, subreddit, sort, limit)
    headers = {'User-Agent": "My-User-Agent'}
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
