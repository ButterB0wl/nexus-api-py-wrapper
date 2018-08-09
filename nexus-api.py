#!/usr/bin/python3
#
# Author: Artemie Jurgenson (ajurgenson@sonatype.com)
# This script serves as a generic request wrapper for the nexus repo API

import os

BASE_URL='/service/rest/v1/'

def get_parser():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--repo-url',
                        action='store', nargs='?',
                        default='http://localhost:8081')

    parser.add_argument('-e', '--endpoint',
                        action='store',
                        help='the api endpoint e.g. \'tags/associate/{tagName}\'')

    parser.add_argument('-t', '--request-type',
                        action='store',
                        choices=['get','post','put','delete'],
                        help='the type of your http request: get, post, put, delete')
    
    return parser

if __name__ == "__main__":
    args = get_parser().parse_args()
