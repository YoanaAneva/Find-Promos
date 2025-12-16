from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def search_lidl(word) :
    results = []
    try :
        search_word = word.replace(" ", "+")
        url = "https://www.lidl.bg/q/search?q=" + search_word

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        products = soup.select(".product-grid-box__content")
        for product in products :
            discount = product.select_one(".ods-price__box-wrapper")
            if discount :
                title = product.select_one(".product-grid-box__title").text
                if word.lower() in title.lower() :
                    quantity = product.select(".ods-price__footer")[1].text
                    period = product.select_one(".ods-badge__label").text

                    prices = product.select(".ods-price__value")
                    price_bgn = prices[0].text
                    price_eur = prices[1].text

                    old_price_bgn = "none"
                    old_price_eur = "none"
                    old_price = product.select_one(".ods-price__stroke-price")
                    if old_price :
                        old_prices = old_price.text.split("(")
                        old_price_bgn = old_prices[0][:-2]
                        old_price_eur = old_prices[1][:-1]

                    results.append({
                        "supermarket" : "Lidl",
                        "title" : title,
                        "quantity" : quantity,
                        "period" : period,
                        "old_price_bgn" : old_price_bgn,
                        "old_price_eur" : old_price_eur,
                        "price_bgn" : price_bgn,
                        "price_eur" : price_eur,
                        "is_two_for_one" : False
                    })

    finally :
        driver.quit()
        
    return results