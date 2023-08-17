''' # Production Settings for MySQL DB:
db_user = "root"
db_password = "pass1234" #Enter you password database password here
db_host = "localhost"  
db_name = "test_db" #name of the database
db_port = "0000" #specify your port here
connection_uri = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
'''
# Using local sqlite server for dev

class DBcomm :
    uri = "connection_uri"