#!/usr/bin/python3
""" Exporting files"""
import json
import requests
import sys


def recurse(subreddit, host_list=[]):
    """Read reddit and return 10 hotspots """
    username = 'led123'
    password = 'Reddit99'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/led123 API Python for NadaKhaled99'}
    payload = {"limit": "150"}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False, params=payload)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        if (len(host_list) < len(list_titles) - 1):
            host_list.append(list_titles[len(host_list)]['data']['title'])
            recurse(subreddit, host_list)
        else:
            print(host_list)
            return(host_list)
    else:
        return(None)
