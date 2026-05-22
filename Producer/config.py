import logging

url = "https://www.alphavantage.co/query"

headers = {
    "User-Agent": "Mozilla/5.0"
}

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)