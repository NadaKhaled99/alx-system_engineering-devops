#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def recurse(subreddit, host_list=[], after="null"):
    """Read reddit and return 10 hotspots """
    username = 'led123'
    password = 'Reddit99'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/led123 API Python for NadaKhaled99'}
    payload = {"limit": "100", "after": after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False, params=payload)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        after = r.json()['data']['after']
        if after is not None:
            host_list.append(list_titles[len(host_list)]['data']['title'])
            recurse(subreddit, host_list, after)
        else:
            return(host_list)
    else:
        return(None)
