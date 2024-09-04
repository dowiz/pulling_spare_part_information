from functions import load_dict_from_dotenv
import requests
from bs4 import BeautifulSoup


# Отримуємо login_data та login_headers зі змінних середовища
login_headers = load_dict_from_dotenv("LOGIN_HEADERS")
login_data = load_dict_from_dotenv("LOGIN_DATA")

# # Create a session
session = requests.Session()

# # Send a GET request to the login page
login_page_url = "https://api-aftermarket.schaeffler.de/authorizationserver/oauth/token?catalogCountry=UA"
response = session.post(login_page_url, headers=login_headers, data=login_data)

# # Parse the login page HTML
soup = BeautifulSoup(response.text, "html.parser")

print(soup)
