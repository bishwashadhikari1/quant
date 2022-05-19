import os
from binance import Client
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("api_key")
apisecret = os.getenv("api_secret")

session = Client(apikey, apisecret)