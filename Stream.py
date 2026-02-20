import streamlit as st
import pandas as pd
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
ts=time.time()
date=datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
timstmp=datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#auto refresh
count=st_autorefresh(interval=2000,limit=100,key='fizzbuzzcounter')
# if count==0:
#     st.write()
df= pd.read_csv('Attendence/attendence_'+date+'.csv')
st.dataframe(df.style.highlight_max(axis=0))

# streamlit run stream.py