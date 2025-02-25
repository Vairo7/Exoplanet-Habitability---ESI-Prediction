import pandas as pd
from sqlalchemy import create_engine

USERNAME = 'root'
PASSWORD = 'pass'
HOST = '127.0.0.1'
DATABASE = 'exo'

engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}')

