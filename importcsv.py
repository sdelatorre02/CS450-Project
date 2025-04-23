import csv

rows = "job_id,company_name,title,description,max_salary,pay_period,location,company_id,views,med_salary,min_salary,formatted_work_type,applies,original_listed_time,remote_allowed,job_posting_url,application_url,application_type,expiry,closed_time,formatted_experience_level,skills_desc,listed_time,posting_domain,sponsored,work_type,currency,compensation_type,normalized_salary,zip_code,fips".split(',')

with open('postings.csv', mode ='r', encoding='utf-8') as file, \
    open('dataset.csv', mode='w', encoding='utf-8', newline='') as outfile:

    postings = csv.DictReader(file)
    posting_list = list(postings)

    sorted_postings = sorted(
        (row for row in posting_list if row["applies"] != ''), 
        key=lambda row: float(row["applies"]))

    dataset = csv.DictWriter(outfile, fieldnames=rows)
    dataset.writeheader()

    for row in sorted_postings:
        dataset.writerow(row)