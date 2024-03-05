#!/usr/bin/python3

import requests, io, json

invidious_instances_api='https://api.invidious.io/instances.json'
invidious_resp = requests.get(invidious_instances_api)
invidious_dict = invidious_resp.json()

yattee_dict = {'instances': []}

for item in invidious_dict:
    invidious_instance = item[1]
    has_api = invidious_instance['api']
    region = invidious_instance['region']
    flag = invidious_instance['flag']
    uri = invidious_instance['uri']

    if ('monitor' in invidious_instance) and (invidious_instance['api']):
        yattee_instance = {
                        'app': 'Invidious',
                        'region': invidious_instance['region'],
                        'country': invidious_instance['region'],
                        'flag': invidious_instance['flag'],
                        'url': invidious_instance['uri']
                        }

        yattee_dict['instances'].append(yattee_instance)

with io.open('yattee.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(yattee_dict, ensure_ascii=False))

