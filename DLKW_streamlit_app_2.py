import streamlit
import pandas
import requests
#import snowflake.connector
from urllib.error import URLError
try:
  streamlit.title('Zenas Amazing Athleisure Catalog')
except URLError as e:
  Streamlit.error()
