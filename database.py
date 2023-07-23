from sqlalchemy import create_engine, text

db_connet_string="mysql+pymysql://ezjv4sn1lunlzs6gccl5:pscale_pw_TiUa4iWFHI3K2hr6iAXimloSnwTnbRVwkxjYNXPuMNR@aws.connect.psdb.cloud/chicareers?charset=utf8mb4"

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