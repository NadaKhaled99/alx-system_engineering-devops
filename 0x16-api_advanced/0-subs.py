#!/usr/bin/python3
""" Exporting files"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Read reddit API and return subscribers number"""
    username = 'led123'
    password = 'Reddit99'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/led123 API Python for NadaKhaled99'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return(0)
