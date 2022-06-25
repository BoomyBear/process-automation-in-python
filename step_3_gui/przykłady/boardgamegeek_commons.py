import csv
from collections import namedtuple
from typing import List

from selene import browser, config
from selene.support.jquery_style_selectors import s

Game = namedtuple("Game", ["title", "ownership"])

config.browser_name = 'chrome'
config.base_url = 'https://www.boardgamegeek.com/'
config.timeout = 10

def login():
    user_name = "TechPizza"
    password = "TechPizzaTechPizzaTechPizzaGdyżMogę"

    browser.open_url(config.base_url)
    browser.driver().maximize_window()

    s("//*[text()='Sign In']").click()
    s("#inputUsername").type(user_name)
    s("#inputPassword").type(password).press_enter()


def go_to_collection():
    s(".mygeek-dropdown-username").click()
    s("//a[@class='dropdown-item' and text()='Collection']").click()


def fetch_games_from_file(file_name="games.csv") -> List[Game]:
    games = []
    with open(file_name) as file:
        for game_data in csv.DictReader(file, delimiter=","):
            games.append(Game(game_data["Title"], game_data["Do I Have It?"]))
    return games

