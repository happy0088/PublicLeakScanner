from .leak_detector import LeakDetector
from models.request_model import PostmanRequestModel
from services.fetch_service import FetchService

class PostmanLeakDetector(LeakDetector):
    def __init__(self, query_text):
        self.query_text = query_text

    def detect_leaks(self):
        request_model = PostmanRequestModel(self.query_text)
        fetch_service = FetchService()
        response = fetch_service.fetch_data(request_model)
        return response
