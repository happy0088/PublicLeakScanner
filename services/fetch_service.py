import requests
from config import API_URL, HEADERS

class FetchService:
    @staticmethod
    def fetch_data(request_model):
        response = requests.post(API_URL, headers=HEADERS, json=request_model.__dict__)
        return response.json()
