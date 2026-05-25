import logging

url = "https://alpha-vantage.p.rapidapi.com/query"

headers = {
    "x-rapidapi-key": "e1aa54ef16mshbcc7e01fea5c9a4p19910ajsna13fa7823f41",
    "x-rapidapi-host": "alpha-vantage.p.rapidapi.com"
}

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)