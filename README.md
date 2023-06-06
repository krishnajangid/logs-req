# logs-req

This project provides APIs to log request to file and flush logs to db once file content is 10 Mb or every 30 second

Table of Contents

    Installation
    Folder Structure
    Usage
    API Endpoints
    Script 
    Authors

## Installation

To install this project, follow these steps:

1. Clone this repository using the following command:

```bash
git clone https://github.com/<username>/logs-req.git
```

2. Change the directory to the cloned repository using the following command:

```bash
cd logs-req
```
## Folder Structure
```commandline
Quantive/
├── README.md
├── requirements.txt
├── entrypoint.sh
├── Dockerfile
├── docker-compose.yml
├── src/
│   ├── __init__.py
│   ├── run.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── log.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── schemas/
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   └── request.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   └── api.py
│   ├── repository/
│   │   ├── __init__.py
│   │   └── log.py
└── └── utils/
        ├── __init__.py
        ├── config.py
        ├── constants.py
        ├── database.py
        └── common.py
```
## Usage
Run app using Docker Compose

```bash
docker compose build
docker compose up
```

3. Access the API endpoints on your local machine using the URL http://localhost:5050/.

## API Endpoints

This project provides the following API endpoints:
```
POST /logs: Allows user to add request to db
payload = {
            "user_id": 123456,
            "event_name": "login"
          }
Note: Here we store id as auto-increament and unix_ts as default now
```
```
DELETE /logs/clear-file: Allows user to clear file
```
## Script
Here we have python script to trigger logs api. Run script by using bellow command

    $ python trigger_log_request_script.py

## Authors

    Your Name (@krishnajangid)