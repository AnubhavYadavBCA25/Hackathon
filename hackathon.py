import streamlit as st
import pandas as pd

# Load datasets
df_state = pd.read_csv('dataset_tk.csv')
df_long = pd.read_csv('long_data_.csv')

# Convert object to timestamp
df_state['TimeStamp'] = pd.to_datetime(df_state['Unnamed: 0'],format="%d/%m/%Y %H:%M:%S")
df_long['Dates_Time'] = pd.to_datetime(df_long['Dates'],format="%d/%m/%Y %H:%M:%S")

# Delete unrelevent columns
df_state = df_state.drop('Unnamed: 0',axis=1)
df_long = df_long.drop('Dates',axis=1)

# Map
st.subheader('Most Power Usage in a particular state',divider='rainbow')
st.map(data=df_long,latitude=df_long['latitude'],longitude=df_long['longitude'])

# Time-series graph
st.subheader('Power Consumption in Selected State',divider='rainbow')
option = st.selectbox('Select your State:',df_state.columns)
st.write('Your State:',option)
st.line_chart(df_state,x='TimeStamp',y=str(option))

