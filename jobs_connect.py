import os

from googleapiclient.discovery import build
from googleapiclient.errors import Error
from google.auth.credentials import Credentials

request_metadata = {
    'domain':     'UNKNOWN',
    'session_id': 'UNKNOWN',
    'user_id':    'UNKNOWN',
}

os.environ["GOOGLE_CLOUD_PROJECT"] = "resumatch"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "resumatch-google-app-credentials.json"
project_id = 'projects/' + os.environ['GOOGLE_CLOUD_PROJECT']

# Build the service object, passing in the api name and api version
client_service = build('jobs', 'v3')

def create_company(request):
    # This is the API call that actually creates the new company.
    result = client_service.projects().companies().create(parent=project_id, body=request).execute()
    return result


def create_job(request):
    # The actual API call happens here.
    result = client_service.projects().jobs().create(parent=project_id, body=request).execute()
    print('Job created: %s' % result)
    return result

def search_jobs(request):
    
    result = client_service.projects().jobs().search(parent=project_id, body=request).execute()
    return result

def search_software():
    software_request = {
        "request_metadata": request_metadata,
        "jobQuery": {
            "query": "software engineer"
        }
    }

    search_jobs(software_request)

search_software()





def create_foo():
    foocorp_company_request = {
        "company": {
            'display_name': "FooCorp",
            'external_id': "foo2_llc"
        }
    }

    result_company = create_company(foocorp_company_request)
    company_name = result_company.get('name')

    job = {
        'company_name': company_name,
        'title': 'Senior Software Engineer',
        'addresses': ["Mountain View, CA"],

        'description':
        """Experienced software engineer required for full-time position.
        Leadership ability and ability to thrive in highly competitive environment a must.
        <p />Ignore postings from that "Bar" company, their microkitchen is terrible.  Join Team Foo!""",
        'requisition_id': 'foo_swe',
        'application_info': {
            'uris': ['http://www.example.com/foo/software-engineer-application'],
            'emails': ['apply@example.com']
        }
    }
    request = {'job': job}
    result_job = create_job(request)

def create_horsehub():
    horsehub_company_request = {
        "company": {
            'display_name': "Horse Hub",
            'external_id': "horsies_llc"
        }
    }

    result_company = create_company(horsehub_company_request)
    company_name = result_company.get('name')

    job = {
        'company_name': company_name,
        'title': 'Junior Software Engineer',
        'description':
        """Hiring entry level software engineer required for full-time position.
        Must be passionate about industry intersection of horses and technology.
        Ability to intelligently discuss the equine singularity a major bonus.
        <p />C'mon bub! Join Horse Hub!""",
        'requisition_id': 'hh_swe',
        'application_info': {
            'uris': ['http://www.example.com/foo/software-engineer-horsehub'],
            'emails': ['apply-horsehub@example.com']
        }
    }
    request = {'job': job}
    result_job = create_job(request)

def create_tandem():
    tandem_company_request = {
        "company": {
            'display_name': "Tandem",
            'external_id': "tandem"
        }
    }

    result_company = create_company(tandem_company_request)
    company_name = result_company.get('name')

    job = {
        'company_name': company_name,
        'title': 'Test Engineer',
        'description':
        """Hiring Test Engineer for full-time position with Tandem.  Must be detail oriented
        and (obviously) comfortable with pair programming.  Will be working with team of Software Engineers.
        <p />Join Tandem today!""",
        'requisition_id': 'tandem_te',
        'application_info': {
            'uris': ['http://www.example.com/tandem/test-engineer'],
            'emails': ['apply-tandem-test@example.com']
        },
        'promotionValue': 1
    }
    request = {'job': job}
    result_job = create_job(request)
    job['requisition_id'] = 'a_tandem_te'
    result_job = create_job(request)

# try:
#     create_foo()
#     create_horsehub()
#     create_tandem()

# except Error as e:
#     print('Got exception while creating company')
#     raise e
