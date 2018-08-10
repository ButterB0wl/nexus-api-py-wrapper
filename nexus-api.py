#!/usr/bin/python3
#
# Author: Artemie Jurgenson (ajurgenson@sonatype.com)
# This script serves as a generic request wrapper for the nexus repo API. 

import os, sys, requests, json
import config

# Parser for command line flags
def get_parser():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--repo-url',
                        action='store',
                        default='http://localhost:8081')

    parser.add_argument('-e', '--endpoint',
                        action='store', required=True,
                        help='the api endpoint e.g. \'tags/associate/{tagName}\'')

    parser.add_argument('-t', '--request-type',
                        action='store', required=True,
                        choices=config.REQ_TYPES,
                        help='the type of your http request: get, post, put, delete')
    
    return parser


# Makes the different types of requests
def make_request(req_type, url):  
    if req_type == 'get':
        return requests.get(url, auth=config.AUTH)
    elif req_type == 'post':
        return requests.post(url, auth=config.AUTH)
    elif req_type == 'delete':
        return requests.delete(url, auth=config.AUTH)
    elif req_type == 'put':
        return requests.put(url, auth=config.AUTH)
    else:
        raise Exception('No valid http requests type', req_type)


def main(argv):
        
    r = make_request(argv.request_type, argv.repo_url + config.BASE_URL + argv.endpoint)
    
    # Checks for request errors
    try:
        r.raise_for_status()
    except requests.exceptions.Timeout:
        print('Request timed out - retrying...')
        r = make_request(argv.request_type, argv.repo_url + config.BASE_URL + argv.endpoint)
    except requests.exceptions.TooManyRedirects:
        print('Bad url, use a different one.')
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    
    # prints headers and status
    status = r.status_code
    print('Status:', status)
    print(r.headers)
    
    # checks if there's content before dumping to json and printing/piping to file
    if status != 204:
        r_json = json.dumps(r.json(), indent=4)
        print(r_json)    
        f = open('response.json', 'w+')
        f.write(r_json)
        f.close()


if __name__ == "__main__":
    main(get_parser().parse_args(sys.argv[1:]))
