import requests

app_id = "39d6c493"
app_key = "6ad5db09f3191ccf9b7e5b4b1f476af7"

def search_jobs(query, country_code="us", num_results=5):
    '''
    Parameters
        country_code (str):
            one of at, au, br, ca, de, fr, gb, in, it, nl, nz, pl, ru, sg, us, za

        query (str):
            what to search the job api for

        num_results (int):
            how many jobs to return

    Returns: list of dicts
    '''
    response = requests.post("http://api.adzuna.com/v1/api/jobs/%s/search/1?app_id=%s&app_key=%s&results_per_page=%d&what=%s&content-type=application/json" 
        % (country_code, app_id, app_key, num_results, query.replace(" ", "-"))).json()

    jobs = []
    for job in response['results']:
        jobs.append(
            {
                "title": job["title"],
                "description": job["description"],
                "link": job["redirect_url"]
            }
        )
    return jobs


'''
Below is a sample response.

{
    'contract_time': 'full_time',
    'description': 'Description: WebDeveloper 3 The Sr. WebDeveloper/<strong>Software</strong> <strong>Engineer</strong> 3 possesses and applies a broad knowledge ofprinciples and practices in the field of <strong>software</strong> <strong>engineering</strong> ...',
    'adref': 'eyJhbGciOiJIUzI1NiJ9.eyJpIjoiMTU0NzMzNDIxOSIsInMiOiJfdm9aY2JDWTZoR0JYUmlLM3hvYWZBIn0.-QqU082Bsl-iUJ4Qc0o2vtjPTkd4JRMGN1ahnVzWVcY', 
    'company': {
        'display_name': 'Asurion', 
        '__CLASS__': 'Adzuna::API::Response::Company'}, 
    'category': {
        'tag': 'it-jobs', 
        '__CLASS__': 'Adzuna::API::Response::Category', 
        'label': 'IT Jobs'}, 
    'location': {
        'area': ['US', 'Florida', 'Orange County', 'Orlo Vista'], 
        '__CLASS__': 'Adzuna::API::Response::Location', 
        'display_name': 'Orlo Vista, Orange County'}, 
    'latitude': 28.51568, 
    'salary_is_predicted': '0', 
    'title': '<strong>Software</strong> <strong>Engineer</strong> 3', 
    'longitude': -81.48228, 
    'id': '1547334219', 
    'created': '2020-05-17T19:34:57Z', 
    'redirect_url': 'https://www.adzuna.com/land/ad/1547334219?se=_voZcbCY6hGBXRiK3xoafA&utm_medium=api&utm_source=39d6c493&v=CF722762DF8CDB54D8F7A8B5A1F560BBA5FF51AA', 
    '__CLASS__': 'Adzuna::API::Response::Job'
}
'''
