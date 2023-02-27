import streamlit as st
import pandas as pd
import io

streamlit_style = """
			 <style>
        @import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
        }
        </style>
			"""



st.markdown(streamlit_style, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: #0066cc;'>TOP SPOTIFY 100 SONGS</h1>", unsafe_allow_html=True)



df = pd.read_csv("top 100 streamed songs.csv")



df_shw = st.selectbox(
     'Click below to see any info :',
     ("dataframe","info","shape","describe","columns","head","tail"))


if df_shw == "dataframe":
    st.write(df)
elif df_shw == "info":
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
elif df_shw == "shape":
    st.markdown("<h6 style='color: #000000;'>Number of Rows :</h6>", unsafe_allow_html=True)
    st.text(df.shape[0])
    st.markdown("<h6 style='color: #000000;'>Number of Columns :</h6>", unsafe_allow_html=True)
    st.text(df.shape[1])
elif df_shw == "describe":
    st.write(df.describe())
elif df_shw == "columns":
    st.write(tuple(df.columns)[0],",",tuple(df.columns)[1],",",tuple(df.columns)[2],",",tuple(df.columns)[3],",",tuple(df.columns)[4],",",tuple(df.columns)[5],",",tuple(df.columns)[6],",",tuple(df.columns)[7],",",tuple(df.columns)[8])
elif df_shw == "head":
    st.dataframe(df.head())
elif df_shw == "tail":
    st.dataframe(df.tail())

    

def convert_df(df):
     return df.to_csv().encode('utf-8')

csv = convert_df(df)


col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.download_button(label="Download ",data=csv,file_name='Spotify top 100.csv',mime='text/csv')