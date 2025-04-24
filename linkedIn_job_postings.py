from huggingface_hub import hf_hub_download
import pandas as pd

df = pd.read_csv("hf://datasets/datastax/linkedin_job_listings/postings.csv")
