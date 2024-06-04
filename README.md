# PublicLeakScanner

PublicLeakScanner is a Python-based tool designed to detect and monitor potential leaks of sensitive information in publicly accessible sources. It fetches data from various sources, parses the responses, and stores any new findings in a MongoDB database. Additionally, it provides notifications for newly discovered leaks.

## Features

- Fetches data from publicly accessible sources.
- Parses response data to extract relevant information.
- Stores findings in a MongoDB database.
- Sends notifications for newly discovered leaks.
- Easily configurable for different search queries.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/happy0088/PublicLeakScanner.git
   ```
2. Navigate to the project directory:
   ```
   cd PublicLeakScanner
   ```
3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Configuration

The project can be configured through the `config.py` file located in the root directory. Here are the configurable parameters:

- **MongoDB Configuration**:
  - `MONGO_URI`: URI for connecting to the MongoDB database.
  - `DATABASE_NAME`: Name of the MongoDB database.
  - `COLLECTION_NAME`: Name of the collection within the database.

- **Email Configuration**:
  - `EMAIL_CONFIG`: Configuration settings for sending email notifications (SMTP server, port, sender email, receiver email, password).

- **Query Configuration**:
  - `QUERY_TEXT`: The search query text used to identify potential leaks. 

## Usage

To run the PublicLeakScanner tool, simply execute the `main.py` script:
```
python main.py
```

Alternatively, you can run the tool using Docker:
```
docker-compose up --build
```

The tool will run the leak detection process and store any new findings in the MongoDB database. Notifications will be sent for newly discovered leaks.

## Schedule as Cron Job

To schedule the PublicLeakScanner tool to run as a cron job, you can use the provided `cron_job.sh` script. Edit the cron schedule in the script as needed and add it to your system's cron jobs.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


## Author

Happy0088