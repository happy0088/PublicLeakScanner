import logging
from services.leak_detection.postman_leak_detector import PostmanLeakDetector
from utils.data_parser import Parser
from services.db_service import DBService
from services.notification_service import NotificationService
from config import QUERY_TEXT

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Instantiate leak detectors
        postman_leak_detector = PostmanLeakDetector(QUERY_TEXT)

        # Detect leaks
        try:
            response = postman_leak_detector.detect_leaks()
        except Exception as e:
            logging.error(f"Error detecting leaks: {e}")
            response = None

        if response:
            try:
                parsed_data = Parser.parse_response(response)
            except Exception as e:
                logging.error(f"Error parsing response: {e}")
                parsed_data = None

            if parsed_data:
                db_service = DBService()
                try:
                    if db_service.find_new_data(parsed_data):
                        db_service.insert_data(parsed_data)
                except Exception as e:
                    logging.error(f"Error handling database operations: {e}")

                try:
                    notification_service = NotificationService()
                    message = f"New findings: {parsed_data}"
                    notification_service.send_notification(message)
                except Exception as e:
                    logging.error(f"Error sending notification: {e}")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
