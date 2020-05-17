import os

from googleapiclient.discovery import build
from googleapiclient.errors import Error
from google.auth.credentials import Credentials

os.environ["GOOGLE_CLOUD_PROJECT"] = "resumatch-277502"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./resumatch-google-application-credentials.json"
project_id = 'projects/' + os.environ['GOOGLE_CLOUD_PROJECT']

# Build the service object, passing in the api name and api version
client_service = build('jobs', 'v3')

def job_search(request_metadata, search_term):
    try:
        job_query = {"query": search_term}

        request = {
            "search_mode": "JOB_SEARCH",
            "request_metadata": request_metadata,
            "job_query": job_query,
            "jobView": "JOB_VIEW_ID_ONLY"
        }

        response = client_service.projects().jobs().search(parent=project_id, body=request).execute()

        print(response)
    except Error as e:
        raise e

request_metadata = {
    "domain": "bornasadeghi.github.io",
    "session_id": "UNKNOWN",
    "user_id": "UNKNOWN"
}

job_search(request_metadata, "engineer")