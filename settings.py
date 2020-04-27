import os
from dotenv import load_dotenv

load_dotenv('.env')
key = os.getenv('APIKEY')
my_hostname = os.getenv('my_hostname')