#!/usr/bin/python3
"""Task 3"""


def number_of_subscribers(subreddit):
    """Queries Reddit APi and return of suscribers"""
    import requests

    sub_inf = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit),
                           headers={"User-Agent": "My-User-Agent"},
                           allow_redirects=False)

    if sub_inf.status_code >= 300:
        return 0

    return sub_inf.json().get("data").get("subscribers")
