from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def search_tmarket(word) :
    results = []
    try :
        search_word = word.replace(" ", "+")
        url = "https://tmarketonline.bg/search?query=" + search_word

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        products = soup.select("._product-inner")
        for product in products :
            discount = product.select_one(".has-discount")  
            if (discount) :
                title = product.select_one("._product-name-tag").text

                if (word.lower() in title.lower()) :
                    image_src = "assets/no-photo.jpg"
                    image = product.select_one("._product-image-thumb-holder .lazyload-image")
                    if image :
                        image_src = image["src"]

                    price_bgn = product.select_one(".bgn2eur-primary-currency").text
                    price_eur = product.select_one(".bgn2eur-secondary-currency").text

                    old_price_bgn = product.select_one("._product-price-old .bgn2eur-primary-currency").text
                    old_price_eur = product.select_one("._product-price-old .bgn2eur-secondary-currency").text

                    results.append({
                        "supermarket" : "TMarket",
                        "title" : title,
                        "image_src" : image_src,
                        "quantity" : None,
                        "price_bgn" : price_bgn,
                        "price_eur" : price_eur,
                        "old_price_bgn" : old_price_bgn,
                        "old_price_eur" : old_price_eur,
                        "period" : None,
                        "is_two_for_one" : False
                    })
    finally :
        driver.quit()
    return results