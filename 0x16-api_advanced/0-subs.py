#!/usr/bin/python3
"""Task 3"""
import requests


def number_of_subscribers(subreddit):
    """Queries Reddit APi and return of suscribers"""

    sub_inf = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit),
                           headers={"User-Agent": "My-User-Agent"})

    if sub_inf.status_code == 200:
        sub_inf.json().get("data").get("subscribers")
    else:
        return 0
