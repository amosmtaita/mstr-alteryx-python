# Install mstrio to Alteryx environment
from ayx import Package
Package.installPackages(['mstrio-py'])

# setup connectivity
mstr_username = 'HF' #changeme
mstr_password = 'mysecretpassword' #changeme
mstr_library_api_url = 'https://my.environment.com/MicroStrategyLibrary/api' #changeme
mstr_project_name = 'Alteryx' #changeme
mstr_dataset_name = 'Alteryx_mstrio' #changeme

# Write the current output to a Dataframe
from ayx import Alteryx
df = Alteryx.read("#1")

# Import MicroStrategy Python library
from mstrio import microstrategy

# connect to MicroStrategy
mstr_conn = microstrategy.Connection(base_url=mstr_library_api_url, username=mstr_username, password=mstr_password, project_name=mstr_project_name)
mstr_conn.connect()

# create MicroStrategy Dataset
mstr_conn.create_dataset(data_frame=df, dataset_name=mstr_dataset_name, table_name=mstr_dataset_name)