#!/usr/bin/python3
"""
Function that queries the Reddit API and
returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    req = requests.get(url, headers={'User-Agent': 'Python/requests'})

    try:
        resp = req.json()
        return resp.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
