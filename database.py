from sqlalchemy import create_engine, text

db_connet_string="mysql+pymysql://22xmk0237wkn2bbfwe7z:pscale_pw_MGlsH6eED36ndFrbs2KnPWI8JfmpjB9IkvINidr2ZB3@aws.connect.psdb.cloud/chicareer2?charset=utf8mb4"

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