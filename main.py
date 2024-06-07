import json
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
                parsed_data_list = Parser.parse_response(response)
                parsed_response_data_list = json.dumps(parsed_data_list['data'])
                parsed_response_data_list = json.loads(parsed_response_data_list)
            except Exception as e:
                logging.error(f"Error parsing response: {e}")
                parsed_data_list = []

            if parsed_data_list:
                db_service = DBService()
                notification_service = NotificationService()
                
        for parsed_data_str in parsed_response_data_list:
            try:
                # Parse each JSON string into a dictionary
                parsed_data = (parsed_data_str)

                # Serialize the data field as JSON
                parsed_data_json = json.dumps(parsed_data["document"])
                parsed_data_json = json.loads(parsed_data_json)

                if db_service.find_new_data(parsed_data_json):
                    # Insert the data into the database
                    db_service.insert_data(parsed_data_json)
                                    
                    # Send notification for each inserted row
                    message = f"New finding: {parsed_data}"
                    notification_service.send_notification(message)
            except Exception as e:
                logging.error(f"Error processing data: {e}")


    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
