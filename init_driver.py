import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth


def init_webdriver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    return driver


def scrolldown(driver, deep):
    for _ in range(deep):
        driver.execute_script('window.scrollBy(0, 500)')
        time.sleep(0.1)


def get_mainpage_cards(driver, url):
    driver.get(url)
    scrolldown(driver, 50)


if __name__ == "__main__":
    driver = init_webdriver()
    get_mainpage_cards(driver, "https://ozon.by")
    time.sleep(25)
    driver.quit()

