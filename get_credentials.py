import json

def get_credentials():
    """None"""
    with open('credentials.json', 'r') as file:
        credentials = json.load(file)
