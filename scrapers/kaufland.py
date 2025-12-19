from bs4 import BeautifulSoup
import requests

def search_kaufland(word) :
    results = []
    search_word = word.replace(" ", "+")
    url = "https://www.kaufland.bg/tursene.html?q=" + search_word

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    products = soup.select(".k-product-tile")
    for product in products :
        title = product.select_one(".k-product-tile__title").text
        description = product.select_one(".k-product-tile__subtitle").text

        if (word.lower() in title.lower() or word.lower() in description.lower()) :
            image_src = None
            image = product.select_one(".k-image")
            if image :
                image_src = image["src"]
                if "media.kaufland" in image_src :
                    image_src = None
                                   
            prices = product.select(".k-price-tag__price")
            price_bgn = prices[0].text
            price_eur = prices[1].text

            quantity = product.select_one(".k-product-tile__unit-price").text
            period = product.select_one(".k-eye-catcher").text

            old_prices = product.select(".k-price-tag__old-price-line-through")
            old_price_bgn = None
            old_price_eur = None
            if (len(old_prices) > 0) :
                old_price_bgn = old_prices[0].text
                old_price_eur = old_prices[1].text

            results.append({
                "supermarket" : "Kaufland",
                "title" : title + " " + description,
                "image_src" : image_src,
                "quantity" : quantity,
                "price_bgn" : price_bgn,
                "price_eur" : price_eur,
                "old_price_bgn" : old_price_bgn,
                "old_price_eur" : old_price_eur,
                "period" : period,
                "is_two_for_one" : False
            })
    return results