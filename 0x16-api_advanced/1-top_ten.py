#!/usr/bin/python3
""" Exporting  files"""
import json
import requests
import sys


def top_ten(subreddit):
    """Read reddit and  return 10 hotspots """
    username = 'led123'
    password = 'Reddit99'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/led123 API Python for NadaKhaled99'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        for a in list_titles[:10]:
            print(a['data']['title'])
    else:
        return(print("None"))
