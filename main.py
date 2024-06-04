from services.db_service import DBService
from services.notification_service import NotificationService
from services.leak_detection.postman_leak_detector import PostmanLeakDetector
from utils.parser import Parser
from config import QUERY_TEXT

def main():
    # Instantiate leak detectors
    postman_leak_detector = PostmanLeakDetector(QUERY_TEXT)

    # Detect leaks
    response = postman_leak_detector.detect_leaks()

    parsed_data = Parser.parse_response(response)

    db_service = DBService()
    if db_service.find_new_data(parsed_data):
        db_service.insert_data(parsed_data)

        notification_service = NotificationService()
        message = f"New findings: {parsed_data}"
        notification_service.send_notification(message)

if __name__ == "__main__":
    main()
