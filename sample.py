import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime

#page setting
st.set_page_config(
     page_title="QRAFT XAI",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded"
 )

#data load
data0 = pd.read_csv('attr_0_tableau.csv')
data1 = pd.read_csv('attr_1_tableau.csv')
data2 = pd.read_csv('attr_2_tableau.csv')
data3 = pd.read_csv('attr_3_tableau.csv')
data4 = pd.read_csv('attr_4_tableau.csv')
data5 = pd.read_csv('attr_5_tableau.csv')
data6 = pd.read_csv('attr_6_tableau.csv')
data7 = pd.read_csv('attr_7_tableau.csv')
data8 = pd.read_csv('attr_8_tableau.csv')

#make set
data_dict = {'A069500' : data0,
            'A148070' : data1,
            'GLD' : data2,
            'GSG' : data3,
            'SPY' : data4,
            'SHY' : data5,
            'TLT' : data6,
            'IEI' : data7,
            'TIP' : data8
            }

#st.write(data_dict.keys())

#set title
st.title('QRAFT XAI')

#set data
data_filter = st.selectbox('Which label do you want to see?', data_dict.keys())
get_data = data_dict.get(data_filter)
#st.dataframe(get_data)

#set date
DATE_COLUMN = 'date'
date_list = list(get_data[DATE_COLUMN].unique())
month_to_filter = st.selectbox('Which month do you want to see?', date_list)

# Attr
attr_data = get_data.drop(['no', 'std'], axis=1)
feature_list = list(attr_data['feature'].unique())
#st.dataframe(attr_data)

filtered_attr_data = attr_data[attr_data['date'] == month_to_filter]
filtered_attr_data = filtered_attr_data.drop(['date'], axis=1)
filtered_attr_data = filtered_attr_data.set_index('feature')
#st.dataframe(filtered_attr_data)

col1, col2 = st.columns([3,1])

with col1:
    # Feature Attribution
    st.subheader('Feature Attribution')
    st.bar_chart(filtered_attr_data['attr'], width=300, height=800)
with col2:
    # Attr top n filter
    st.subheader('Top 5 Attributed Feature')
    st.table(filtered_attr_data['attr'].nlargest(5))

    # Attr bottom n filter
    st.subheader('Bottom 5 Attributed Feature')
    st.table(filtered_attr_data['attr'].nsmallest(5))


# Std
std_data = get_data.drop(['no', 'attr'], axis=1)
#st.dataframe(std_data)

filtered_std_data = std_data[std_data['date'] == month_to_filter]
filtered_std_data = filtered_std_data.drop(['date'], axis=1)
filtered_std_data = filtered_std_data.set_index('feature')
#st.dataframe(filtered_std_data)

col3, col4 = st.columns([3,1])

with col3:
    st.subheader('Feature Standard Error')
    st.bar_chart(filtered_std_data['std'], width=300, height=400)
with col4:
    st.empty()