import json
import requests

link = "http://deckofcardsapi.com/api/deck"

deck_count = 6

decks = requests.get ( link + "/new/shuffle/?deck_count=" + str ( deck_count ) )

decks = decks.json ( )

print ( decks )
