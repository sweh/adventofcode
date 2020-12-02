import requests


def fetch(url):
    session = requests.session()
    session.cookies["session"] = open(".session", "r").read().splitlines()[0]
    response = session.get(url)
    return response.text
