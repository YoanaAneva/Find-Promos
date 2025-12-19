from bs4 import BeautifulSoup
import requests

def search_fantastico(word) :
    results = []
    url = "https://glovoapp.com/bg/bg/sofia/stores/coca-cola-real-magic-sof?content=promotsii-pr"

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    products = soup.select(".ItemTile_itemTile__ob2HL")
    for product in products :
        title = product.select_one(".ItemTile_title__aYrXE").text

        if word.lower() in title.lower() :
            image = product.select_one(".ItemTile_image__Qr45O")
            image_src = None
            if image:
                image_src = image["src"]

            prices = product.select_one(".ItemTile_discountedPrice__KmFiz").text.split("(")
            price_bgn = prices[0]
            price_bgn = price_bgn[:-1]
            price_eur = prices[1]
            price_eur = price_eur[:-1]

            is_two_for_one = False
            old_price_bgn = None
            old_price_eur = None
            old_price = product.select_one(".ItemTile_originalPrice__zM5Sr")
            if not old_price :
                is_two_for_one = True
            else :
                old_prices = old_price.text.split("(")
                old_price_bgn = old_prices[0][:-2]
                old_price_eur = old_prices[1][:-1]

            results.append({
                "supermarket" : "Fantastico",
                "title" : title,
                "image_src" : image_src,
                "quantity" : None,
                "price_bgn" : price_bgn,
                "price_eur" : price_eur,
                "old_price_bgn" : old_price_bgn,
                "old_price_eur" : old_price_eur,
                "period" : None,
                "is_two_for_one" : is_two_for_one
            })

    return results
            