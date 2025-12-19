from scrapers.lidl import search_lidl
from scrapers.kaufland import search_kaufland
from scrapers.billa import search_billa
from scrapers.tmarket import search_tmarket
from scrapers.fantastico import search_fantastico


def search_supermarkets(word) : 
    results = []
    results += search_lidl(word)
    results += search_kaufland(word)
    results += search_billa(word)
    results += search_tmarket(word)
    results += search_fantastico(word)

    return results