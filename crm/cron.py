import datetime
import requests
from gql.transport.requests import RequestsHTTPTransport 
from gql import gql, Client

def log_crm_heartbeat():
    """
    checks the GraphQL endpoint for a response
    """
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is live\n"

    log_path = "/tmp/crm_heartbeat_log.txt"

    try:
        #graphQL endpoint check
        response = requests.post(
            "http://localhost:8000/graphql",
            json={"query": "{ hello }"},
            timeout=5
        )
        if response.status_code == 200:
            message = f"{timestamp} CRM is alive (GraphQL OK)\n"
        else:
            message = f"{timestamp} CRM is alive (GraphQL FAILED {response.status_code})\n"
    except Exception as e:
        message = f"{timestamp} CRM is alive (GraphQL ERROR: {e})\n"

    with open(log_path, "a") as log_file:
        log_file.write(message)
