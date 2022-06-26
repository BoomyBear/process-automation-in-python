from time import sleep

from selene import config, browser
from selene.conditions import visible, clickable
from selene.support.jquery_style_selectors import s

env = f"http://boardgamegeek.com/"
config.timeout = 5
config.start_maximized = True
accept_cookie_button = s("#c-p-bn")

browser.open_url(env)
accept_cookie_button.should_be(clickable)
accept_cookie_button.click()
accept_cookie_button.should_not_be(visible)

sleep(5)
