# Install the library using pip: pip install sentence-transformers

"""## Load the BERT Model"""
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('bert-base-nli-mean-tokens')

"""## Setup a Corpus"""
# Example corpus of job descriptions
job1 = "We are seeking a savvy wordsmith to join our blogging team. Candidates must have a knack and love for writing, a comprehensive understanding of the industry, and experience in blogging to achieve business goals. The blogger will be expected to sustain and develop the company's voice across all blog content. "
job2 = "Do you tweet, share, and post to social media in your sleep? Do you know what it takes to grow an online community? We're looking for a social media manager to manage our social media accounts by implementing strategies and tactics that grow our followers, engage and retain them, and help convert them into leads, customers, and active fans and promoters of our company. You should have command of best practices and trends in social media marketing, enjoy being creative, and understand how to both build and convert a digital audience."
job3 = "We are looking for an amazing, data-driven inbound marketer to own the majority of the marketing funnel for our company. You will be in charge of attracting site traffic, converting that traffic into new leads for the business, and nurturing those leads to close into customers, the latter of which sales leadership will help you accomplish."
job4 = "We’re looking for an organized and driven Staff Accountant to join our growing team at our company. The Staff Accountant position will work closely with our other accountants and operations personnel and handle day-to-day bookkeeping. We’re an energetic company and are looking for a passionate individual to join our organization and revitalize our record keeping and bring more organization to our day to day financials."
job5 = "Our residential design firm is looking for a Lead Architect to manage our contract design department. The successful candidate will be responsible for creating, evaluating and manipulating designs to meet the needs of our clientele. We focus on energy-efficient designs, so we’re looking for a licensed architect with green building experience. Additionally, the ideal candidate should be open to contributing designs to our online repository of residential blueprints. Such contributions earn commissions in addition to the candidate’s base salary. If you are looking for an exciting opportunity to join a growing team of dedicated architects, we’re interested in meeting with you."
job6 = "You are a highly collaborative individual who is capable of laying aside your own agenda, listening to and learning from colleagues, challenging thoughtfully and prioritising impact. You search for ways to improve things and work collaboratively with colleagues. You believe in iterative change, experimenting with new approaches, learning and improving to move forward quickly."
job7 = "Deep understanding of machine learning/data mining algorithms and techniques Experiences in processing and analyzing both structured and unstructured data Solid knowledge of big data processing framework and tools, such as Spark, Hadoop, MapReduce, etc. Proficiency in one or more programming languages including but not limited to: Python, Java, Scala, R Strong analytical and problem solving skills Ability to effectively communicate analysis results to customers and negotiate options at management levels Comfort working in a dynamic R&D group with several ongoing concurrent projects"
job8 = "We are seeking an experienced graphic designer to own the creation and maintenance of both our marketing assets and content created to support the product and other marketing goals. From concept through execution, this candidate will improve our user experience by bringing our brand to life and keeping it consistent across all our various touchpoints: "
jobs = [job1, job2, job3, job4, job5, job6, job7, job8]

# Each sentence is encoded as a 1-D vector with 78 columns
sentence_embeddings = model.encode(jobs)
#print('Sample BERT embedding vector', sentence_embeddings[0])

"""## Perform Semantic Search"""
import scipy
query = 'Excellent communication, collaboration, and planning skills with meticulous attention to detail Ability to successfully organize, prioritize and manage multiple projects under strict deadlines Ability to work weekends from home Ability to write copy that is both emotional and informational You are current with pop culture, music, entertainment news and industry trends Expert understanding of the social ecosystem and how brands should participate in an authentic way Confident in publishing copy and content to mass audiences Experience in music/entertainment specific social media is a major A passion for working in a fast-paced environment with passionate teammates Strategic and creative thinker who can pro-actively problem solve'
queries = [query]
query_embeddings = model.encode(queries)

# Find the closest 5 job descriptions of the corpus for each resume based on cosine similarity
number_top_matches = 5

print("Search Results")

for query, query_embedding in zip(queries, query_embeddings):
    distances = scipy.spatial.distance.cdist([query_embedding], sentence_embeddings, "cosine")[0]

    results = zip(range(len(distances)), distances)
    results = sorted(results, key=lambda x: x[1])

    print("\n======================\n")
    print("Resume:", query)
    print("\nTop 5 most similar jobs in corpus:")

    for idx, distance in results[0:number_top_matches]:
        print(sentences[idx].strip(), "(Similarity: %.4f)" % (1-distance))