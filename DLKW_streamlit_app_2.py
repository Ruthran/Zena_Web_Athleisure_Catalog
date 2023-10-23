import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
try:
streamlit.title('Zena\'s Amazing Athleisure Catalog')
except URLError as e:
  Streamlit.error()
