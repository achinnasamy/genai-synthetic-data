import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
  page_title="GenAI",
)

st.title('GenAI')
st.divider()


ctgan = False
data_syn = False
mime = False
sdv = False
faker = False

with st.sidebar:
    # Linking
    st.header('GenAI Modules')
    if st.button('CTGAN Data Factory', use_container_width=True):
        ctgan = not ctgan
    if st.button('Data Synthesizer Data Factory', use_container_width=True):
        data_syn = not data_syn
    if st.button('Mimesis Data factory', use_container_width=True):
        mime = not mime
    if st.button('SDV Data factory', use_container_width=True):
        sdv = not sdv
    if st.button('Faker Data factory', use_container_width=True):
        faker = not faker

if ctgan:
    st.subheader('CTGAN Synthetic Data')
    df1 = pd.read_csv('/workspaces/genai-synthetic-data/ctgan_generated.csv/part-00000-b303dd70-2ac7-432f-9419-c808f96268ac-c000.csv')
    df2 = pd.read_csv('ctgan_generated.csv/part-00001-b303dd70-2ac7-432f-9419-c808f96268ac-c000.csv')
    st.dataframe(df2, use_container_width= True)

if data_syn:
    st.subheader('Data Synthesizer Synthetic Data')
    df = pd.read_csv('synthoutput.csv')
    st.dataframe(df, use_container_width= True)

if mime:
    st.subheader('Mimesis Synthetic Data')
    df = pd.read_csv('mimesis_user_data.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace = True)
    st.dataframe(df, use_container_width= True)

if sdv:
    st.subheader('SDV Synthetic Data')
    df = pd.read_csv('sdv_sample_dataset.csv')
    st.dataframe(df, use_container_width= True)

if faker:
    st.subheader('Faker Synthetic Data')
    df = pd.read_csv('/workspaces/genai-synthetic-data/faker_job.csv/part-00000-153f5530-819c-4ebe-ba7c-0b71376655cb-c000.csv')
    st.dataframe(df, use_container_width= True)


