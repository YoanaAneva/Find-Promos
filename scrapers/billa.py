from bs4 import BeautifulSoup
import requests

def search_billa(word) :
    results = []
    url = "https://ssbbilla.site/"

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    products = soup.select(".product")
    for product in products :
        title = product.select_one(".actualProduct").text
        if (word.lower() in title.lower()) :
            title = title.rstrip()
            title = title.lstrip()

            prices = product.select(".price")
            if prices :
                price_bgn = prices[2].text
                price_eur = prices[3].text
                old_price_bgn = prices[0].text
                old_price_eur = prices[1].text

                results.append({
                    "supermarket" : "Billa",
                    "title" : title,
                    "quantity" : "none",
                    "period" : "none",
                    "old_price_bgn" : old_price_bgn,
                    "old_price_eur" : old_price_eur,
                    "price_bgn" : price_bgn,
                    "price_eur" : price_eur,
                    "is_two_for_one" : False
                })
 
    return results