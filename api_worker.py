import requests
import json 
import ip_parser
import socket

"""
api fields
    status
    country
    as
"""


URL = 'http://ip-api.com/batch'

def pre_work(ips: list):
    new_ips = []
    for i in range(len(ips)):
        new_ips.append(ip_parser.parse_ip(ips[i]))
    return new_ips

def get_dns(ip):
    hostname = "unresolved"
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        ...
    return hostname

def parse_response_data(response_data, ips):
    result = []

    for i in range(len(response_data)):

        temp_data = {
            'ip': 'ip',
            'status': 'fail',
            'country': 'country none',
            'organization': 'organization none',
            'as': 'as none',
            'hostname': 'unresolved'
        }

        temp_data['ip'] = ips[i]

        if response_data[i]['status'] == 'fail':
            result.append(temp_data)
            continue
        else:
            hostname = get_dns(response_data[i]['query'])
            temp_data['status'] = response_data[i]['status']
            temp_data['country'] = response_data[i]['country']
            temp_data['as'] = response_data[i]['as']
            temp_data['organization'] = response_data[i]['org']
            temp_data['hostname'] = hostname
            result.append(temp_data)

    return result

def work(ips: list):
    
    worked_ips = pre_work(ips)

    assert len(worked_ips) <= 100

    data_json = json.dumps(worked_ips)

    response = requests.post(URL, data=data_json)

    response_data = parse_response_data(json.loads(response.text), ips)

    return response_data    