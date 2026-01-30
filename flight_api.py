import requests
from config import API_KEY, API_SECRET

TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"

def get_access_token():
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }
    )
    response.raise_for_status()
    return response.json()["access_token"]

def get_flight_price(source, destination, date):
    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "originLocationCode": source.upper(),
        "destinationLocationCode": destination.upper(),
        "departureDate": date,
        "adults": 1,
        "currencyCode": "INR",
        "max": 1
    }

    response = requests.get(FLIGHT_URL, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    price = float(data["data"][0]["price"]["grandTotal"])
    return int(price)
