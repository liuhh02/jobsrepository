"""## Load the BERT Model"""
from sentence_transformers import SentenceTransformer
import scipy
import pandas as pd

def calculate_similarity(job_embeddings, resume_embeddings):
    distance = scipy.spatial.distance.cdist([job_embeddings], [resume_embeddings], "cosine")[0]
    similarity = 1-distance[0]
    return similarity

def find_similarity(jobs, resume):
	'''
    Parameters
        jobs (pd.DataFrame):
            a pandas DataFrame containing job title, job description & link to website

        resume (str):
            data extracted from the resume

    Returns: list of dicts
    '''
	model = SentenceTransformer('bert-base-nli-mean-tokens')
	# Each sentence is encoded as a 1-D vector with 78 columns
	resume_info = [resume]
	resume_embeddings = model.encode(resume_info)

	# Get embeddings of jobs in the jobs DataFrame
	jobs['embeddings'] = model.encode(jobs['description'])
	jobs['similarity'] = jobs['embeddings'].apply(calculate_similarity, args=resume_embeddings)
	jobs = jobs.sort_values(by=['similarity'], ascending=False)
    jobs = jobs[['title', 'description', 'link', 'similarity']]
    jobs = jobs.reset_index()
    jobs = jobs[['title', 'description', 'link', 'similarity']]
    jobs_dict = jobs.to_dict()

	return jobs_dict

'''
Below is a sample response.


{'title': 
{0: 'Software Engineer 1', 
 1: 'Software Engineer 4',
 2: 'Software Engineering Lead', 
 3: 'Software Engineer 2',
 4: 'Software Engineer 3'},
 'description': 
 {0: 'Description: Software Engineer 1 Product Development Nashville, TN Asurion s product development teams are focused on helping people love and get the most from technology. We re ...',
  1: 'Description: Software Engineer 4 Enterprise Data Services For twodecades, Asurion has led the technology protection industry around the globe.The Company provides premier support ...',
  2: 'Description: Software Engineering Lead Product Development Nashville, TN Asurion s product development teams are focused on helping people love and get the most from technology ...  a team of software engineers of varying experience levels Partner with product management and design peers to take advantage of new technologies and incorporate a whole-team approach ...',
  3: 'Description: Software Engineer 2 Product Development Nashville, TN Asurion s product development teams are focused on helping people love and get the most from technology. We re ...',
  4: 'Description: WebDeveloper 3 The Sr. WebDeveloper/Software Engineer 3 possesses and applies a broad knowledge ofprinciples and practices in the field of software engineering ...'},
 'link': 
 {0: 'https://www.adzuna.com/land/ad/1547334217?se=5r5F6MCY6hGfPB0frV0H3g&utm_medium=api&utm_source=39d6c493&v=CCC22F133433CB38A3E35FF118F7ED90A9167F69',
  1: 'https://www.adzuna.com/land/ad/1547334202?se=5r5F6MCY6hGfPB0frV0H3g&utm_medium=api&utm_source=39d6c493&v=2812759E5C63F0D040948AFEB09B18FDD8257B78',
  2: 'https://www.adzuna.com/land/ad/1539277557?se=5r5F6MCY6hGfPB0frV0H3g&utm_medium=api&utm_source=39d6c493&v=5988B20D7F50239DCC93A92902CAEE62A9C9D993',
  3: 'https://www.adzuna.com/land/ad/1547334218?se=5r5F6MCY6hGfPB0frV0H3g&utm_medium=api&utm_source=39d6c493&v=ED409EC832B1170A0BFDC1B9C97CA3FD11283C58',
  4: 'https://www.adzuna.com/land/ad/1547334219?se=5r5F6MCY6hGfPB0frV0H3g&utm_medium=api&utm_source=39d6c493&v=CF722762DF8CDB54D8F7A8B5A1F560BBA5FF51AA'},
 'similarity': 
 {0: 0.5655256148302235,
  1: 0.54622512610916,
  2: 0.5427682377921388,
  3: 0.5380590376419644,
  4: 0.5194907625451657}
}
'''