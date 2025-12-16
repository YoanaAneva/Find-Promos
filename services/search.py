from scrapers.lidl import search_lidl
from scrapers.kaufland import search_kaufland
from scrapers.billa import search_billa
from scrapers.tmarket import search_tmarket
from scrapers.fantastico import search_fantastico


def search_stores(word) : 
    results = []
    results += search_lidl(word)
    results += search_kaufland(word)
    results += search_billa(word)
    results += search_tmarket(word)
    results += search_fantastico(word)

    if results :
        current_supermarket = results[0]["supermarket"]
        print(current_supermarket)

        for result in results :
            if result["supermarket"] != current_supermarket :
                current_supermarket = result["supermarket"]
                print("\n" + current_supermarket)
            print(result)

search_stores("щолен")

