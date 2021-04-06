import requests


def fetch(year, day):
    session = requests.session()
    session.cookies["session"] = open(".session", "r").read().splitlines()[0]
    response = session.get(f"https://adventofcode.com/{year}/day/{day}/input")
    return response.text[:-1]

