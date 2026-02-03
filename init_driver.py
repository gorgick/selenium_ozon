import time
from bs4 import BeautifulSoup
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
        driver.execute_script('window.scrollBy(0, 200)')
        time.sleep(0.1)


def get_mainpage_cards(driver, url):
    driver.get(url)
    scrolldown(driver, 50)
    main_page_html = BeautifulSoup(driver.page_source, "html.parser")
    content = main_page_html.find("div", {"class": "container c"})
    content = content.find_all(recursive=False)[-1].find("div")
    content = content.find_all(recursive=False)
    content = [item for item in content if "island" in str(item)][-1]
    content = content.find("div").find("div").find("div")
    content = content.find_all(recursive=False)

    for layer in content:
        layer = layer.find("div")
        cards = layer.find_all(recursive=False)
        for card in cards:
            card = card.find_all(recursive=False)
            card_name = card[2].find("span", {"class": "tsBody500Medium"}).contents[0]
            card_url = card[2].find("a", href=True)["href"]
            print(card_name, card_url)


if __name__ == "__main__":
    driver = init_webdriver()
    get_mainpage_cards(driver, "https://ozon.by")
    time.sleep(25)
    driver.quit()
