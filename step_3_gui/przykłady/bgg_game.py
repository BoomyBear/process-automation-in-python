from selene import browser
from selene.support.jquery_style_selectors import s


def get_game_id():
    return browser.driver().current_url.split("/")[-2]


def get_language_dependence():
    return s("[item-poll-button='languagedependence'] .ng-binding").text

def unfold_language_dependence_poll():
    return s("[item-poll-button='languagedependence'] button").click()
