from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv() 

db_connet_string=os.environ['User']

engine = create_engine(db_connet_string,
                       connect_args={
                           "ssl":{
                               "ssl_ca": "/etc/ssl/cert.pem",
                           }
                       })


def load_jobs_from_db():
    with engine.connect() as conn:
        result= conn.execute(text("select * from jobs"))
        results_as_dict = result.mappings().all()

        jobs=[]
        for row in results_as_dict:
            jobs.append(dict(row))
        return jobs
    
        

def load_job_from_db(id):
  with engine.connect() as conn:

    result = conn.execute( text("SELECT * FROM jobs WHERE id = {}".format(id)))

    results_as_dict = result.mappings().all()
    jobs=[]
    for row in results_as_dict:
        jobs.append(dict(row))        

    if len(jobs) == 0:
      return None
    else:
      return dict(jobs[0])